# Tuo tarvittavat moduulit
import time, random, os
from gameResources import license_table # VSCodelle: #type: ignore

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
    text_border = "+" + "=" * 84 + "+"
    while True:
        clear_screen()
        print(f"\n{text_border}\n| Jos rakennat itsellesi 88br derbin ja kohdistat keulan suoraan keulakulmille peli. |\n{text_border}")
        print("\n1. Aloita uusi peli\n2. Lue lisenssitiedot\n\nSyötä numero: ")
        aloitusValinta = input(">> ")
        if aloitusValinta == "1":
            break
        elif aloitusValinta == "2":
            clear_screen()
            print(license_table.smaller())
        lisenssiValinta = input(">> ")
        if lisenssiValinta.lower() == "l":
            clear_screen()
            print(license_table.full())
            input("\nPaina ENTER jatkaaksesi. Press ENTER to continue. ")

# Aseta muuttujien arvo
def setup():
    global money, style, speed, derbilaatu, poliisi
    money = 10
    style = 0
    speed = 0
    derbilaatu = 0
    poliisi = 0

# Tulosta pelaajan edistyminen
def stats_print():
    global money, derbilaatu, style, speed
    fmoney, fderbilaatu, fstyle, fspeed = f"Raha: {money}", f"Derbin laatu: {derbilaatu}", f"Tyylipisteet: {style}", f"Nopeus: {speed}"
    highest = max(len(fmoney), len(fderbilaatu), len(fstyle), len(fspeed))
    border = "=" * highest
    print(f"\n{border}\n{fmoney}\n{fderbilaatu}\n{fstyle}\n{fspeed}\n{border}")

# Derbin osien valinta
def derbi_osat():
    global money, style, speed, derbilaatu
    clear_screen()
    stats_print()
    slow_print("\nAloit rakentamaan derbiä, mutta sinulta puuttuu osia!")
    slow_print("Mitä teet?")
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
        elif osat_choice == "b":
            slow_print("\nLöysit kaupasta hyvänlaatuisia osia! Nopeutta niissä ei kuitenkaan ole mielinmäärin.")
            time.sleep(2)
            money -= 5
            speed += 1
            derbilaatu += 3
            break
        elif osat_choice == "c":
            slow_print("\nMitä odotit tapahtuvan?")
            time.sleep(2)
            speed -= -1
            style -= 2
            derbilaatu -= -1
            break
        elif osat_choice == "d":
            slow_print('\n"Osta halvalla, säästä mahdollisesti myös laadusta."')
            time.sleep(2)
            money -= 2
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
            slow_print("Ei kaikki uskalla!")
            break
        elif viritys_choice == "b":
            slow_print("\nNyt on virit!")
            time.sleep(2)
            money -= 2
            speed += 1
            derbilaatu += 1
            poliisi += 1
            break
        elif viritys_choice == "c":
            slow_print("\nKatsot ympärillesi jännittyneenä. Toivot, että kukaan ei nähnyt virittelyjäsi...")
            time.sleep(2)
            speed += 4
            style += 2
            derbilaatu += 2
            money -= 4
            poliisi += 2
            break
        else:
            slow_print("\nTuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.")
