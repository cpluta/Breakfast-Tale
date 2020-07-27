label dream_choice_first:
        menu:
            "What do you feel next?"
            
            "[Fire]" if Fire not in dream_choices:
                jump dream_fire_second
            "[Water]" if Water not in dream_choices:
                jump dream_water_second
            "[Air]" if Air not in dream_choices:
                jump dream_wind_second
            "[Earth]" if Earth not in dream_choices:
                jump dream_earth_second