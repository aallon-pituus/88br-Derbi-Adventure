# Mitä lisätä seuraavaksi:
# 1. Pelintallennussysteemi
# 2. Lisää pelattavaa

import time
import random

# Hidas tulostusfunktio

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Peli alkaa

peliAloitettu = False
while peliAloitettu == False:
    slow_print("\nJos rakennat itsellesi 88br derbin ja kohdistat keulan suoraan keulakulmille peli.", 0.05)
    slow_print("1. Aloita uusi peli\n2. Lue lisenssitiedot\n\nSyötä numero: ", 0.05)
    aloitusValinta = input()
    if aloitusValinta == "1":
        peliAloitettu = True
    elif aloitusValinta == "2":
        print("""
88br-Derbi-Adventure --- A game referencing our insider joke.
Copyright (C) 2025  aallon-pituus

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
              
The full license is in the LICENSE file.
Koko lisenssi on LICENSE tiedostossa.
If you do not have the LICENSE file, get it from https://github.com/aallon-pituus/88br-Derbi-Adventure/blob/main/Licenses%26Copyright/LICENSE.
Jos sinulla ei ole LICENSE tiedostoa, hanki se osoitteesta https://github.com/aallon-pituus/88br-Derbi-Adventure/blob/main/Licenses%26Copyright/LICENSE.
              """)
        input("Paina ENTER jatkaaksesi.")

### Aloitusmuuttuja-arvot

# HP
hp = 12

# Stamina
stamina = 20

# Raha
money = 10

# Tyyli (pari eventtiä, score)
style = 0

# Laatu (monta eventtiä, score)
derbilaatu = 0

# Nopeus (monta eventtiä, score)
speed = 0

# Wanted level (poliisit)
poliisi = 0

# Erityinen esine
tinalasit = 0

# Erityinen esine
tcube = 0

breaker = 0

dmod = 0
atmod = 0
hitmod = 0
damage = 0
shieldbreak = 0
dodge = 0
breaker2 = 0

tinaGamesActive = True

# Tulosta tilastot

def printStats():
    show1 = f"Raha: {money}"

    lenght = len(show1) # Käytin erillistä muuttujaa, jotta tulevaisuudessa on helpompi päivittää printStats() funktiota.

    border = "=" * lenght

    print(f"\n{border}\n{show1}\n{border}\n")

def tinagamesvictory():
    global tcube, money

    while True:
        global tinaGamesActive
        slow_print("Voit valita yhden palkinnon...", 0.05)
        slow_print("A: Tinakuutio", 0.05)
        slow_print("B: Rahallinen palkinto", 0.05)
        tg_choice = input("\n")

        if tg_choice.capitalize() == "A":
            tcube = 1
            tinaGamesActive = False
            break
        elif tg_choice.capitalize() == "B":
            slow_print("[Mietit itseksesi] Onpa se köyhä, kun se ei voi antaa enempää kuin 111...", 0.05)
            money = 111
            tinaGamesActive = False
            break
        else:
            slow_print("Yritä uudelleen.", 0.05)

def tinagameschallenge():
    while tinaGamesActive == True:
        slow_print("[Ääni kaiuttimista] Tervetuloa Tina Gamesiin. Ensimmäinen haasteenne on väistellä luoteja.", 0.05)
        slow_print("Vieressäsi on portaat.", 0.05)
        slow_print("A: Kokeile väistellä luoteja.", 0.05)
        slow_print("B: Juokse portaat ylös.", 0.05)
        tg_choice = input("\n")

        if tg_choice.capitalize() == "A":
            slow_print("Olipa tyhmä idea. Kuolit.", 0.05)
        elif tg_choice.capitalize() == "B":
            slow_print("Portaat suojasivat sinua luodeilta", 0.05)
            slow_print("Olet ainoa selviytyjä...", 0.05)
            tinagamesvictory()

