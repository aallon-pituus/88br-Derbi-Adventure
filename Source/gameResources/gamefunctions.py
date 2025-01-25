# Tuo tarvittavat moduulit
import time, random, os
from gameResources import string_table as tab #type: ignore

######################################
## Osio 1: Pelin alku ja valmistelu ##
######################################

# Tyhjennä terminaali
def clear_screen():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS and Linux
        os.system("clear")


# Kirjoita tekstiä hitaasti
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


# Pelin aloitus-funktio
def start():
    while True:
        clear_screen()
        print(tab.logo())
        print("Versio: Alpha-v0.1.0\n\n1. Aloita uusi peli\n2. Lue lisenssitiedot / Read license information\n3. Mitä lisättiin uudessa versiossa?\n\nSyötä numero: ")
        aloitus_valinta = input("\n>> ")
        if aloitus_valinta == "1":
            break
        elif aloitus_valinta == "3":
            clear_screen()
            print(tab.new())
            input("\nPaina ENTER jatkaaksesi.")
        elif aloitus_valinta == "2":
            clear_screen()
            print(tab.smaller())
            lisenssi_valinta = input(">> ")
            if lisenssi_valinta.lower() == "l":
                clear_screen()
                print(tab.full())
                input("\nPaina ENTER jatkaaksesi. Press ENTER to continue. ")


# Aseta muuttujien arvo
def setup():
    global money, style, speed, derbilaatu, poliisi, hunger, in_bed, sanity, giffit, discord_ban, dark_web_access, kvk_ban, refrigerator_food
    money = 10
    style = 0
    speed = 0
    derbilaatu = 0
    poliisi = 0
    hunger = 0
    sanity = 10
    discord_ban = False
    giffit = False
    in_bed = True
    dark_web_access = False
    kvk_ban = False
    refrigerator_food = True

def check(variable):
    global dark_web_access, kvk_ban, discord_ban
    if variable == "dark_web_access":
        return dark_web_access
    if variable == "kvk_ban":
        return kvk_ban

# Tulosta pelaajan edistyminen
def stats_print():
    global money, derbilaatu, style, speed, hunger, sanity
    fmoney, fderbilaatu, fstyle, fspeed, fhunger, fsanity = f"Raha: {money}", f"Derbin laatu: {derbilaatu}", f"Tyylipisteet: {style}", f"Nopeus: {speed}", f"Nälkä: {hunger}", f"Mielenterveys: {sanity}"
    highest = max(len(fmoney), len(fderbilaatu), len(fstyle), len(fspeed), len(fhunger), len(fsanity))
    border = "=" * highest
    print(f"\n{border}\n{fmoney}\n{fderbilaatu}\n{fstyle}\n{fspeed}\n{fhunger}\n{fsanity}\n{border}")

# Pelin häviäminen (tehty valmiiksi, jotta helpompi käytää tulevaisuudessa)
def lose(condition):
    if condition == "test":
        tab.lose()
        slow_print("\Hävisit pelin!")
        stats_print()

# Saavut peliin
def place_bedroom():
    global in_bed
    if in_bed:
        in_bed_str = "Heräsit sängyssäsi ja nousit ylös."
    else:
        in_bed_str = "Palasit sänkysi luokse."
    clear_screen()
    stats_print()
    slow_print(f"\n{in_bed_str} Haistat huoneesi Wunderbaumin raikastaman mintun hajuisen ilman.")
    slow_print("A: Mene alakertaan")
    slow_print("B: Mene työpöydän äärelle")
    in_bed = False
    while True:
        bedroom_choice = input("\n>> ").lower()

        if bedroom_choice == "a":
            slow_print("\nKävelit alakertaan.")
            time.sleep(2)
            break
        elif bedroom_choice == "b":
            slow_print("\nKävelit työpöytäsi luo ja istuit tuolille.")
            time.sleep(2)
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

    return bedroom_choice

########################################
## Osio 2: Pelin ensimmäiset valinnat ##
########################################

# Menit alakertaan
def place_downstairs():
    clear_screen()
    stats_print()
    slow_print("\nNäet edessäsi keittiön, television ja oven takapihallesi.")
    slow_print("A: Mene keittiöön")
    slow_print("B: Mene television äärelle")
    slow_print("C: Mene takapihalle")
    slow_print("D: Mene takaisin yläkertaan")
    while True:
        downstairs_choice = input("\n>> ").lower()

        if downstairs_choice == "a":
            slow_print("\nKävelet keittiöön...")
            time.sleep(2)
            break
        elif downstairs_choice == "b":
            slow_print("\nIstut sohvalle television edessä...")
            time.sleep(2)
            break
        elif downstairs_choice == "c":
            slow_print("\nLaitat raksavaatteet päälle ja kävelet takapihalle...")
            time.sleep(2)
            break
        elif downstairs_choice == "d":
            slow_print("\nPalaat yläkertaan...")
            time.sleep(2)
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

    return downstairs_choice


