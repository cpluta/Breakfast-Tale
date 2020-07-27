label dream_fire_first:
    # todo: play sizzle sound
    "such flames"
    
    $ dream_choices.append(Fire)

    $ choices_length = len(dream_choices)-1
    $ current_index = 0

label dream_fire_loop:
    $ current_choice = dream_choices[current_index]
    "What's this? [current_choice]"

    if current_index != choices_length:
        $ current_index += 1
        jump dream_fire_loop
    
    if Water in dream_choices:
        "There is fire inside"

    "nooo"

    jump dream_choice_first