def tinagameswin():
    while True:           
        slow_print("Päihitit molemmat pelaajat taisteluusa. Tina Gamesin johtaja on yllättynyt ja kutsui sinut yksityiskeskusteluun.", 0.05)
        slow_print("Hyväksytkö pyynnon?", 0.05)
        slow_print("Y: Hyväksyn", 0.05)
        slow_print("N: En hyväksy", 0.05)
        tg_choice = input("\n")

        if tg_choice.capitalize() == "Y":
            global style
            slow_print("[Tina Gamesin johtaja] Hei siellä... Minulla on sinulle jotain spesiaalia...", 0.05)
            slow_print("Sait fluffy hairin.", 0.05)
            style += 111
            break
        elif tg_choice.capitalize() == "N":
            tinagameschallenge()

def tinagamesfight():
    while tinaGamesActive == True:
        slow_print("Huomaat vierelläsi tapahtuvan taistelun kahden pelaajan välillä.", 0.05)
        slow_print("A: Osallistu taisteluun.", 0.05)
        slow_print("B: Liiku muualle.", 0.05)

        tg_choice = input("\n")

        if tg_choice.capitalize() == "A":
                    winChance = random.randint(1, 2)
                    if winChance == 1:
                        tinagameswin()
                    else:
                        slow_print("Kuolit taistelussa.", 0.05)
                        input()
                        exit()
        elif tg_choice.capitalize() == "B":
            tinagameschallenge()
        else: 
            slow_print("Yritä uudelleen.", 0.05)

def tinagames():
    # Määrittely
    playerNumber = random.randint(1, 456)

    while tinaGamesActive == True:

        printStats()
        slow_print("Osallistuit Tina Gamesiin.", 0.05)
        slow_print(f"Pelaajanumerosi on {playerNumber}\n", 0.05)
        slow_print("Heräät kerrossängyssä...", 0.05)
        slow_print("A: Poistu sängystä.", 0.05)
        slow_print("B: Jää nukkumaan.", 0.05)
        tg_choice = input("\n")

        if tg_choice.capitalize() == "A":
            tinagamesfight()
        elif tg_choice.capitalize() == "B":
            slow_print("Voi ei! Päällesi putosi 1000kg painava osa kattoa.", 0.05)
            input()
            exit()
        else:
            slow_print("Yritä uudelleen.", 0.05)
    


def poliisit():
    global poliisi_run_roll, style
    printStats()
    slow_print("Poliisi setä lähestyy sinua!", 0.05)
    slow_print("A: Aja pakoon", 0.05)
    slow_print("B: Anna poliisille turpiin!", 0.05)
    
    while True:
        
        poliisi_choice = input().lower()
        
        if poliisi_choice == "a":
            poliisi_run_roll = (random.randint(0,10)) + speed
            if poliisi_run_roll > 8:
                slow_print("Pääsit pakoon!", 0.05)
                style += 1
                break
            
            elif poliisi_run_roll < 7:
                slow_print("Jäit kiinni!", 0.05)
                input()
                exit()
            
        elif poliisi_choice == "b":
            slow_print("Poliisi lamaannutti sinut taserilla!", 0.05)
            slow_print("Hävisit pelin!", 0.05)
            input()
            exit()
            
        else:
            slow_print("Tuo ei ole yksi vaihtoehdoista", 0.05)

