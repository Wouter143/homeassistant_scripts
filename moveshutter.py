def getEntityConfig(entity_id):

    inputDict = {"cover.shutter_front": ("switch.rolluik_voorkamer_up","switch.rolluik_voorkamer_down","input_number.shutter_front_input"), 
    "cover.shutter_back": ("switch.rolluik_achterkamer_up","switch.rolluik_achterkamer_down","input_number.shutter_back_input"), 
    "cover.shutter_kitchen": ("switch.rolluik_keuken_up","switch.rolluik_keuken_down","input_number.shutter_back_input")
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
    switch = getEntityConfig(cover_entity.entity_id)[0]
    newPosition = 100
else:
    switch = getEntityConfig(cover_entity.entity_id)[1]
    newPosition = 0

#Set the delay time
delay = 20

#First stop both switches
switch_up = getEntityConfig(cover_entity.entity_id)[0]
switch_down = getEntityConfig(cover_entity.entity_id)[1]
hass.services.call('switch', 'turn_off', {'entity_id':switch_up}, False)
hass.services.call('switch', 'turn_off', {'entity_id':switch_down}, False)

#Now set currect switch to ON, delay and then back to off again
hass.services.call('switch', 'turn_on', {'entity_id':switch}, False)
time.sleep(delay)
hass.services.call('switch', 'turn_off', {'entity_id':switch}, False)

#Now update shutter position
serviceData = {'entity_id' : getEntityConfig(cover_entity.entity_id)[2], 'value' : newPosition}
hass.services.call('input_number', 'set_value', serviceData, False)