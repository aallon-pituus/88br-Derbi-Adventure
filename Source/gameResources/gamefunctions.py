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
        comply_tin_choice = input("\n>> ").lower()'
        
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
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
        