# Menit pöydän äärelle
def place_desk():
    clear_screen()
    stats_print()
    slow_print("\nNäet edessäsi tietokoneen.")
    slow_print("A: Käynnistä tietokone")
    slow_print("B: Poistu pöydän ääreltä")
    while True:
        desk_choice = input("\n>> ").lower()

        if desk_choice == "a":
            slow_print("\nKäynnistit tietokoneen...")
            time.sleep(2)
            break
        elif desk_choice == "b":
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

    return desk_choice

######################
## Osio 3: Alakerta ##
######################

def item_tv():
    clear_screen()
    stats_print()
    slow_print("\nIstuit sohvalle television äärelle.")
    slow_print("Televisiosta näkyy Top Gear.")
    slow_print("A: Katso Top Gearia")
    slow_print("B: Poistu television ääreltä")
    while True:
        tv_choice = input("\n>> ")
        if tv_choice == "a":
            slow_print("\nAudi RS8:n moottori irtoaa yhtäkkiä kuin taikatempusta ja lentää konepellin läpi kesken ajon.")
        elif tv_choice == "b":
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

def place_kitchen():
    clear_screen()
    stats_print()
    slow_print("\nOlet keittiössä. Näet edessäsi jääkaapin")
    slow_print("A: Avaa jääkaappi")
    slow_print("B: Poistu keittiöstä")
    while True:
        kitchen_choice = input("\n>> ")
        if kitchen_choice == "a":
            slow_print("\nAvaat jääkaapin...")
            time.sleep(2)
            break
        elif kitchen_choice == "b":
            slow_print("\nPoistut keittiöstä...")
            time.sleep(2)
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

    return kitchen_choice

def item_refrigerator():
    global hunger, refrigerator_food
    clear_screen()
    stats_print()
    slow_print("\nJääkaapissa on Roiskeläppä-pizza ja Megaforce-energiajuoma.")
    slow_print("A: Syö pizza ja juo energiajuoma")
    slow_print("B: Sulje jääkaappi")
    while True:
        refrigerator_choice = input("\n>> ")
        if refrigerator_choice == "a" and refrigerator_food:
            clear_screen()
            stats_print()
            slow_print("\nKävelet mikrolle ja lämmität pitsan...")
            time.sleep(4)
            slow_print("\nSyöt pitsan...")
            time.sleep(4)
            slow_print("\nJuot Megaforcen...")
            time.sleep(4)
            slow_print("\nOlet yltäkylläinen!")
            time.sleep(2)
            hunger -= 5
            refrigerator_food = False
            break
        if refrigerator_choice == "a" and refrigerator_food == False:
            slow_print("\nJääkaapissa ei ole ruokaa...")
        if refrigerator_choice == "b":
            slow_print("\nSuljet jääkaapin...")
            time.sleep(2)
            break

#######################
## Osio 4: Tietokone ##
#######################

# Käynnistit tietokoneen
def item_computer():
    clear_screen()
    stats_print()
    slow_print('\nTietokoneesi näyttö tulee näkyviin. Näet derbi-taustakuvasi.')
    slow_print("A: Avaa nettiselain")
    slow_print("B: Avaa Discord")
    slow_print("C: Sammuta tietokone")
    if dark_web_access == True:
        slow_print("D: Avaa Tor-selain")
    while True:
        computer_choice = input("\n>> ").lower()

        if computer_choice == "a":
            slow_print("\nSovellus avautuu...")
            time.sleep(2)
            break
        elif computer_choice == "b":
            slow_print("\nSovellus avautuu...")
            time.sleep(2)
            break

        elif computer_choice == "c":
            slow_print("\nSammutat tietokoneen...")
            time.sleep(2)
            break

        elif computer_choice == "d":
            slow_print("\nSovellus avautuu...")
            time.sleep(2)
            break

        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

    return computer_choice


