import time
import random

# slow print funktio

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
# peli alkaa

slow_print("Jos rakennat ittelles 88br derbin ja kohdistat keulan suoraan keulakulmille peli.", 0.05)
slow_print("paina enter aloittaaksesi.", 0.05)
input()

#aloitus stats

#hp

hp = 12

#stamina

sta = 20

#raha

mon = 10

#tyyli (pari eventtiä, score)

style = 0

# laatu (monta eventtiä, score)
derbilaatu = 0

# nopeus (monta eventtiä, score)

speed = 0

# wanted level

poliisi = 0

# älkää vetäkö huumeita lapset

addiktio = 0

# special item

waveglasses = 0

# special item

tcube = 0

#weapons

baton = 0

knife = 0

glock = 0

#level up, score

xp = 0

#level

level = 0

counterrattack = 0

right_hook = 0

fast_jab = 0

groin_shot = 0

spin_kick = 0

killer_lock = 0

dmod = 0

atmod = 0

defmod = 0

hitmod = 0

damage = 0

shieldbreak = 0

slow_print("Sinulla on 10 rahaa.", 0.05)

def osat():
    global mon
    global style
    global speed
    global derbilaatu
    slow_print("Aloit rakentamaan derbiä, mutta sinulta puuttuu osia!", 0.05)
    slow_print("mitä teet?", 0.05)
    slow_print("A: Kompromisoit osia kotoa.", 0.05)
    slow_print("B: Ostat uusia osia kaupasta. (5 rahaa)", 0.05)
    slow_print("C: Korjaat purukumilla.", 0.05)
    slow_print("D: Ostat alibabasta. (2 rahaa)", 0.05)
    
    # loop
    
    while True:
    
        osat_choice = input().lower()
        
        if osat_choice == "a":
            break
        
        elif osat_choice == "b":
            mon -= 5
            speed +=1
            derbilaatu +=3
            break
        
        elif osat_choice == "c":
            speed -=2
            syle -=2
            derbilaatu -=2
            break
            
        elif osat_choice == "d":
            mon -=2
            derbilaatu += (random.randint(-3,2))
            speed += (random.randint(-2,2))
            break
        
        else: slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)
osat()
        
# viritys

def viritys():
    global mon, style, derbilaatu, speed, poliisi
    slow_print("Pitäisikö nyt virittää mopoa...", 0.05)
    slow_print("A: No ei vilivonkka vitussa!", 0.05)
    slow_print("B: hieman vääntöä ja kääntöä, laillisesti. (2 rahaa)", 0.05)
    slow_print("C: täydet virit päälle! Ei ne poliisit saa mua kiinni. (4 rahaa)", 0.05)
    
    while True:
    
        viritys_choice = input().lower()
        
        if viritys_choice == "a":
            break
        
        elif viritys_choice == "b":
            mon -= 2
            speed +=1
            break
        
        elif viritys_choice == "c":
            speed +=4
            style +=2
            derbilaatu -=1
            mon -=4
            poliisi +=2
            break
    
        else: slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)
viritys()

# Pärinät

def ääni():
    global mon, style, derbilaatu, speed, poliisi
    slow_print("Laitetaanko päristely päälle?", 0.05)
    slow_print("A: Turhaa semmoinen.", 0.05)
    slow_print("B: Äänenvaimennin irti ja pärinä kuuluu.", 0.05)
    slow_print("C: Kyllä, ja kaijuttimet kaiken varaksi että kukaan ei saa unta! (2 rahaa)", 0.05)
    
    while True:
    
        viritys_choice = input().lower()
        
        if viritys_choice == "a":
            break
        
        elif viritys_choice == "b":
            style +=1
            break
        
        elif viritys_choice == "c" and mon > 1:
            poliisi +=1
            style +=3
            mon -=2
            break
        
        elif viritys_choice == "c" and mon < 2:
            slow_print("Sinulla ei ole tarpeeksi rahaa.")
    
        else: slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)
ääni()

slow_print("Sinulla on nyt "+mon+" rahaa.", 0.05)