def event_trigger():
    global money, poliisi, polroll, style, speed, derbilaatu, random_event, roadman_choice
    if poliisi > 0:
        polroll = (random.randint(0,12)) + poliisi
        if polroll > 10:
            poliisit()
            
    elif poliisi < 1:
        random_event = (random.randint(0,4))
        if random_event == 1:
            printStats()
            slow_print("Sinua lähestyy epäilyttävä katumyyjä!", 0.05)
            slow_print("A: Uhkapelaa kaikki rahasi.", 0.05)
            slow_print("B: Osta epäilyttävää ainetta (2 rahaa).", 0.05)
            slow_print("C: Osta epäilyttävä ruisku (5 rahaa).", 0.05)
            slow_print("D: Osta tinalasit (8 rahaa).", 0.05)
            
            while True:
                
                dealer_choice = input().lower()
                
                if dealer_choice == "a" and money > 0:
                    gamble = random.randint(1, 100)
                    if gamble <= 30:  # 30% voittaa
                        money *= 2
                        slow_print(f"Voitit! Nyt sinulla on {money} rahaa.", 0.05)
                    else:
                        money = 0
                        slow_print("Hävisit kaikki rahasi!", 0.05)
                    break
                elif dealer_choice == "b" and money >= 2:
                    powder_effect = random.randint(-2, 2)
                    speed += powder_effect
                    slow_print(f"Tuntuu oudolta...", 0.05)
                    money -= 2
                    break
                elif dealer_choice == "c" and money >= 5:
                    syringe_effect = random.randint(1, 100)
                    if syringe_effect <= 45:  # 45% kuolla
                        slow_print("Älkää käyttäkö huumeita! Kuolit!", 0.05)
                        exit()
                    else:
                        speed += 4
                        slow_print("Energiaa pumppaa valtavasti!", 0.05)
                        money -= 5
                    break
                elif dealer_choice == "d" and money >= 8:
                    global tinalasit
                    tinalasit = 1
                    money -= 8
                    break
                else:
                    slow_print("Sinulla ei ole tarpeeksi rahaa tai valitsit jonkun muun kirjaimen/symbolin kuin A, B, C ja D. Yritä uudelleen.", 0.05)
        
        elif random_event == 2:
            printStats()
            slow_print("Sinua lähestyy roadman!", 0.05)
            slow_print("Roadman vetää taskustaan puukon!", 0.05)
            slow_print("Mitä teet?", 0.05)
            slow_print("A: Juokset pakoon.", 0.05)
            slow_print("B: Hakkaa roadman.", 0.05)
            slow_print("C: Uskottele, että sinua ei kannata ryöstää, koska sinulla on liian hyvä drip.", 0.05)
            
            while True:
                
                roadman_choice = input().lower()
                    
                if roadman_choice == "b":
                    slow_print("Sinut tapettiin!", 0.05)
                    slow_print("Hävisit pelin!", 0.05)
                    input()
                    exit()
                    
                elif roadman_choice == "a":
                    roadman_roll = (random.randint(0,2))
                    if roadman_roll > 1:
                        slow_print("Pääsit pakoon!", 0.05)
                        break
                elif roadman_roll < 2:
                    slow_print("Jäit kiinni!", 0.05)
                    slow_print("Hävisit pelin!", 0.05)
                    input()
                    exit()
                elif roadman_choice == "c":
                    if style > 1:
                        slow_print("Roadman huomaa eeppisen tyylisi!", 0.05)
                        slow_print("Hän päästää sinut pakoon!", 0.05)
                        style += 2
                        break
                    elif style < 2:
                        slow_print("Roadman ei pidä sun dripistä.", 0.05)
                        slow_print("Hän puukottaa sinut! Hävisit pelin!", 0.05)
                        input()
                        exit()
        
        elif random_event == 3:
            
            speed += 1
        
        elif random_event == 4 and derbilaatu < 5:
            slow_print("Derbisi hajosi!", 0.05)
            slow_print("Korjaamisessa kului aikaa ja derbin laatu on hieman huonontunut.", 0.05)
            derbilaatu -= 1
            speed -= 3 

