label dream_choice_third:
        menu:
            "What do you feel next?"
            
            "[Fire]" if Fire not in dream_choices:
                jump dream_fire_fourth
            "[Water]" if Water not in dream_choices:
                jump dream_water_fourth
            "[Air]" if Air not in dream_choices:
                jump dream_wind_fourth
            "[Earth]" if Earth not in dream_choices:
                jump dream_earth_fourth