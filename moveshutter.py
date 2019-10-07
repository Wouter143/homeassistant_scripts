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
    "cover.shutter_front": ("switch.rolluik_voorkamer_up","switch.rolluik_voorkamer_down","input_number.shutter_front_input",20,20), 
    "cover.shutter_back": ("switch.rolluik_achterkamer_up","switch.rolluik_achterkamer_down","input_number.shutter_back_input",30,25), 
    "cover.shutter_kitchen": ("switch.rolluik_keuken_up","switch.rolluik_keuken_down","input_number.shutter_kitchen_input",28,26)
    }
    return inputDict.get(entity_id)

#retrieve required data from data object
direction = data.get('direction')
entity_id = data.get('entity_id')

#retrieve required data from Home Assistant
cover_entity = hass.states.get(entity_id)
cover_position = cover_entity.attributes.get('current_position')

# Check the direction, set switch ID
if direction == 'up':
    switch = get_entity_config(cover_entity.entity_id)[0]
    newPosition = 100
    total_move_time = get_entity_config(cover_entity.entity_id)[3]
else:
    switch = get_entity_config(cover_entity.entity_id)[1]
    total_move_time = get_entity_config(cover_entity.entity_id)[4]
    newPosition = 0

#Set the delay time
delay = total_move_time

#First stop both switches
# switch_up = get_entity_config(cover_entity.entity_id)[0]
# switch_down = get_entity_config(cover_entity.entity_id)[1]
# hass.services.call('switch', 'turn_off', {'entity_id':switch_up}, False)
# hass.services.call('switch', 'turn_off', {'entity_id':switch_down}, False)

#Now set currect switch to ON, delay and then back to off again
hass.services.call('switch', 'turn_on', {'entity_id':switch}, False)
time.sleep(delay)
logger.info(hass.states.get(switch).state)
if hass.states.get(switch).state == 'on':
    hass.services.call('switch', 'turn_off', {'entity_id':switch}, False)
    serviceData = {'entity_id' : get_entity_config(cover_entity.entity_id)[2], 'value' : newPosition}
    hass.services.call('input_number', 'set_value', serviceData, False)

#Now update shutter position