def shop():
    global money, style, speed, derbilaatu, tinalasit, tcube
    
    
    if tinalasit == 1:
        printStats()
        slow_print("Sisällä R-kioskissa ei ole juuri mitään, paitsi vanha nainen.", 0.05)
        slow_print("Vanha nainen myy sinulle jotain erikoista.", 0.05)
        slow_print("A: Osta tinakuutio (5 rahaa).", 0.05)
        slow_print("B: Poistu kaupasta.", 0.05)
        
        while True:
            shop_choice = input().lower()
            
            if shop_choice == "a" and money >= 5:
                money -= 5
                tcube = 1  
                slow_print("Ostit tinakuution. Se vaikuttaa tärkeältä...", 0.05)
                break
            elif shop_choice == "a" and money < 5:
                slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
            elif shop_choice == "b":
                break
            else:
                slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)
        
    else:
        printStats()
        slow_print("Tervetuloa R-kioskille!", 0.05)
        slow_print("Mitä haluaisit ostaa?", 0.05)
        slow_print("A: Megaforce (2 rahaa)", 0.05)
        slow_print("B: Megaforce 6-pack (10 rahaa)", 0.05)
        slow_print("C: Prime (6 rahaa)", 0.05)
        slow_print("D: Sipsit (3 rahaa)", 0.05)
        slow_print("E: Ei mitään", 0.05)
        
        while True:
            shop_choice = input().lower()
            
            if shop_choice == "a" and money >= 2:
                money -= 2
                speed += 1
                slow_print("Ostit megiksen.", 0.05)
                break
            elif shop_choice == "b" and money >= 10:
                money -= 10
                speed += 6
                slow_print("Nyttt tuleee pärinät!!!!!!", 0.05)
                break
            elif shop_choice == "c" and money >= 6:
                money -= 6
                slow_print("Kuolit välittömästi.", 0.05)
                input()
                exit()
            elif shop_choice == "d" and money >= 3:
                money -= 3
                style += 1
                slow_print("Ostit sipsit.", 0.05)
                break
            elif shop_choice == "a" and money < 2:
                slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
            elif shop_choice == "b" and money < 10:
                slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
            elif shop_choice == "c" and money < 6:
                slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
            elif shop_choice == "d" and money < 3:
                slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
            elif shop_choice == "e":
                break
                    
            else:
                slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)
    
    ending()

def ending():
    global style, speed, derbilaatu, tcube
    
    
    score = style + speed + derbilaatu
    slow_print(f"Pelisi on päättynyt. Drip: {style}, Nopeus: {speed}, Derbi: {derbilaatu}", 0.05)
    
    if tcube == 1:
        slow_print("Tina ei johda sähköä.", 0.05)
    
    slow_print(f"Pisteesi: {score}", 0.05)
    input()  
    exit()

# Osat
def osat():
    global money, style, speed, derbilaatu
    printStats()
    slow_print("Aloit rakentamaan derbiä, mutta sinulta puuttuu osia!", 0.05)
    slow_print("Mitä teet?", 0.05)
    slow_print("A: Etsit osia kotoa.", 0.05)
    slow_print("B: Ostat uusia osia kaupasta. (5 rahaa)", 0.05)
    slow_print("C: Korjaat purukumilla.", 0.05)
    slow_print("D: Ostat Alibabasta. (2 rahaa)", 0.05)
    
    while True:
        osat_choice = input().lower()
        
        if osat_choice == "a":
            break
        elif osat_choice == "b":
            money -= 5
            speed += 1
            derbilaatu += 3
            break
        elif osat_choice == "c":
            speed -= 2
            style -= 2
            derbilaatu -= 2
            break
        elif osat_choice == "d":
            money -= 2
            derbilaatu += random.randint(-3, 2)
            speed += random.randint(-2, 2)
            break
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

osat()

# Viritys
def viritys():
    global money, style, derbilaatu, speed, poliisi
    printStats()
    slow_print("Pitäisikö nyt virittää mopoa...", 0.05)
    slow_print("A: No ei todellakaan!", 0.05)
    slow_print("B: Hiukan vääntöä ja kääntöä, laillisesti. (2 rahaa)", 0.05)
    slow_print("C: Täydet virit päälle! Ei ne poliisit saa mua kiinni. (4 rahaa)", 0.05)
    
    while True:
        viritys_choice = input().lower()
        
        if viritys_choice == "a":
            break
        elif viritys_choice == "b":
            money -= 2
            speed += 1
            break
        elif viritys_choice == "c":
            speed += 4
            style += 2
            derbilaatu -= 1
            money -= 4
            poliisi += 2
            break
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

viritys()