# Avasit nettiselaimen
def app_browser():
    clear_screen()
    stats_print()
    slow_print("\nNettiselain käynnistyi. Näet edessäsi hakupalkin. Kirjoita kirjain tai tuettu nettisivu.")
    slow_print("A: Mene incognito tilaan")
    slow_print("B: Poistu nettiselaimesta")
    slow_print("C: Mene YouTubeen")
    slow_print("D: Mene Alibabaan")
    slow_print("E: Mene Redditiin")
    if dark_web_access:
        slow_print("F: Selaa suosittuja dark web sivustoja")
    while True:
        browser_choice = input("\n>> ").lower()

        if browser_choice == "a":
            break
        elif browser_choice == "b":
            slow_print("\nSuljet sovelluksen...")
            time.sleep(2)
            break
        elif browser_choice == "c":
            slow_print("\nAvaat YouTuben...")
            time.sleep(2)
            break
        elif browser_choice == "d":
            slow_print("\nAvaat Alibaban...")
            time.sleep(2)
            break
        elif browser_choice == "tor.org" and dark_web_access == False:
            slow_print("\nAvaat Tor-selaimen lataussivun...")
            time.sleep(2)
            break
        elif browser_choice == "tor.org" and dark_web_access:
            slow_print("\nOlet jo ladannut Tor-selaimen.")
            time.sleep(2)
        elif browser_choice == "e":
            slow_print("\nAvaat Redditin...")
            time.sleep(2)
            break
        elif browser_choice == "f":
            slow_print("\nEtsit vastauksia...")
            time.sleep(2)
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista tai se on nettisivu jota ei tueta. Yritä uudelleen.")

    return browser_choice

#####################
## Osio 5: Discord ##
#####################

# Discord
def app_discord():
    clear_screen()
    stats_print()
    slow_print("\nAvasit Discordin!")
    if kvk_ban == False:
        slow_print("A: Avaa keulakulma-vihaajan kellari -serveri.")
    slow_print("B: Avaa teletapit faniserveri.")
    slow_print("C: Sulje discord.")

    while True:
        discord_choice = input("\n>> ").lower()

        if discord_choice == "a" and kvk_ban == False:
            slow_print("\nAvaat keulakulma-vihaajan kellari -serverin...")
            time.sleep(2)
            break
        elif discord_choice == "b":
            slow_print("\nAvaat teletappi-palvelimen!")
            time.sleep(2)
            break

        elif discord_choice == "c":
            slow_print("\nSuljet sovelluksen...")
            time.sleep(2)
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

    return discord_choice

# Keulakulma-vihaajan kellari
def keulakulma_vihaajan_kellari():
    global sanity, poliisi, giffit, kvk_ban
    clear_screen()
    stats_print()
    slow_print("\nYleis-kanavan vastenmieliset GIFfit aiheuttavat sinulle henkistä tuskaa!")
    sanity -= 4
    slow_print("A: Tallenna GIFfit.")
    slow_print("B: Poistu paikalta ennen kun on liian myöhäistä.")
    slow_print("C: Ilmianna palvelin Discordille.")

    while True:
        kvk_choice = input("\n>> ").lower()

        if kvk_choice == "a":
            slow_print("\nEi kannata näyttää näitä edes terapeutillesi!")
            poliisi += 1
            giffit = True
            time.sleep(2)
            break

        elif kvk_choice == "b":
            slow_print("\nViisas valinta.")
            time.sleep(2)
            break

        elif kvk_choice == "c":
            slow_print("\nOlet sankari! Palvelin bännättiin!")
            sanity += 2
            kvk_ban = True
            time.sleep(2)
            break

        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")


#teletapit
def teletapit():
    global poliisi, giffit, discord_ban
    clear_screen()
    stats_print()
    slow_print("\nTeletappi-serveri on kaiken ikäisille, ja on täynnä faneja!")
    slow_print("A: Osallistu keskusteluun teletapeista.")
    slow_print("B: Lähde serveriltä.")
    if giffit == True:
        slow_print("C: Lähetä GIFfit jotka sait keulakulma-vihaajan kellarista.")

    while True:
        teletappi_choice = input("\n>> ").lower()

        if teletappi_choice == "a":
            slow_print("\nTiesitkö, että teletapit oli ensimmäinen lapsia varten tehty TV-ohjelma?")
        elif teletappi_choice == "b":
            slow_print("\nLähdit serveriltä.")
            time.sleep(2)
            break
        elif teletappi_choice == "c" and giffit == True:
            slow_print("\nPalaute ei ollut myönteistä... Sinun tilisi bännättiin!")
            poliisi += 1
            time.sleep(2)
            discord_ban = True
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")


def discord_banned():
    global discord_ban
    if discord_ban == True:
        clear_screen()
        stats_print()
        slow_print("\nOlemme erittäin pahoillamme, Discord-tilillenne on annettu pysyvä porttikielto.")
        time.sleep(2)
        return True
    else:
        return False
    
########################
## Osio 6: Nettisivut ##
########################

