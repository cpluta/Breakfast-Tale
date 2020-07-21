# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    call initialize_constants
    call initialize_state
    call initialize_characters

    call opening
    
    # This ends the game.
    "The End"
    
    return
