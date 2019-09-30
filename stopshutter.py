# def setInputNr(entity_id):

#     inputDict = {"cover.shutter_front": "input_number.shutter_front_input", 
#     "cover.shutter_back": "input_number.shutter_back_input", 
#     "cover.shutter_kitchen": "input_number.shutter_back_input"
#     }
#     return inputDict.get(entity_id)

# def setSwitches(entity_id):

#     inputDict = {"cover.shutter_front": ("switch.rolluik_voorkamer_up","switch.rolluik_voorkamer_down"), 
#     "cover.shutter_back": ("switch.rolluik_achterkamer_up","switch.rolluik_achterkamer_down"), 
#     "cover.shutter_kitchen": ("switch.rolluik_keuken_up","switch.rolluik_keuken_down")
#     }
#     return inputDict.get(entity_id)


# #retrieve required data from data object
# direction = data.get('direction')
# entity_id = data.get('entity_id')

# #retrieve required data from Home Assistant
# cover_entity = hass.states.get(entity_id)
# cover_position = cover_entity.attributes.get('current_position')

# # Check the direction, set switch ID
# if direction == 'up':
#     switch = "switch.rolluik_voorkamer_up"
#     newPosition = 100
# else:
#     switch = "switch.rolluik_voorkamer_down"
#     newPosition = 0

# #Set the delay time
# delay = 5

# #First stop both switches
# switch_up = setSwitches(cover_entity.entity_id)[0]
# switch_down = setSwitches(cover_entity.entity_id)[1]
# hass.services.call('switch', 'turn_off', {'entity_id':switch_up}, False)
# hass.services.call('switch', 'turn_off', {'entity_id':switch_down}, False)

# #Now set currect switch to ON, delay and then back to off again
# hass.services.call('switch', 'turn_on', {'entity_id':switch}, False)
# time.sleep(delay)
# hass.services.call('switch', 'turn_off', {'entity_id':switch}, False)

# #Now update shutter position
# serviceData = {'entity_id' : setInputNr(cover_entity.entity_id), 'value' : newPosition}
# hass.services.call('input_number', 'set_value', serviceData, False)