def site_youtube():
    global sanity
    clear_screen()
    stats_print()
    slow_print("\nMinkä videon haluat katsoa vai haluatko poistua sivustolta?")
    slow_print("A: Poistu sivustolta")
    slow_print("B: Saul goodman theme 1h")
    slow_print("C: How to acces the dark web")
    slow_print("D: Shimmy Shimmy ay Shimmy ay Shimmy ya")
    slow_print("E: Memes from the discord basement")

    while True:
        youtube_choice = input("\n>> ").lower()

        if youtube_choice == "a":
            break

        elif youtube_choice == "b":
            slow_print("Odotat...")
            slow_print("Ja odotat...")
            slow_print("Ja odotat...")
            time.sleep(10)
            slow_print("Saat armoa, lopetan videon puolestasi.")

        elif youtube_choice == "c":
            slow_print("Do you want to access the dark web?")
            slow_print("All you have to do is type tor.org in your browser and download the Tor Browser from that website.")
            time.sleep(2)

        elif youtube_choice == "d":
            times_watched = 0
            while times_watched < 100:
                time.sleep(0.05)
                slow_print("Shimmy Shimmy ay Shimmy ay Shimmy ya")
                times_watched += 1
            time.sleep(2)

        elif youtube_choice == "e":
            slow_print("\nKatsot todellista aivomätää.")
            time.sleep(2)
            sanity -= 1

        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

# Vieraile Redditissä
def site_reddit():
    global sanity
    clear_screen()
    stats_print()
    slow_print("\nTervetuloa Redditiin!")
    slow_print("A: Keskustele muiden herrasmiesten kanssa derbeistä")
    slow_print("B: Poistu")

    while True:
        reddit_choice = input("\n>> ").lower()

        if reddit_choice == "a":
            slow_print("Sivistyt paljon!")
            chance = random.randint(1, 100)
            if chance == 5:
                sanity += 1
            time.sleep(2)
        elif reddit_choice == "b":
            slow_print("Poistut sivustolta...")
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

# Alibaba
def site_alibaba():
    global alibaba_parts, money
    clear_screen()
    stats_print()
    slow_print("\nAvaat Alibaban-nettisivun!")
    slow_print("Haluaisitko ostaa mopoon osia?")
    slow_print("A: Osta osia (2 rahaa)")
    slow_print("B: Älä osta osia")

    while True:
        alibaba_choice = input("\n>> ").lower()

        if alibaba_choice == "a":
            alibaba_parts = True
            slow_print("\nOstit osia!")
            time.sleep(2)
            break
        elif alibaba_choice == "b":
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

######################
## Osio 7: Dark Web ##
######################

# Lataa Tor-selain
def tor_download():
    global dark_web_access
    clear_screen()
    slow_print("Haluatko ladata Tor selaimen?")
    slow_print("A: Kyllä")
    slow_print("B: En halua")

    while True:
        darkdownload_choice = input("\n>> ").lower()

        if darkdownload_choice == "a":
            slow_print("\nLatasit Tor selaimen!")
            dark_web_access = True
            time.sleep(2)
            break
        elif darkdownload_choice == "b":
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

def dark_web():
    global tina_signup
    clear_screen
    stats_print
    slow_print("\nSinut on yhdistetty tor-verkkoon!\n")
    random_number1 = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    random_number2 = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    random_number3 = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    slow_print(f"1. Solmu (Vartija): {random_number1}")
    slow_print(f"2. Solmu: {random_number2}")
    slow_print(f"3. Solmu: {random_number3}")
    slow_print("\nMihin osoiteeseen haluat mennä?")
    slow_print("Kirjoita exit poistuaaksesi.")
    slow_print("\nKäy The Hidden Wikissä nettiselaimesi kautta katsomassa osoitteita.")

    while True:
        dark_web_choice = input("\n>> ").lower()

        if dark_web_choice == "exit":
            break
        elif dark_web_choice == "228w8wqeri93389298iwe98.onion":
            slow_print("\nSaavut Dark-web New-York times sivustolle!")
            slow_print("\nAika siistiä!")
            time.sleep(3)

        elif dark_web_choice == "2439552439528aaji2304932jgj3324.onion":
            slow_print("\nEi tämä sivusto ketään kinnosta.")
            time.sleep(3)

        elif dark_web_choice == "join.tina":
            time.sleep(2)
            slow_print("\nAvaamalla tämän sivun olet ilmoittautunut Tina Gamesiin!")
            slow_print("\nNähdään pian =)")
            tina_signup = True
            time.sleep(2)
            break
        else:
            slow_print("\nTuo ei ollut yksi tuetuista osoitteista. Yritä uudelleen.")


