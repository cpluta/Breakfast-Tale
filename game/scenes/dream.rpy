label dream:
    "Where was I again..."

    menu:
        "What is this feeling?"

        "[Hot]":
            $ dream_choice = Hot
            jump meet_chicken_guide_first
            
        "[Wet]":
            $ dream_choice = Wet
            jump meet_pig_guide_first

        "[Wind]":
            $ dream_choice = Wind
            jump meet_chicken_guide_first

        "[Dirt]":
            $ dream_choice = Dirt
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

    if dream_choice == Hot:
        "so hot"
        #block of code to run
    if dream_choice == Wet:
        #block of code to run
        "so wet"
    if dream_choice == Wind:
        #block of code to run
        "so windy"
    if dream_choice == Dirt:
        #block of code to run
        "so dirty"