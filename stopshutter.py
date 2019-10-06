
def get_entity_config(entity_id):
    inputDict = {"cover.shutter_front": ("switch.rolluik_voorkamer_up","switch.rolluik_voorkamer_down","input_number.shutter_front_input"), 
    "cover.shutter_back": ("switch.rolluik_achterkamer_up","switch.rolluik_achterkamer_down","input_number.shutter_back_input"), 
    "cover.shutter_kitchen": ("switch.rolluik_keuken_up","switch.rolluik_keuken_down","input_number.shutter_kitchen_input")
    }
    return inputDict.get(entity_id)



#retrieve required data from data object
entity_id = data.get('entity_id')

#Set other variables
total_run_time = 20

#retrieve required data from Home Assistant
cover_entity = hass.states.get(entity_id)
current_position = cover_entity.attributes.get('current_position') 
logger.info(current_position)

#check the direction the shutter is currently going by comparing last_changed 
#from both switches
up_last_changed = hass.states.get(get_entity_config(entity_id)[0]).last_changed
logger.info(up_last_changed)
down_last_changed = hass.states.get(get_entity_config(entity_id)[1]).last_changed
logger.info(down_last_changed)
logger.info(datetime.datetime.now().replace(tzinfo=datetime.timezone.utc))


# if up_last_changed > down_last_changed:
#     direction =  'up'
# else:
#     direction = 'down'
# logger.info(direction)

# # calculate new position from last_changed states, then stop switch based on current direction.

# if direction == 'up':
#     run_time_seconds = (datetime.datetime.now()- up_last_changed).seconds
#     run_time_percentage = (total_run_time/run_time_seconds)*100
#     new_position = current_position + run_time_percentage
#     switch = get_entity_config(entity_id)[0]
    
# else:
#     run_time_seconds = (datetime.datetime.now()- down_last_changed).seconds
#     run_time_percentage = (total_run_time/run_time_seconds)*100
#     new_position = current_position - run_time_percentage
#     switch = get_entity_config(entity_id)[1]
    
# # First stop the switch
# hass.services.call('switch', 'turn_off', {'entity_id':switch}, False)

# # Now update shutter position
# service_data = {'entity_id' : get_entity_config(entity_id)[2], 'value' : new_position}
# hass.services.call('input_number', 'set_value', service_data, False)
