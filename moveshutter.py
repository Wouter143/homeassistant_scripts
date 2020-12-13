"""" 
method which return config for an entity in a tuple. Tuples contain the following:
0: switch entity for 'up' switch.
1: switch entity for 'down' switch.
2: input entity for position value
3: delay for a complete move up
4: delay for a complete move down
"""

def get_entity_config(entity_id):

    inputDict = {
    "cover.shutter_front": ("switch.rolluik_voorkamer_up","switch.rolluik_voorkamer_down","input_number.shutter_front_input",20,20, "", "Rolluik Voorkant"), 
    "cover.shutter_back": ("switch.rolluik_achterkamer_up","switch.rolluik_achterkamer_down","input_number.shutter_back_input",30,25, "binary_sensor.living_door", "Rolluik Achterkamer"), 
    "cover.shutter_kitchen": ("switch.rolluik_keuken_up","switch.rolluik_keuken_down","input_number.shutter_kitchen_input",28,26, "binary_sensor.kitchen_door", "Rolluik Keuken")
    }
    return inputDict.get(entity_id)

#retrieve required data from data object
direction = data.get('direction')
entity_id = data.get('entity_id')

#retrieve required data from Home Assistant
cover_entity = hass.states.get(entity_id)
cover_position = cover_entity.attributes.get('current_position')

# Check the direction, set switch ID, turn off opposite switch if applicable  
if direction == 'up':
    switch = get_entity_config(cover_entity.entity_id)[0]
    opposite_switch = get_entity_config(cover_entity.entity_id)[1]
    new_position = 100
    total_move_time = get_entity_config(cover_entity.entity_id)[3]
else:
    switch = get_entity_config(cover_entity.entity_id)[1]
    opposite_switch = get_entity_config(cover_entity.entity_id)[0]
    total_move_time = get_entity_config(cover_entity.entity_id)[4]
    new_position = 0

#Set the delay time
delay = total_move_time

#First stop both switches
# switch_up = get_entity_config(cover_entity.entity_id)[0]
# switch_down = get_entity_config(cover_entity.entity_id)[1]
# hass.services.call('switch', 'turn_off', {'entity_id':switch_up}, False)
# hass.services.call('switch', 'turn_off', {'entity_id':switch_down}, False)

# Now check if the door sensor is closed for both back shutters
door_sensor_state = 'off'
if entity_id != 'cover.shutter_front':
    door_sensor_entity_id = get_entity_config(cover_entity.entity_id)[5]
    door_sensor_entity = hass.states.get(door_sensor_entity_id)
    door_sensor_state = door_sensor_entity.state

if door_sensor_state == 'off':
    #Now set currect switch to ON, delay and then back to off again
    hass.services.call('switch', 'turn_off', {'entity_id':opposite_switch}, False)
    hass.services.call('switch', 'turn_on', {'entity_id':switch}, False)
    time.sleep(delay)

    # now renew state objeect, and get  the final cover  position, if it's the same as at the start, turn the switch off, then update position.
    # If it has changed, the shutter was stopped and position is already updated, so do nothing.
    cover_entity = hass.states.get(entity_id)
    cover_position_final = cover_entity.attributes.get('current_position')

    logger.info("current_position")
    logger.info(cover_position)
    logger.info("cover_position_final")
    logger.info(cover_position_final)

    if cover_position == cover_position_final:
        logger.info("updating cover position")
        hass.services.call('switch', 'turn_off', {'entity_id':switch}, False)
        serviceData = {'entity_id' : get_entity_config(cover_entity.entity_id)[2], 'value' : new_position}
        hass.services.call('input_number', 'set_value', serviceData, False)

else:
    hass.services.call('switch', 'turn_off', {'entity_id': switch}, False)
    message_text = f'De deur bij {get_entity_config(cover_entity.entity_id)[6]} is nog open!'
    service_data = {'title': 'Deur nog open!', 'message': message_text}
    hass.services.call('notify', 'mobile_app_sm_g950f', service_data)
    hass.services.call('notify', 'mobile_app_sm_g973f', service_data)
    #Now update shutter position