def hidden_wiki():
    clear_screen
    slow_print("\nNew York Times: 228w8wqeri93389298iwe98.onion")
    slow_print("Onion Cooking Recipes: 2439552439528aaji2304932jgj3324.onion")
    slow_print("Idk what this link is: join.tina")
    input("\nPaina ENTER jatkaaksesi. ")

#############################
## Osio 8: Derbin rakennus ##
#############################

# Derbin osien valinta
def derbi_osat():
    global money, style, speed, derbilaatu
    clear_screen()
    stats_print()
    slow_print("\nNäet takapihallasi olevan derbin, mutta siitä puuttuu osia!")
    slow_print("A: Etsit osia kotoa.")
    slow_print("B: Ostat uusia osia motonetistä. (5 rahaa)")
    slow_print("C: Korjaa ilmastointiteipillä.")
    if alibaba_parts == True:
        slow_print("D: Käytä Alibabasta ostamiasi osia. (2 rahaa)")

    while True:
        osat_choice = input("\n>> ").lower()

        if osat_choice == "a":
            slow_print("\nLöysit kotoa hieman varaosia!")
            time.sleep(2)
            derbilaatu = +1
            break
        elif osat_choice == "b" and money > 4:
            slow_print("\nSaavuit motonettiin.")
            time.sleep(2)
            slow_print("\nValitse osat.")
            slow_print("\n88BigRacing sylinteri 5 rahaa")
            moto_osat = input("\n>> ")
            break
        elif osat_choice == "b" and money < 5:
            slow_print("\nSinulla ei ole tarpeeksi rahaa.")
        elif osat_choice == "c":
            slow_print("\nMitä odotit tapahtuvan?")
            time.sleep(2)
            speed -= 1
            style -= 2
            derbilaatu -= 1
            break
        elif osat_choice == "d" and alibaba_parts == True:
            slow_print('\n"Osta halvalla, säästä mahdollisesti myös laadusta."')
            time.sleep(2)
            derbilaatu += random.randint(-1, 2)
            speed += random.randint(-1, 2)
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")


# Derbin viritys
def derbi_viritys():
    global money, style, derbilaatu, speed, poliisi
    clear_screen()
    stats_print()
    slow_print("\nPitäisikö nyt hiukan virittää mopoa...")
    slow_print("A: No ei todellakaan!")
    slow_print('B: Hiukan vääntöä ja kääntöä, "mahdollisimman laillisesti". (2 rahaa)')
    slow_print("C: Täydet virit päälle! Ei ne poliisit saa mua kiinni. (4 rahaa)")

    while True:
        viritys_choice = input("\n>> ").lower()

        if viritys_choice == "a":
            slow_print("\nEi kaikki uskalla!")
            break
        elif viritys_choice == "b" and money > 1:
            slow_print("\nNyt on virit!")
            time.sleep(2)
            money -= 2
            speed += 1
            derbilaatu += 1
            poliisi += 1
            break
        elif viritys_choice == "b" and money < 2:
            slow_print("\nSinulla ei ole tarpeeksi rahaa.")
        elif viritys_choice == "c" and money > 3:
            slow_print(
                "\nKatsot ympärillesi jännittyneenä. Toivot, että kukaan ei nähnyt virittelyjäsi..."
            )
            time.sleep(2)
            speed += 4
            style += 2
            derbilaatu += 2
            money -= 4
            poliisi += 2
            break
        elif viritys_choice == "c" and money < 4:
            slow_print("\nSinulla ei ole tarpeeksi rahaa.")
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")


# Pärinät
def derbi_ääni():
    global money, style, derbilaatu, speed, poliisi
    clear_screen()
    stats_print()
    slow_print("\nLaitetaanko päristely päälle?")
    slow_print("A: Turhaa semmoinen.")
    slow_print("B: Äänenvaimennin irti ja pärinä kuuluu.")
    slow_print(
        "C: Kyllä, ja kaiuttimet kaiken varaksi että kukaan ei saa unta! (2 rahaa)"
    )

    while True:
        ääni_choice = input("\n>> ").lower()

        if ääni_choice == "a":
            slow_print("\nEi se kaikkien juttu ole!")
            time.sleep(2)
            break
        elif ääni_choice == "b":
            slow_print("\nNyt on pärinät!")
            time.sleep(2)
            style += 1
            break
        elif ääni_choice == "c" and money > 1:
            slow_print("\nKaiuttimet...?")
            time.sleep(2)
            poliisi += 1
            style += 3
            money -= 2
            break
        elif ääni_choice == "c" and money < 2:
            slow_print("\nSinulla ei ole tarpeeksi rahaa.")
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
