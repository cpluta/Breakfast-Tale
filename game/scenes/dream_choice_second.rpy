label dream_choice_second:
        menu:
            "What do you feel next?"
            
            "[Fire]" if Fire not in dream_choices:
                jump dream_fire_third
            "[Water]" if Water not in dream_choices:
                jump dream_water_third
            "[Air]" if Air not in dream_choices:
                jump dream_wind_third
            "[Earth]" if Earth not in dream_choices:
                jump dream_earth_third