# Pärinät
def ääni():
    global money, style, derbilaatu, speed, poliisi
    printStats()
    slow_print("Laitetaanko päristely päälle?", 0.05)
    slow_print("A: Turhaa semmoinen.", 0.05)
    slow_print("B: Äänenvaimennin irti ja pärinä kuuluu.", 0.05)
    slow_print("C: Kyllä, ja kaiuttimet kaiken varaksi että kukaan ei saa unta! (2 rahaa)", 0.05)
    
    while True:
        ääni_choice = input().lower()
        
        if ääni_choice == "a":
            break
        elif ääni_choice == "b":
            style += 1
            break
        elif ääni_choice == "c" and money > 1:
            poliisi += 1
            style += 3
            money -= 2
            break
        elif ääni_choice == "c" and money < 2:
            slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

ääni()

# Köyhille pojille
def rahapula():
    global money, style, speed, derbilaatu, poliisi
    slow_print("Voi ei! Olet köyhempi kuin tehdastyöläinen!", 0.05)
    slow_print("A: Aika mennä kerjäämään kadulle.", 0.05)
    slow_print("B: Yritä vetää rahat viereisen ohikulkijan taskusta hiljaa.", 0.05)
    slow_print("C: Rahaa on ihan tarpeeksi.", 0.05)
    slow_print("D: Ryöstä viereisesi ohikulkija.", 0.05)
    slow_print("E: Pölli vanhempien pankkitiedot.", 0.05)
    slow_print("F: Osallistu Tina Gamesiin.", 0.05)
    
    while True:
        raha_choice = input().lower()
        
        if breaker == 1:
            event_trigger()
            event_trigger()
            shop()
            event_trigger()
            ending()
        
        elif raha_choice == "a":
            speed -= 1
            money += 1
            style -= 1
            slow_print("Onnistuit keräämään yhden rahan.", 0.05)
            break
        elif raha_choice == "b":
            raha_chance = random.randint(0, 100)
            if raha_chance > 50:
                taskuvaras_k()
                break
            if raha_chance <= 50:
                money += 4
                slow_print("Sinä onnistuit! Sait 4 rahaa.", 0.05)
                break
        elif raha_choice == "c":
            break
        elif raha_choice == "d":
            taskuvaras_k()
            
        elif raha_choice == "e":
            rahaonnistuminen = (random.randint(0,10))
            if rahaonnistuminen > 8:
                slow_print("Onnistuit!!! et jäänyt kiinni!", 0.05)
                slow_print("Sait 15 rahaa!", 0.05)
                money += 15
            elif rahaonnistuminen < 9:
                slow_print("Jäit kiinni, hävisit pelin!", 0.05)
                input()
                exit()
                break
        elif raha_choice == "f":
            tinagames()
            break
        
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

# Taskuvaras
def taskuvaras_k():
    global money, poliisi, style
    slow_print("Jäit kiinni! Mitä teet nyt?", 0.05)
    slow_print("A: Juokse", 0.05)
    slow_print("B: Kaksintaistelu!", 0.05)
    
    while True:
        fight_choice = input().lower()
        
        if fight_choice == "a":
            slow_print("Ohikulkija soittaa poliisit!", 0.05)
            break
        elif fight_choice == "b":
            slow_print("Tietoosi tulee, että ohikulkija ei arvosta keulakulmia.", 0.05)
            fighthater()
            break
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)
            
