# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    $ main_player = "Sunshine"
    
    call opening
    
    # This ends the game.
    "The End"
    
    return
