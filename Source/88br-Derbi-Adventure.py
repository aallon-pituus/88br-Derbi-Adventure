# Tuo vaadittu skripti
from gameResources import gamefunctions as game # VS Codelle: #type: ignore

# Avaa päävalikko
game.start()

# Anna muuttujille oletusarvot
game.setup()
choice_downstairs = ""

# Heräät talossa
choice_bedroom = game.place_bedroom()
if choice_bedroom == "a":
    # Menet alakertaan
    choice_downstairs = game.place_downstairs()
    if choice_downstairs == "c":
        # Valitse osat
        game.derbi_osat()

        # Viritä derbi
        game.derbi_viritys()

        # Pärinät
        game.derbi_ääni()
elif choice_bedroom == "b":
    game.place_desk()