def fighthater():
    global hp, stamina, money, poliisi, style, dmod, atmod, hitmod, hitroll, hit, shieldbreak, damage, dmgroll, haterai, hater_hp, hater_sta, dodge, woda, wohit, wdodge, breaker2
    slow_print("--------Fight!!!--------", 0.1)
    slow_print("-You-      -Hater-", 0.05)
    slow_print("HP 12       HP 10", 0.05)
    slow_print("STA 20      STA 18", 0.05)

    hater_hp = 10
    hater_sta = 15

    while True:

        wohit = 0
        woda = 0
        wostagger = 0
        stagger = 0

        slow_print("Mitä teet?", 0.05)
        slow_print("1. Kick", 0.05)
        slow_print("2. Heavy punch", 0.05)
        slow_print("3. Punch", 0.05)
        slow_print("4. Block", 0.05)
        slow_print("5. Dodge", 0.05)

        while True:

            while True:

                attackoption = input().lower()

                if attackoption == "1" and stamina > 3:
                    stamina -= 3
                    hitroll = (random.randint(0, 12))
                    hit = hitroll + hitmod
                    dmgroll = (random.randint(0, 5))
                    damage = dmgroll + dmod
                    shieldbreak = 2
                    break

                elif attackoption == "2" and stamina > 5:
                    stamina -= 5
                    hitroll = (random.randint(0, 12))
                    hit = hitroll + hitmod - 2
                    dmgroll = (random.randint(0, 7))
                    damage = dmgroll + dmod
                    break

                elif attackoption == "3" and stamina > 2:
                    stamina -= 2
                    hitroll = (random.randint(0, 12))
                    hit = hitroll + hitmod + 1
                    dmgroll = (random.randint(0, 5))
                    damage = dmgroll + dmod
                    break

                elif attackoption == "4":
                    stamina += 1
                    break

                elif attackoption == "5" and stamina > 2:
                    stamina -= 2
                    dmod = 5
                    break

                else:
                    slow_print("Tuo ei ollut yksi vaihtoehdoista tai sinulla ei ole tarpeeksi staminaa. Yritä uudelleen.", 0.05)

            haterai = (random.randint(0, 4))

            # 1 = light bag attack 2 = heavy bag attack 3 = frantic block 4 = mace

            if haterai == 1:
                hater_sta -= 2
                wohit = (random.randint(0, 12))
                woda = (random.randint(0, 4))

            elif haterai == 2:
                hater_sta -= 4
                wohit = (random.randint(0, 12)) - 2
                woda = (random.randint(0, 6))

            if haterai == 1 or 2 and attackoption == "1" or "2" or "3":
                if hitroll > wohit:
                    wdodge = (random.randint(0, 10))
                    if wdodge < 9:
                        hit_success()
                    elif wdodge > 8:
                        slow_print("Molemmat löi, mutta kumpikaan ei osunut!", 0.05)

                elif wohit > hitroll:
                    dodge = (random.randint(0, 10)) + dmod
                    if dodge < 9:
                        gothit()
                    elif dodge > 8:
                        slow_print("Molemmat löi, mutta kumpikaan ei osunut!", 0.05)

            elif haterai == 1 or 2 and attackoption == "4":
                if wohit > 7:
                    gothit()
                else:
                    hater_sta -= 5
                    if hater_sta < 1:
                        hater_sta = 5
                        slow_print("Keulakulma-vihaajan stamina loppui!", 0.05)
                        slow_print("Saat iskeä uudelleen!", 0.05)
                        stadodw = (random.randint(0, 10))
                        if stadodw > 8:
                            slow_print("Et osunut!", 0.05)
                        elif stadodw < 9:
                            slow_print("Osuit!", 0.05)
                            stahit = (random.randint(0, 4))
                            slow_print("Keulakulma-vihaaja menetti" + str(stahit) + " hp!", 0.05)
                            hater_hp -= stahit
                        if hater_hp < 1:
                            slow_print("Keulakulma-vihaaja kuoli, voitit taistelun!!!", 0.05)
                            loot()

            elif haterai == 1 or 2 and attackoption == "5":
                dodge = (random.randint(0, 10)) + dmod
                if dodge < 9:
                    gothit()
                elif dodge > 8:
                    slow_print("Keulakulma-vihaaja ei osunut!", 0.05)

            elif haterai == 3 and attackoption == "1" or "2" or "3":
                if hit + shieldbreak > 7:
                    slow_print("Sinä iskit torjunnan läpi!", 0.05)
                else:
                    stamina -= 5
                    if stamina < 1:
                        stamina = 5
                        slow_print("Sinulta loppui stamina!", 0.05)
                        slow_print("Keulakulma-vihaaja lyö uudelleen!", 0.05)
                        stadod = random.randint(0, 10)
                        if stadod > 8:
                            slow_print("Keulakulma-vihaaja ei osunut!", 0.05)
                        elif stadod < 9:
                            slow_print("Sinuun osui!", 0.05)
                            stahitw = (random.randint(0, 4))
                            slow_print("Menetit " + str(stahitw) + " hp!", 0.05)
                            if hp < 1:
                                slow_print("Kuolit!!!", 0.05)
                                input()
                                exit()

            elif haterai == 3 and attackoption == "4":

                slow_print("Molemmat puolustaa itseään... mitään ei tapahdu!", 0.05)

            elif haterai == 3 and attackoption == "5":

                slow_print("Keulakulma-vihaaja puolustaa itseään... Mitään ei tapahdu!", 0.05)

            elif haterai == 4 and attackoption == "1" or "2" or "3":

                wdodge = (random.randint(0, 10))
                if wdodge < 9:
                    hit_success()
                elif wdodge > 8:
                    getmaced()

            elif haterai == 4 and attackoption == "4":

                getmaced()

            elif haterai == 4 and attackoption == "5":

                getmaced()
            
            print("sinulla on "+str(hp)+" hp:tä!")
            print("sinulla on "+str(stamina)+" staminaa!")
            
            if breaker == 1:
                break
        if breaker == 1:
            break
               
