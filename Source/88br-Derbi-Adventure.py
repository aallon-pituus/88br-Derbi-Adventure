import time
import random

# Hidas tulostusfunktio

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Peli alkaa

slow_print("Jos rakennat itsellesi 88br derbin ja kohdistat keulan suoraan keulakulmille peli.", 0.05)
slow_print("Paina enter aloittaaksesi.", 0.05)
input()

# Aloitus statsit

# HP
hp = 12

# Stamina
sta = 20

# Raha
mon = 10

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

def poliisit():
    global poliisi_run_roll, style
    slow_print("Poliisi setä lähestyy sinua!", 0.05)
    slow_print("A: aja pakoon", 0.05)
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
            slow_print("Poliisi sähköitti sinut!", 0.05)
            slow_print("Hävisit pelin!", 0.05)
            input()
            exit()
            
        else:
            slow_print("Tuo ei ole yksi vaihtoehdoista", 0.05)

def event_trigger():
    global mon, poliisi, polroll, style, speed, derbilaatu, random_event, roadman_choice
    if poliisi > 0:
        polroll = (random.randint(0,12)) + poliisi
        if polroll > 10:
            poliisit()
            
    elif poliisi < 1:
        random_event = (random.randint(0,4))
        if random_event == 1:
            
            slow_print("sinua lähestyy epäilyttävä diileri!", 0.05)
            slow_print("A: Uhkapelaa kaikki rahasi.", 0.05)
            slow_print("B: Osta epäilyttävää jauhetta (2 rahaa).", 0.05)
            slow_print("C: Osta epäilyttävä ruisku (5 rahaa).", 0.05)
            slow_print("D: Osta tinalasit (8 rahaa).", 0.05)
            
            while True:
                
                dealer_choice = input().lower()
                
                if dealer_choice == "a" and mon > 0:
                    gamble = random.randint(1, 100)
                    if gamble <= 30:  # 30% voittaa
                        mon *= 2
                        slow_print(f"Voitit! Nyt sinulla on {mon} rahaa.", 0.05)
                    else:
                        mon = 0
                        slow_print("Hävisit kaikki rahasi!", 0.05)
                    break
                elif dealer_choice == "b" and mon >= 2:
                    powder_effect = random.randint(-2, 2)
                    speed += powder_effect
                    slow_print(f"Tuntuu oudolta...", 0.05)
                    mon -= 2
                    break
                elif dealer_choice == "c" and mon >= 5:
                    syringe_effect = random.randint(1, 100)
                    if syringe_effect <= 45:  # 45% kuolla
                        slow_print("Älkää käyttäkö huumeita! Kuolit!", 0.05)
                        exit()
                    else:
                        speed += 4
                        slow_print("Energiaa pumppaa valtavasti!", 0.05)
                        mon -= 5
                    break
                elif dealer_choice == "d" and mon >= 8:
                    global tinalasit
                    tinalasit = 1
                    mon -= 8
                    break
                else:
                    slow_print("Sinulla ei ole tarpeeksi rahaa tai valinta ei ole validi. Yritä uudelleen.", 0.05)
        
        elif random_event == 2:
            
            slow_print("sinua lähestyy Roadman!", 0.05)
            slow_print("Roadman vetää taskustaan puukon!", 0.05)
            slow_print("Mitä teet?", 0.05)
            slow_print("A: Juokset pakoon.", 0.05)
            slow_print("B: Hakkaa roadman", 0.05)
            slow_print("C: uskottele että sinua ei kannata ryöstää koska sinulla on liian hyvä drip", 0.05)
            
            while True:
                
                roadman_choice = input().lower()
                    
                if roadman_choice == "b":
                    slow_print("Sinut puukotettiin kuoliaaksi!", 0.05)
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
                        slow_print("Roadman ei pidä sun dripistä", 0.05)
                        slow_print("Hän puukottaa sinut! Hävisit pelin!", 0.05)
                        input()
                        exit()
        
        elif random_event == 3:
            
            speed +=1
        
        elif random_event == 4 and derbilaatu < 5:
            slow_print("Derbisi hajosi!", 0.05)
            slow_print("Korjaamisessa kului aikaa ja derbin laatu on hieman huonontunut.", 0.05)
            derbilaatu -= 1
            speed -= 3 

