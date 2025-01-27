def tina_games_start():
    clear_screen()
    stats_print()
    slow_print("\nKaasua alkaa vuotaa huoneeseesi...")
    slow_print("...")
    slow_print("...")
    slow_print("...")
    time.sleep(2)
    slow_print("\nHeräät tuntemattomassa paikassa.")
    slow_print("Punaisiin ruumiin-peittäviin kaapuihin pukeutuneet miehet seisoo edeessäsi.")
    slow_print("Kyseiset miehet ovat aseistettuja!")
    slow_print("Ympärilläsi seisoo satoja muita ihmisiä.")
    slow_print("Ylhäältä päin kuulu ääni.")
    slow_print("Tervetuloa tina gamesiin!")
    slow_print("Voittaja palkitaan 456:ella rahalla!")
    slow_print("Aloittakaamme ensimmäinen peli!")
    
def red_green_light_start():
    clear_screen()
    stats_print()
    slow_print("\nSinut ja muut ihmiset siirretään suraavaan huoneeseen.")
    slow_print("A: Mene mukana.")
    slow_print("b: Vastusta.")
    
    while True
        comply_tin_choice = input("\n>> ").lower()
        
        if comply_tin_choice == "a":
            time.sleep(2)
            break
        if comply_tin_choice == "b":
            time.sleep(2)
            slow_print("Sinut ammuttiin!")
            lose()
            input()
            exit()
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
            
