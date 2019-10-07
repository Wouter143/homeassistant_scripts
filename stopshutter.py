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
entity_id = data.get('entity_id')
time_date = data.get('time')

#Set other variables
total_run_time = get_entity_config(entity_id)

#retrieve required data from Home Assistant
cover_entity = hass.states.get(entity_id)
current_position = cover_entity.attributes.get('current_position') 
logger.info(current_position)

#check the direction the shutter is currently going by comparing last_changed 
#from both switches
up_last_changed = (hass.states.get(get_entity_config(entity_id)[0]).last_changed + datetime.timedelta(hours=int(time_date[-4]))).replace(tzinfo=None)
logger.info(up_last_changed)
down_last_changed = (hass.states.get(get_entity_config(entity_id)[1]).last_changed + datetime.timedelta(hours=int(time_date[-4]))).replace(tzinfo=None)
logger.info(down_last_changed)
current_time = datetime.datetime.now()
logger.info(current_time)


if up_last_changed > down_last_changed:
    total_run_time_seconds = get_entity_config(entity_id)[3]
    run_time_seconds = (current_time - up_last_changed).seconds
    logger.info("run_time_seconds")
    logger.info(run_time_seconds)
    run_time_percentage = round((run_time_seconds / total_run_time_seconds) * 100)
    logger.info("run_time_percentage")
    logger.info(run_time_percentage)
    new_position = current_position + run_time_percentage
    logger.info("new_position")
    logger.info(new_position)
    switch = get_entity_config(entity_id)[0]
else:
    total_run_time_seconds = get_entity_config(entity_id)[4]
    run_time_seconds = (current_time - down_last_changed).seconds
    logger.info("run_time_seconds")
    logger.info(run_time_seconds)
    run_time_percentage = round((run_time_seconds / total_run_time_seconds) * 100)
    logger.info("run_time_percentage")
    logger.info(run_time_percentage)
    new_position = current_position - run_time_percentage
    logger.info("new_position")
    logger.info(new_position)
    switch = get_entity_config(entity_id)[1]

# First stop the switch
hass.services.call('switch', 'turn_off', {'entity_id':switch}, False)

# Now update shutter position
service_data = {'entity_id' : get_entity_config(entity_id)[2], 'value' : new_position}
hass.services.call('input_number', 'set_value', service_data, False)
