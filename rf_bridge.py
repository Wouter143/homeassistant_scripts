'''
The following codes are available:
E1: 29C4E8
E2: 29C4E2
E3: 29C4E4
W1: AB8088 (Turn off Hue)
W2: AB8082 (Turn Hue to nightmode)
W3: AB8084 (Toggle Hue between on/off/nightmode, like button)
'''

#Grab the state of the RF_Bridge sensor
entity_id = 'sensor.rf_bridge'
entity_state = hass.states.get(entity_id).state
logger.info(entity_state)

# Now check state, and execute the method

if entity_state == 'AB8088':
    logger.info('case 1, Wouter')
    service_data = {'entity_id' : 'light.slaapkamer'}
    hass.services.call('light', 'turn_off', service_data)   
elif entity_state == 'AB8082':
    logger.info('case 2, Wouter')
    service_data = {'entity_id' : 'light.slaapkamer' , 'brightness' : 1}
    hass.services.call('light', 'turn_on', service_data)
elif entity_state == 'AB8084':
    logger.info('case 3, Wouter')
    service_data = {'entity_id' : 'light.slaapkamer'}
    hass.services.call('python_script', 'switch_lights', service_data)
elif entity_state == '29C4E8':
    logger.info('case 1, Eline')
    service_data = {'entity_id' : 'light.slaapkamer'}
    hass.services.call('light', 'turn_off', service_data)  
elif entity_state == '29C4E2':
    logger.info('case 2, Eline')
    service_data = {'entity_id' : 'light.slaapkamer' , 'brightness' : 1}
    hass.services.call('light', 'turn_on', service_data)
elif entity_state == '29C4E4':
    logger.info('case 3, Eline')
    service_data = {'entity_id' : 'light.slaapkamer'}
    hass.services.call('python_script', 'switch_lights', service_data)