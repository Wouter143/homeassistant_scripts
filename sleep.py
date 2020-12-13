switches = ["buitenlamp_spots", "buitenlamp_vlonder", "christmas_tree_relay", "exhaust_light", "hal_lamp", "led_strip", "side_lights"]
lights = ["achterkamer", "rotsverlichting", "voorkamer"]
covers = ["cover.shutter_back", "cover.shutter_front", "cover.shutter_kitchen"] 

# First, check time to determine button behavior

current_time = datetime.datetime.now()

if current_time.hour >= 5 and current_time.hour <= 15:
    # It's morning, so open all shutters
    for cover in covers:
        state = hass.states.get(cover).state
        if state == 'closed':
            service_data = {'entity_id': cover}
            hass.services.call('cover', 'open_cover', service_data)

else:
    # It's evening, so close all covers, turn off lights & turn off the tv
    # check states of 2 door sensors and attic window sensor

    kitchen_sensor = hass.states.get('binary_sensor.kitchen_door').state
    living_door_sensor = hass.states.get('binary_sensor.living_door').state
    attic_sensor = hass.states.get('binary_sensor.attic_window').state

    if kitchen_sensor == 'on' or living_door_sensor == 'on' or attic_sensor == 'on':
        open_doors = ""
        if kitchen_sensor == 'on':
            open_doors += 'Keukendeur, '
        if living_door_sensor == 'on':
            open_doors +=  'Achterkamer deur, '
        if attic_sensor == 'on':
            open_doors += 'Zolderraam '
        message = f'{open_doors} staan nog open!'
        service_data = {'message': message, 'title': 'Er staat nog iets open!'}
        hass.services.call('notify', 'mobile_app_sm_g973f', service_data)
        hass.services.call('notify', 'mobile_app_sm_g981b', service_data)

    if kitchen_sensor != 'on' and living_door_sensor != 'on':
        service_data = {'message': 'Alles is dicht, welterusten!', 'title': 'Welterusten'}
        hass.services.call('notify', 'mobile_app_sm_g973f', service_data)
        hass.services.call('notify', 'mobile_app_sm_g981b', service_data)
        for cover in covers:
            state = hass.states.get(cover).state
            if state == 'open':
                service_data = {'entity_id': cover}
                hass.services.call('cover', 'close_cover', service_data)

        for switch in switches:
            entity_id = 'switch.' + switch
            service_data = {'entity_id': entity_id}
            hass.services.call('switch','turn_off', service_data)

        for light in lights:
            entity_id = 'light.' + light
            service_data = {'entity_id': entity_id}
            hass.services.call('light','turn_off', service_data)

        tv_state = hass.states.get('media_player.lg_tv')
        if tv_state != 'off':
            service_data = {'entity_id': 'media_player.lg_tv'}
            hass.services.call('media_player', 'turn_off', service_data)
