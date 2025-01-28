# Tuo vaadittu skripti
from gameResources import gamefunctions as game

# Avaa päävalikko
game.start()

# Anna muuttujille oletusarvot
game.setup()

# Heräät talossa
while True:  # Makuuhuone loop
    choice_bedroom = game.place_bedroom()
    if choice_bedroom == "a":  # Jos menet alakertaan
        while True: # Alakerta loop
            choice_downstairs = game.place_downstairs()
            if choice_downstairs == "a": # Jos menet keittiöön
                while True:
                    choice_kitchen = game.place_kitchen()
                    if choice_kitchen == "a": # Jos avaat jääkaapin
                        game.item_refrigerator()
                    if choice_kitchen == "b": # Jos poistut keittiöstä
                        break # Poistut keittiöstä
            if choice_downstairs == "b": # Jos istut television äärelle
                game.item_tv()
            if choice_downstairs == "c":  # Jos menet takapihalle
                choice_derbi = game.derbi_osat()  # Valitse osat
                if choice_derbi == "b": # Jos menet Motonettiin
                    game.place_motonet() # Mene Motonettiin
                if not choice_derbi == "c": # Jos et palaa takaisin sisälle
                    game.derbi_viritys()  # Viritä derbi
                    game.derbi_ääni()  # Pärinät
            if choice_downstairs == "motonet" and game.check("motonetissä_käyty") == False: # Jos menet Motonettiin
                game.place_motonet() # Mene Motonettiin
            if choice_downstairs == "smarket": # Jos menet S-Markettiin
                game.place_smarket()
            if choice_downstairs == "e": # Jos menet takaisin ylös
                break # Mene takaisin ylös
    if choice_bedroom == "b":  # Jos menet pöydän äärelle
        while True:  # Pöytä loop
            choice_desk = game.place_desk()
            if choice_desk == "a":  # Jos valitset A pöydän luona
                while True:  # Tietokone loop
                    access_dark_web = game.check("dark_web_access")
                    choice_computer = game.item_computer()
                    if choice_computer == "a":  # Jos avaat Chromen
                        while True:  # Chrome loop
                            choice_chrome = game.app_browser()
                            if choice_chrome == "a":  # Jos avaat incognito-tilan
                                game.slow_print("Avasit incognito tilan.")
                            if choice_chrome == "b":  # Jos suljet Chromen
                                break  # Sulje Chrome
                            if choice_chrome == "c":  # jos avaat YouTuben
                                game.site_youtube()
                            if choice_chrome == "d":  # Jos avaat alibaban
                                game.site_alibaba()
                            if choice_chrome == "e":  # Avaa Reddit
                                game.site_reddit()
                            if choice_chrome == "tor.org":
                                game.tor_download()
                                break
                            if choice_chrome == "f":  # Avaa The Hidden Wiki
                                game.hidden_wiki()
                                break

                    if choice_computer == "c":  # Jos sammutat tietokoneen
                        break  # Sammuta tietokone
                    if choice_computer == "b":  # Jos avaat Discordin
                        while True:  # Discord loop
                            ban_discord = game.discord_banned()
                            if ban_discord:
                                break

                            choice_discord = game.app_discord()

                            if choice_discord == "a" and game.check("kvk_ban") == False: 
                                game.keulakulma_vihaajan_kellari()
                                    
                            elif choice_discord == "b":
                                game.teletapit()

                            elif choice_discord == "c":
                                break

                    if choice_computer == "d" and access_dark_web:
                        game.dark_web()

            if choice_desk == "b":  # Jos valitset B pöydän luona
                break  # Mene takaisin makuuhuoneeseen