# köyhille pojille

def rahapula():
    global mon, style, speed, derbilaatu, poliisi
    slow_print("Voi ei! Olet köyhempi kuin vietnamilainen lapsi tehtaassa!", 0.05)
    slow_print("A: aika mennä kerjäämään kadulle.", 0.05)
    slow_print("B: yritä vetää rahat viereisesi naisen taskusta hiljaa.", 0.05)
    slow_print("C: rahaa on ihan tarpeeksi.", 0.05)
    slow_print("D: ryöstä viereisesi nainen.", 0.05)
    
    while True:
    
        raha_choice = input().lower()
        
        if raha_choice == "a":
           speed -= 1
           mon += 1
           style -=1
           slow_print("Onnistuit keräämään yhden rahan.", 0.05)
           break
        
        elif raha_choice == "b":
            raha_chance = (random.randint(0,100))
            if raha_chance > 50:
                taskuvaras_k()
                break
            if raha_chance < 51:
                mon += 4
                slow_print("Sinä onnistuit! Sait 4 rahaa.", 0.05)
                break
        
        elif raha_choice == "c":
        
            
        elif raha_choice == "d":
           
        
        else: slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

def taskuvaras_k():
    global mon, poliisi, style
    slow_print("Jäit kiinni! Mitä teet nyt?", 0.05)
    slow_print("A: Juokse", 0.05)
    slow_print("B: Turpa kii vitun ämmä ja laita se saatanan imuri päälle!", 0.05)
    
    while True:
        
        fight_choice = input().lower()
        
        if fight_choice = "a":
            slow_print("Nainen soittaa sinivuokot paikalle!", 0.05)
            piipaa()
            break
        
        elif fight_choice = "b"
            slow_print("Anna turpiin sille vitun nartulle!", 0.05)
            fight()
            break
        
        else: slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)

def fightwoman():
    global hp, sta, mon, poliisi, style, dmod, atmod, defmod, hitmod, hitroll, hit, shieldbreak, damage, dmgroll, womai, woman_hp, woman_sta
    slow_print("--------Fight!!!--------", 0.1)
    slow_print("-You-      -Woman-", 0.5)
    slow_print("HP 12       HP 10", 0.05)
    slow_print("STA 20      STA 15", 0.05)
    
    woman_hp = 10
    woman_sta = 15
    
    while True:
        
        slow_print("What do you do?", 0.05)
        slow_print("1. Kick", 0.05)
        slow_print("2. Heavy punch", 0.05)
        slow_print("3. punch", 0.05)
        slow_print("4. block", 0.05)
        slow_print("5. dodge", 0.05)
        
        while True:
            
            while True:
            
                attackwomoption = input().lower()
            
                if attackwomoption == 1:
                    sta -=3
                    hitroll = (random.randint(0,12))
                    hit = hitroll + hitmod
                    dmgroll = (random.randint(0,5))
                    damage = dmgroll + dmod
                    shieldbreak = 2
                    break
                    
                elif attackwomoption == 2:
                    sta -=5
                    hitroll = (random.randint(0,12))
                    hit = hitroll + hitmod -2
                    dmgroll = (random.randint(0,8))
                    damage = dmgroll + dmod
                    break
                
                elif attackwomoption == 3:
                    sta -=2
                    hitroll = (random.randint(0,12))
                    hit = hitroll + hitmod +1
                    dmgroll = (random.randint(0,5))
                    damage = dmgroll + dmod
                    break
                     
                elif attackwomoption == 4:
                    break
                
                elif attackwomoption == 5:
                    sta -=2
                    dmod = 5
                    break
                
                else:
                    slow_print("Tuo ei ollut yksi vaihtoehdoista. Yritä uudelleen.", 0.05)
            
            womai = (random.randint(0,4))
            
            # 1 = light bag attack 2 = heavy bag attack 3 = frantic block 4 = mace
            
            if: womai == 1 and attackwomoption == 1 or 2 or 3:
                
            elif womai == 1 and attackwomoption == 4
            
            elif womai == 1 and attackwomoption == 5
