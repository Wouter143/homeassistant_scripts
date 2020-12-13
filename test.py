
service_data = {'message': 'test'}
hass.services.call('notify', 'mobile_app_sm_g950f', service_data)



# entity_id = data.get('entity_id')
# logger.info("entity: ")
# logger.info(entity_id)
# #Check which entity is triggered, retrieve entity state

# entity = hass.states.get(entity_id)
# entity_state = entity.state
# logger.info("state: ")
# logger.info(entity_state)

# if entity_id == 'light.slaapkamer':
#     #Hue in Slaapkamer is triggered
#     if entity_state == 'off':
#         logger.info("going to turn on ")
#         #light is off, turn on in nightmode
#         service_data = {'entity_id' : entity_id , 'brightness' : 1}
#         hass.services.call('light', 'turn_on', service_data)
#     elif entity_state == 'on':
#         if entity.attributes.get('brightness') < 30:
#             #light turned on in nightmode, switch to full
#             service_data = {'entity_id' : entity_id , 'brightness' : 254}
#             hass.services.call('light', 'turn_on', service_data)
#         else:
#             #light is turned on full, turn off            
#             service_data = {'entity_id' : entity_id}
#             hass.services.call('light', 'turn_off', {'entity_id' : entity_id })    
# elif entity_id == 'light.voorkamer':
#     # Hue in Voorkamer is triggered
#     if entity_state == 'off':
#         logger.info("going to turn on ")
#         #light is off, turn on with rgb value
#         service_data = {'entity_id': entity_id , 'brightness': 254, 'rgb_color': (255,139,31)}
#         hass.services.call('light', 'turn_on', service_data)
#     elif entity_state == 'on':
#         #light is turned on, turn off            
#         service_data = {'entity_id' : entity_id}
#         hass.services.call('light', 'turn_off', {'entity_id' : entity_id })
# elif entity_id == 'light.achterkamer':
#     # Hue in Achterkamer is triggered
#     if entity_state == 'off':
#         logger.info("going to turn on ")
#         #light is off, turn on with brightness 77
#         service_data = {'entity_id': entity_id , 'brightness': 77}
#         hass.services.call('light', 'turn_on', service_data)
#     elif entity_state == 'on':
#         #light is turned on, turn off            
#         service_data = {'entity_id' : entity_id}
#         hass.services.call('light', 'turn_off', {'entity_id' : entity_id })
# elif entity_id == 'light.badkamer':
#     # Hue in Badkamer is triggered, from motion sensor, determine light intensity based on
#     # current time
#     current_time = datetime.datetime.now()
#     brightness = 209
#     if current_time.hour <= 6:
#         brightness = 37
#     service_data = {'entity_id': entity_id , 'brightness': brightness}
#     hass.services.call('light', 'turn_on', service_data)
# elif entity_id == 'light.overloop':
#     if entity_state == 'off':
#         # Hue on Overloop is triggered, determine light intensity based on current time
#         current_time = datetime.datetime.now()
#         brightness = 209
#         if current_time.hour >= 23 or current_time.hour <= 6:
#             brightness = 37
#         service_data = {'entity_id': entity_id , 'brightness': brightness}
#         hass.services.call('light', 'turn_on', service_data)    
#     elif entity_state == 'on':
#         #light is turned on, turn off            
#         service_data = {'entity_id' : entity_id}
#         hass.services.call('light', 'turn_off', {'entity_id' : entity_id })