def shop():
    global mon, style, speed, derbilaatu, tinalasit, tcube
    
    
    if tinalasit == 1:
        slow_print("Sisällä R-kioskissa ei ole juuri mitään, paitsi vanha nainen.", 0.05)
        slow_print("Vanha nainen myy sinulle jotain erikoista.", 0.05)
        slow_print("A: Osta tinakuutio (5 rahaa).", 0.05)
        
        while True:
            shop_choice = input().lower()
            
            if shop_choice == "a" and mon >= 5:
                mon -= 5
                tcube = 1  
                slow_print("Ostit tinakuution. Se vaikuttaa tärkeältä...", 0.05)
                break
            elif shop_choice == "a" and mon < 5:
                slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
            else:
                slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)
        
    else:
        
        slow_print("Tervetuloa R-kioskille!", 0.05)
        slow_print("Mitä haluaisit ostaa?", 0.05)
        slow_print("A: Megaforce (2 rahaa)", 0.05)
        slow_print("B: Megaforce 6-pack (10 rahaa)", 0.05)
        slow_print("C: Prime (6 rahaa)", 0.05)
        slow_print("D: Sipsit (3 rahaa)", 0.05)
        slow_print("E: nothing", 0.05)
        
        while True:
            shop_choice = input().lower()
            
            if shop_choice == "a" and mon >= 2:
                mon -= 2
                speed += 1
                slow_print("Ostit megiksen.", 0.05)
                break
            elif shop_choice == "b" and mon >= 10:
                mon -= 10
                speed += 6
                slow_print("Nyttt tuleee pärinät!!!!!!", 0.05)
                break
            elif shop_choice == "c" and mon >= 6:
                mon -= 6
                slow_print("Kuolit välittömästi", 0.05)
                input()
                exit()
            elif shop_choice == "d" and mon >= 3:
                mon -= 3
                style += 1
                slow_print("Ostit sipsit", 0.05)
                break
            elif shop_choice == "a" and mon < 2:
                slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
            elif shop_choice == "b" and mon < 10:
                slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
            elif shop_choice == "c" and mon < 6:
                slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
            elif shop_choice == "d" and mon < 3:
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
    
    slow_print(f"score: {score}", 0.05)
    input()  
    exit()

slow_print("Sinulla on 10 rahaa.", 0.05)

# Osat
def osat():
    global mon
    global style
    global speed
    global derbilaatu
    slow_print("Aloit rakentamaan derbiä, mutta sinulta puuttuu osia!", 0.05)
    slow_print("Mitä teet?", 0.05)
    slow_print("A: Kompromisoit osia kotoa.", 0.05)
    slow_print("B: Ostat uusia osia kaupasta. (5 rahaa)", 0.05)
    slow_print("C: Korjaat purukumilla.", 0.05)
    slow_print("D: Ostat alibabasta. (2 rahaa)", 0.05)
    
    while True:
        osat_choice = input().lower()
        
        if osat_choice == "a":
            break
        elif osat_choice == "b":
            mon -= 5
            speed += 1
            derbilaatu += 3
            break
        elif osat_choice == "c":
            speed -= 2
            style -= 2
            derbilaatu -= 2
            break
        elif osat_choice == "d":
            mon -= 2
            derbilaatu += random.randint(-3, 2)
            speed += random.randint(-2, 2)
            break
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

osat()

# Viritys
def viritys():
    global mon, style, derbilaatu, speed, poliisi
    slow_print("Pitäisikö nyt virittää mopoa...", 0.05)
    slow_print("A: No ei vilivonkka vitussa!", 0.05)
    slow_print("B: Hiukan vääntöä ja kääntöä, laillisesti. (2 rahaa)", 0.05)
    slow_print("C: Täydet virit päälle! Ei ne poliisit saa mua kiinni. (4 rahaa)", 0.05)
    
    while True:
        viritys_choice = input().lower()
        
        if viritys_choice == "a":
            break
        elif viritys_choice == "b":
            mon -= 2
            speed += 1
            break
        elif viritys_choice == "c":
            speed += 4
            style += 2
            derbilaatu -= 1
            mon -= 4
            poliisi += 2
            break
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

viritys()

# Pärinät
def ääni():
    global mon, style, derbilaatu, speed, poliisi
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
        elif ääni_choice == "c" and mon > 1:
            poliisi += 1
            style += 3
            mon -= 2
            break
        elif ääni_choice == "c" and mon < 2:
            slow_print("Sinulla ei ole tarpeeksi rahaa.", 0.05)
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

ääni()

slow_print(f"Sinulla on nyt {mon} rahaa.", 0.05)