def red_green_light():
    global rngshot, lights_progress, games_reputation, contestants
    lights_progress = 0
    games_reputation = 0
    contestants = 500
    clear_screen()
    stats_print()
    slow_print("\nEdessäsi avautuu suuri kenttä, jonka perällä on punainen viiva, ja massiivinen tinapatsas.")
    slow_print("Pelin säänöt ovat simppelit!")
    slow_print("Kun tulee (green light!), saa liikkua")
    slow_print("Kun tulee (red light!), pitää pysähtyä!")
    slow_print("Yrittäkää päästä viivan yli.")
    slow_print("\nMitä teet?")
    slow_print("A: varovaisella tavalla eteneminen")
    slow_print("B: nopeasti sprinttaaminen")
    slow_print("C: yritä kaataa muita pelaajia")
    
    while True:
        red_green_choice = input("\n>> ").lower()
        
        if red_green_choice == "a":
            lights_progress += 1
            slow_print("Onnistuit pysähhtymään ajoissa!")
            break
        elif red_green_choice == "b":
            rngshot = (random.randint(0,2))
            if rngshot == 1:
                slow_print("Et pysähtynyt ajoissa! Sinut ammuttiin!")
                lose()
                input()
                exit()
            elif rngshot == 2:
                slow_print("Pääsit johtoon!")
                lights_progress += 3
        elif red_green_choice == "c"
            slow_print("Onnistuit eliminoimaan yhden pelaajan!")
                games_reputation -= 2
                contestants -= 1
                break
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
    
    slow_print("mitä teet seuraavaksi?")
    slow_print("A: Jatka matkaa rauhallisesti") 
    slow_print("B: sprinttaa")
    slow_print("C: yritä elimminoida paljon ihmisiä")
    while True:
        red_green_choice1 = input("\n>> ").lower()
        
        if red_green_choice1 == "a":
            lights_progress += 1
            slow_print("Onnistuit pysähhtymään ajoissa!")
            break
        elif red_green_choice1 == "b":
            rngshot = (random.randint(0,2))
            if rngshot == 1:
                slow_print("Et pysähtynyt ajoissa! Sinut ammuttiin!")
                lose()
                input()
                exit()
            elif rngshot == 2:
                slow_print("Onnistuit pysähtymään ajoissa!")
                lights_progress += 3
                break
        elif red_green_choice1 == "c"
            slow_print("Onnistuit eliminoimaan kaksi pelaajaa!")
                games_reputation -= 2
                contestants -= 2
                break
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
        
    if progress == 6:
        slow_print("\nLähenet maalia!")
        slow_print("Mitä teet")
        slow_print("A: Nopea loppukiri")
        slow_print("B: jatka matkaa rauhallisesti")
        slow_print("C: kaada ihmisiä")
        
        while True:
            red_green_choice2 = input("\n>> ").lower()
            
            if red_green_choice2 == "a":
                rngshot = (random.randint(0,4))
                if rngshot == 1:
                    slow_print("Innostuksessasi, sinut ammuttiin!")
                    lose()
                    input()
                    exit()
                else:
                    slow_print("Onnistuit! pääsit maaliin!")
                    lights_progress += 2
                    break
            elif red_green_choice2 == "b":
                slow_print("Olet ihan melkein maalissa!")
                lights_progress += 1
            elif red_green_choice == "c":
                slow_print("Onnistuit kaatamaan yhden pelaajan!")
                games_reputation -= 2
                contestants -= 1
                break
            
            else:
                slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
    if lights_progress == 8:
        slow_print("Pääsit maaliin! Mitä teet?")
        slow_print("A: Odota että peli loppuu")
        slow_print("B: Työnnä ihmisiä linjan toiselta puolelta")
        
        while True:
            lights_finish_choice = input("\n>> ").lower()
            
            if lights_finish_choice == "a":
                time.sleep(2)
                break
            elif lights_finish_choice == "b":
                slow_print("Sait kaadettua kolme ihmistä!")
                games_reputation -= 3
                contestants -= 3
                break
            else:
                slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
    if games_reputation < -5 and lights_progress < 8:
        slow_print("Vihainen pelaaja kosti ystävänsä!!")
        slow_print("Hävisit pelin")
        lose()
        input()
        exit()
    else:
        slow_print("mitä teet seuraavaksi?")
    slow_print("A: Jatka matkaa rauhallisesti") 
    slow_print("B: sprinttaa")
    slow_print("C: yritä elimminoida paljon ihmisiä")
    while True:
        red_green_choice1 = input("\n>> ").lower()
        
        if red_green_choice1 == "a":
            lights_progress += 1
            slow_print("Onnistuit pysähhtymään ajoissa!")
            break
        elif red_green_choice1 == "b":
            rngshot = (random.randint(0,2))
            if rngshot == 1:
                slow_print("Et pysähtynyt ajoissa! Sinut ammuttiin!")
                lose()
                input()
                exit()
            elif rngshot == 2:
                slow_print("Onnistuit pysähtymään ajoissa!")
                lights_progress += 3
                break
        elif red_green_choice1 == "c"
            slow_print("Onnistuit eliminoimaan kaksi pelaajaa!")
                games_reputation -= 2
                contestants -= 2
                break
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
    if progress == 6:
        slow_print("\nLähenet maalia!")
        slow_print("Mitä teet")
        slow_print("A: Nopea loppukiri")
        slow_print("B: jatka matkaa rauhallisesti")
        slow_print("C: kaada ihmisiä")
        
        while True:
            red_green_choice2 = input("\n>> ").lower()
            
            if red_green_choice2 == "a":
                rngshot = (random.randint(0,4))
                if rngshot == 1:
                    slow_print("Innostuksessasi, sinut ammuttiin!")
                    lose()
                    input()
                    exit()
                else:
                    slow_print("Onnistuit! pääsit maaliin!")
                    lights_progress += 2
                    break
            elif red_green_choice2 == "b":
                slow_print("Olet ihan melkein maalissa!")
                lights_progress += 1
            elif red_green_choice == "c":
                slow_print("Onnistuit kaatamaan yhden pelaajan!")
                games_reputation -= 2
                contestants -= 1
                break
            
            else:
                slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
    if lights_progress == 8:
        slow_print("Pääsit maaliin! Mitä teet?")
        slow_print("A: Odota että peli loppuu")
        slow_print("B: Työnnä ihmisiä linjan toiselta puolelta")
        
        while True:
            lights_finish_choice = input("\n>> ").lower()
            
            if lights_finish_choice == "a":
                time.sleep(2)
                break
            elif lights_finish_choice == "b":
                slow_print("Sait kaadettua kolme ihmistä!")
                games_reputation -= 3
                contestants -= 3
                break
            else:
                slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
    if games_reputation < -5 and lights_progress < 8:
        slow_print("Vihainen pelaaja kosti ystävänsä!!")
        slow_print("Hävisit pelin")
        lose()
        input()
        exit()
    else:
        slow_print("Aika alkaa loppua!")
        slow_print("Mitä teet?")
        slow_print("A: Juokse hitaasti")
        slow_print("B: Juokse keskinopeutta")
        slow_print("C: sprinttaa täysiä")
        
        while True:
            last_light_choice = input("\n>> ").lower()
            
            if last_light_choice == "a":
                slow_print("Et ehtinyt ajoissa!")
                lose()
                input()
                exit()
            elif last_light_choice == "b":
                slow_print("Ehdit juuri ja juuri!")
                time.sleep(2)
                break
            elif last_light_choice == "c":
                slow_print("Punainen valo tulee viime hetkellä! Hävisit pelin!")
                lose()
                input()
                exit()
            else:
                slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
        
