label dream:
    # todo: add snore effect
    "zzZZzz"

    menu:
        "What's that feeling on my skin?"

        "[Fire]":
            $ dream_choice = Fire
            jump meet_chicken_guide_first
            
        "[Water]":
            $ dream_choice = Water
            jump meet_pig_guide_first

        "[Air]":
            $ dream_choice = Air
            jump meet_chicken_guide_first

        "[Earth]":
            $ dream_choice = Earth
            jump meet_pig_guide_first
    
label meet_chicken_guide_first:
    show guide_c at left

    call meet_introduction

    guide_c "I'm [guide_c]! Pleased to meet you, I'm excited to be involved with your journey."

    jump meet_pig_guide_second

label meet_pig_guide_first:
    show guide_p at left
    
    call meet_introduction

    guide_p "I'm [guide_p]! Pleased to meet you, I'm exicited to be committed to your journey."
    jump meet_chicken_guide_second

label meet_chicken_guide_second:
    guide_p "And here is my fowl colleage [guide_c]."
    show guide_c at right
    
    jump guides_all_introduced

label meet_pig_guide_second:
    guide_c "And here is my swine associate [guide_p]."
    show guide_p at right
    
    jump guides_all_introduced

label meet_introduction:
    "Hello there! Who might you be?"
    p "I'm [p]. And you are?"
    return

label guides_all_introduced:
    "[guide_c] and [guide_p]" "Now that we know eachother. We can start our journey."
    p "What journey are you talking about?"

    if dream_choice == Fire:
        jump dream_fire_first
    if dream_choice == Water:
        jump dream_water_first
    if dream_choice == Air:
        jump dream_wind_first
    if dream_choice == Earth:
        jump dream_earth_first