# Köyhille pojille
def rahapula():
    global mon, style, speed, derbilaatu, poliisi
    slow_print("Voi ei! Olet köyhempi kuin vietnamilainen lapsi tehtaassa!", 0.05)
    slow_print("A: Aika mennä kerjäämään kadulle.", 0.05)
    slow_print("B: Yritä vetää rahat viereisesi naisen taskusta hiljaa.", 0.05)
    slow_print("C: Rahaa on ihan tarpeeksi.", 0.05)
    slow_print("D: Ryöstä viereisesi nainen.", 0.05)
    slow_print("E: Pölli vanhempien pankki-informaatio", 0.05)
    
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
            mon += 1
            style -= 1
            slow_print("Onnistuit keräämään yhden rahan.", 0.05)
            break
        elif raha_choice == "b":
            raha_chance = random.randint(0, 100)
            if raha_chance > 50:
                taskuvaras_k()
                break
            if raha_chance <= 50:
                mon += 4
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
                mon += 15
            elif rahaonnistuminen < 9:
                slow_print("Jäit kiinni, hävisit pelin!", 0.05)
                input()
                exit()
                break
        
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

# Taskuvaras
def taskuvaras_k():
    global mon, poliisi, style
    slow_print("Jäit kiinni! Mitä teet nyt?", 0.05)
    slow_print("A: Juokse", 0.05)
    slow_print("B: Turpa kii vitun ämmä ja laita se saatanan imuri päälle!", 0.05)
    
    while True:
        fight_choice = input().lower()
        
        if fight_choice == "a":
            slow_print("Nainen soittaa sinivuokoille!", 0.05)
            break
        elif fight_choice == "b":
            slow_print("Anna turpiin sille vitun nartulle!", 0.05)
            fightwoman()
            break
        else:
            slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)
            
def fightwoman():
    global hp, sta, mon, poliisi, style, dmod, atmod, hitmod, hitroll, hit, shieldbreak, damage, dmgroll, womai, woman_hp, woman_sta, dodge, woda, wohit, wdodge, breaker2
    slow_print("--------Fight!!!--------", 0.1)
    slow_print("-You-      -Woman-", 0.5)
    slow_print("HP 12       HP 10", 0.05)
    slow_print("STA 20      STA 18", 0.05)

    woman_hp = 10
    woman_sta = 15

    while True:

        wohit = 0
        woda = 0
        wostagger = 0
        stagger = 0

        slow_print("Mitä teet?", 0.05)
        slow_print("1. Kick", 0.05)
        slow_print("2. Heavy punch", 0.05)
        slow_print("3. punch", 0.05)
        slow_print("4. block", 0.05)
        slow_print("5. dodge", 0.05)

        while True:

            while True:

                attackwomoption = input().lower()

                if attackwomoption == "1" and sta > 3:
                    sta -= 3
                    hitroll = (random.randint(0, 12))
                    hit = hitroll + hitmod
                    dmgroll = (random.randint(0, 5))
                    damage = dmgroll + dmod
                    shieldbreak = 2
                    break

                elif attackwomoption == "2" and sta > 5:
                    sta -= 5
                    hitroll = (random.randint(0, 12))
                    hit = hitroll + hitmod - 2
                    dmgroll = (random.randint(0, 7))
                    damage = dmgroll + dmod
                    break

                elif attackwomoption == "3" and sta > 2:
                    sta -= 2
                    hitroll = (random.randint(0, 12))
                    hit = hitroll + hitmod + 1
                    dmgroll = (random.randint(0, 5))
                    damage = dmgroll + dmod
                    break

                elif attackwomoption == "4":
                    sta += 1
                    break

                elif attackwomoption == "5" and sta > 2:
                    sta -= 2
                    dmod = 5
                    break

                else:
                    slow_print("Tuo ei ollut yksi vaihtoehdoista tai sinulla ei ole tarpeeksi staminaa. Yritä uudelleen.", 0.05)

            womai = (random.randint(0, 4))

            # 1 = light bag attack 2 = heavy bag attack 3 = frantic block 4 = mace

            if womai == 1:
                woman_sta -= 2
                wohit = (random.randint(0, 12))
                woda = (random.randint(0, 4))

            elif womai == 2:
                woman_sta -= 4
                wohit = (random.randint(0, 12)) - 2
                woda = (random.randint(0, 6))

            if womai == 1 or 2 and attackwomoption == "1" or "2" or "3":
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

            elif womai == 1 or 2 and attackwomoption == "4":
                if wohit > 7:
                    gothit()
                else:
                    woman_sta -= 5
                    if woman_sta < 1:
                        woman_sta = 5
                        slow_print("Naisen stamina loppui!", 0.05)
                        slow_print("Saat iskeä uudelleen!", 0.05)
                        stadodw = (random.randint(0, 10))
                        if stadodw > 8:
                            slow_print("Et osunut!", 0.05)
                        elif stadodw < 9:
                            slow_print("Osuit!", 0.05)
                            stahit = (random.randint(0, 4))
                            slow_print("Nainen menetti" + str(stahit) + " hp!", 0.05)
                            woman_hp -= stahit
                        if woman_hp < 1:
                            slow_print("Nainen kuoli, voitit taistelun!!!", 0.05)
                            loot()

            elif womai == 1 or 2 and attackwomoption == "5":
                dodge = (random.randint(0, 10)) + dmod
                if dodge < 9:
                    gothit()
                elif dodge > 8:
                    slow_print("Nainen ei osunut!", 0.05)

            elif womai == 3 and attackwomoption == "1" or "2" or "3":
                if hit + shieldbreak > 7:
                    slow_print("Sinä iskit torjunnan läpi!", 0.05)
                else:
                    sta -= 5
                    if sta < 1:
                        sta = 5
                        slow_print("Sinulta loppui stamina!", 0.05)
                        slow_print("Nainen lyö uudelleen!", 0.05)
                        stadod = random.randint(0, 10)
                        if stadod > 8:
                            slow_print("Nainen ei osunut!", 0.05)
                        elif stadod < 9:
                            slow_print("Sinuun osui!", 0.05)
                            stahitw = (random.randint(0, 4))
                            slow_print("Menetit " + str(stahitw) + " hp!", 0.05)
                            if hp < 1:
                                slow_print("Kuolit!!!", 0.05)
                                input()
                                exit()

            elif womai == 3 and attackwomoption == "4":

                slow_print("Molemmat puolustaa itseään... mitään ei tapahdu!", 0.05)

            elif womai == 3 and attackwomoption == "5":

                slow_print("Nainen puolustaa itseään... Mitään ei tapahdu!", 0.05)

            elif womai == 4 and attackwomoption == "1" or "2" or "3":

                wdodge = (random.randint(0, 10))
                if wdodge < 9:
                    hit_success()
                elif wdodge > 8:
                    getmaced()

            elif womai == 4 and attackwomoption == "4":

                getmaced()

            elif womai == 4 and attackwomoption == "5":

                getmaced()
            
            print("sinulla on "+str(hp)+" hp:tä!")
            print("sinulla on "+str(sta)+" staminaa!")
            
            if breaker == 1:
                break
        if breaker == 1:
            break
               
