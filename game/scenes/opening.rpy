label opening:
    scene black

    play sound "audio/sfx/alarm_clock.mp3" fadein 5.0 loop

    "uhhh is it morning already?"

menu:

    "Snooze Alarm":
        jump snooze

    "Wake up":
        jump wakeup

label snooze:

    m "Hey! Wake Up!" with vpunch

    stop sound

    jump wokenup

label wakeup:

    stop sound

    m "Morning [p]!"
    
    jump wokenup

label wokenup:

    scene bg room with fade

    $ pname = renpy.input("You don't need to be so loud in the morning! And stop calling me [p] you know my name is:")
    $ old_name = p;
    $ p = pname.strip()

    m "Of course I know your name. But you'll always be my [old_name]."

    p "It's too early for you to be sappy. I'm going to rest for a little longer."

    m "{cps=5}If you say so...{/cps}"    
    m "Just so you know, I'm making breakfast."
    m "So don't sleep too long before breakfast gets cold!" with vpunch

    p "Don't worry I won't."

    scene black with fade
    
    jump dream