def hit_success():
    global hater_sta, hater_hp, stadodw, stahit
    slow_print("Osuit!", 0.05)
    slow_print("Keulakulma-vihaaja menetti " + str(damage) + " hp!", 0.05)
    slow_print("Keulakulma-vihaaja menetti " + str(damage) + " staminaa!", 0.05)
    hater_hp -= damage
    hater_sta -= damage
    dmod
    atmod
    hitmod = 0
    if hater_sta < 1:
        hater_sta = 5
        slow_print("Keulakulma-vihaajalta loppui stamina!", 0.05)
        slow_print("Saat lyödä uudelleen!", 0.05)
        stadodw = (random.randint(0, 10))
        if stadodw > 8:
            slow_print("Et osunut.", 0.05)
        elif stadodw < 9:
            slow_print("Sinä osuit!", 0.05)
            stahit = (random.randint(0, 4))
            slow_print("Keulakulma-vihaaja menetti " + str(stahit) + " hp!", 0.05)
            hater_hp -= stahit
    if hater_hp < 1:
        slow_print("Se kuoli VIHDOINKIN!!!!", 0.05)
        loot()

def gothit():
    global hp, stamina, stadod, stahitw, dmod, atmod, hitmod
    slow_print("Sinuun osui!", 0.05)
    slow_print("Sinä menetit " + str(woda) + " hp!", 0.05)
    hp -= woda
    stamina -= woda
    dmod = 0
    atmod = 0
    hitmod = 0
    if stamina < 1:
        stamina = 5
        slow_print("Sinulta loppui stamina!", 0.05)
        slow_print("Keulakulma-vihaaja lyö uudestaan!", 0.05)
        stadod = random.randint(0, 10)
        if stadod > 8:
            slow_print("Keulakulma-vihaaja ei osunut!", 0.05)
        elif stadod < 9:
            slow_print("Sinuun osui!", 0.05)
            stahitw = (random.randint(0, 4))
            slow_print("Menetit " + str(stahitw) + " hp!", 0.05)
    if hp < 1:
        slow_print("Kuolit!!!", 0.05)
        input()
        exit()

def getmaced():
    global poliisi, breaker
    slow_print("Keulakulma-vihaaja suihkutti sinua mace:lla!", 0.05)
    slow_print("Keulakulma-vihaaja soitti poliisit!", 0.05)
    slow_print("Keulakulma-vihaaja juoksi pakoon!")
    poliisi += 5
    breaker = 1

def loot():
    global breaker, money
    slow_print("Sait 8 rahaa!")
    money += 8
    breaker = 1

if money < 3: rahapula()

event_trigger()
event_trigger()
shop()
event_trigger()
ending()