def hit_success():
    global woman_sta, woman_hp, stadodw, stahit
    slow_print("Osuit!", 0.05)
    slow_print("Nainen menetti " + str(damage) + " hp!", 0.05)
    slow_print("Nainen menetti " + str(damage) + " staminaa!", 0.05)
    woman_hp -= damage
    woman_sta -= damage
    dmod
    atmod
    hitmod = 0
    if woman_sta < 1:
        woman_sta = 5
        slow_print("Naiselta loppui stamina!", 0.05)
        slow_print("Saat lyödä uudelleen!", 0.05)
        stadodw = (random.randint(0, 10))
        if stadodw > 8:
            slow_print("Et osunut.", 0.05)
        elif stadodw < 9:
            slow_print("Sinä osuit!", 0.05)
            stahit = (random.randint(0, 4))
            slow_print("Nainen menetti " + str(stahit) + " hp!", 0.05)
            woman_hp -= stahit
    if woman_hp < 1:
        slow_print("Se vitun äämä kuoli!!!!", 0.05)
        loot()

def gothit():
    global hp, sta, stadod, stahitw
    slow_print("Sinuun osui!", 0.05)
    slow_print("Sinä menetit " + str(woda) + " hp!", 0.05)
    hp -= woda
    sta -= woda
    dmod = 0
    atmod = 0
    hitmod = 0
    if sta < 1:
        sta = 5
        slow_print("Sinulta loppui stamina!", 0.05)
        slow_print("Nainen lyö uudestaan!", 0.05)
        stadod = random.randint(0, 10)
        if stadod > 8:
            slow_print("Nainen ei osunut!", 0.05)
        elif stadod < 9:
            slow_print("Sinuun osui!", 0.05)
            stahitw = (random.randint(0, 4))
            slow_print("Menetit " + str(stahitw) + " hp!", 0.05)
    if hp < 1:
        slow_print("Kuolit!!!", 0.05)
        input()
        exit()

def getmaced():
    global poliisi
    slow_print("Nainen suihkutti sinua mace:lla!", 0.05)
    slow_print("Nainen soitti poliisit!", 0.05)
    slow_print("Nainen juoksi pakoon!")
    poliisi += 5
    breaker = 1

def loot():
    global breaker
    slow_print("Sait 8 rahaa!")
    mon += 8
    breaker = 1

if mon < 3: rahapula()

event_trigger()
event_trigger()
shop()
event_trigger()
ending()
