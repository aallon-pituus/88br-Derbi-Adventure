# Tuo vaadittu skripti
from gameResources import gamefunctions as game
from gameResources import string_table as tab

# Avaa päävalikko
game.start()

# Anna muuttujille oletusarvot
game.setup()

# Heräät talossa
while True: # Makuuhuone loop
    choice_bedroom = game.place_bedroom()
    if choice_bedroom == "a": # Jos menet alakertaan
        choice_downstairs = game.place_downstairs()
        if choice_downstairs == "c": # Jos menet takapihalle
            game.derbi_osat() # Valitse osat
            game.derbi_viritys() # Viritä derbi
            game.derbi_ääni() # Pärinät
    if choice_bedroom == "b": # Jos menet pöydän äärelle
        while True: # Pöytä loop
            choice_desk = game.place_desk()
            if choice_desk == "a": # Jos valitset A pöydän luona
                while True: # Tietokone loop
                    choice_computer = game.item_computer()
                    if choice_computer == "a": # Jos avaat Chromen
                        while True: # Chrome loop
                            choice_chrome = game.app_chrome()
                            if choice_chrome == "b": # Jos avaat incognito-tilan
                                game.clear_screen()
                                print(tab.lose())
                                game.slow_print("Hävisit pelin. Sinut huomattiin menemässä incognito-tilaan.")
                                game.stats_print()
                                exit()
                            if choice_chrome == "c": # Jos suljet Chromen
                                break # Sulje Chrome
                    if choice_computer == "b": # Jos sammutat tietokoneen
                        break # Sammuta tietokone
            if choice_desk == "b": # Jos valitset B pöydän luona
                break # Mene takaisin makuuhuoneeseen
