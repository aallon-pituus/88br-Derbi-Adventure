# Tuo tarvittavat moduulit
import time, random, os
from gameResources import string_table as tab

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
        print("\n1. Aloita uusi peli\n2. Lue lisenssitiedot\n\nSyötä numero: ")
        aloitusValinta = input(">> ")
        if aloitusValinta == "1":
            break
        elif aloitusValinta == "2":
            clear_screen()
            print(tab.smaller())
        lisenssiValinta = input(">> ")
        if lisenssiValinta.lower() == "l":
            clear_screen()
            print(tab.full())
            input("\nPaina ENTER jatkaaksesi. Press ENTER to continue. ")

# Aseta muuttujien arvo
def setup():
    global money, style, speed, derbilaatu, poliisi, hunger, in_bed
    money = 10
    style = 0
    speed = 0
    derbilaatu = 0
    poliisi = 0
    hunger = 0
    in_bed = True

# Tulosta pelaajan edistyminen
def stats_print():
    global money, derbilaatu, style, speed, hunger
    fmoney, fderbilaatu, fstyle, fspeed, fhunger = f"Raha: {money}", f"Derbin laatu: {derbilaatu}", f"Tyylipisteet: {style}", f"Nopeus: {speed}", f"Nälkä: {hunger}"
    highest = max(len(fmoney), len(fderbilaatu), len(fstyle), len(fspeed), len(fhunger))
    border = "=" * highest
    print(f"\n{border}\n{fmoney}\n{fderbilaatu}\n{fstyle}\n{fspeed}\n{fhunger}\n{border}")

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

# Menit alakertaan
def place_downstairs():
    clear_screen()
    stats_print()
    slow_print("\nNäet edessäsi keittiön, television ja oven takapihallesi.")  
    slow_print("A: Mene keittiöön")  
    slow_print("B: Mene television äärelle")
    slow_print("C: Mene takapihalle") 
    while True:
        downstairs_choice = input("\n>> ").lower()

        if downstairs_choice == "a":
            slow_print("\nKävelet keittiöön.")
            time.sleep(2)
            break
        elif downstairs_choice == "b":
            slow_print("\nIstut sohvalle television edessä.")
            time.sleep(2)
            break
        elif downstairs_choice == "c":
            slow_print("\nKävelet takapihalle.")
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

# Käynnistit tietokoneen
def item_computer():
    clear_screen()
    stats_print()
    slow_print('\nTietokoneesi näyttö tulee näkyviin. Näet "värikkään" taustakuvasi.')
    slow_print("A: Avaa Chrome")
    slow_print("B: Sammuta tietokone")
    while True:
        computer_choice = input("\n>> ").lower()

        if computer_choice == "a":
            slow_print("\nSovellus avautuu...")
            time.sleep(2)
            break
        elif computer_choice == "b":
            slow_print("\nSammutat tietokoneen...")
            time.sleep(2)
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

    return computer_choice 

# Avasit Chromen
def app_chrome():
    clear_screen()
    stats_print()
    slow_print("\nNettiselain käynnistyi. Näet edessäsi hakupalkin.")
    slow_print("A: Katso kirjanmerkkisi")
    slow_print("B: Mene incognito tilaan")
    slow_print("C: Poistu Chromesta")
    while True:
        chrome_choice = input("\n>> ").lower()
        if chrome_choice == "a":
            slow_print("\nKirjanmerkkinäkymä avautuu...")
            time.sleep(2)
            break
        elif chrome_choice == "b":
            break
        elif chrome_choice == "c":
            slow_print("\nSuljet sovelluksen...")
            time.sleep(2)
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")

    return chrome_choice

# Derbin osien valinta
def derbi_osat():
    global money, style, speed, derbilaatu
    clear_screen()
    stats_print()
    slow_print("\nNäet takapihallasi olevan derbin, mutta siitä puuttuu osia!")
    slow_print("A: Etsit osia kotoa.")
    slow_print("B: Ostat uusia osia kaupasta. (5 rahaa)")
    slow_print("C: Korjaat purukumilla.")
    slow_print("D: Ostat Alibabasta. (2 rahaa)")
    
    while True:
        osat_choice = input("\n>> ").lower()
        
        if osat_choice == "a":
            slow_print("\nLöysit kotoa hieman varaosia!")
            time.sleep(2)
            derbilaatu =+ 1
            break
        elif osat_choice == "b" and money > 4:
            slow_print("\nLöysit kaupasta hyvänlaatuisia osia! Nopeutta niissä ei kuitenkaan ole mielinmäärin.")
            time.sleep(2)
            money -= 5
            speed += 1
            derbilaatu += 3
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
        elif osat_choice == "d" and money > 1:
            slow_print('\n"Osta halvalla, säästä mahdollisesti myös laadusta."')
            time.sleep(2)
            money -= 2
            derbilaatu += random.randint(-1, 2)
            speed += random.randint(-1, 2)
            break
        elif osat_choice == "d" and money < 2:
            slow_print("\nSinulla ei ole tarpeeksi rahaa.")
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
            slow_print("\nKatsot ympärillesi jännittyneenä. Toivot, että kukaan ei nähnyt virittelyjäsi...")
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
    slow_print("C: Kyllä, ja kaiuttimet kaiken varaksi että kukaan ei saa unta! (2 rahaa)")
    
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
