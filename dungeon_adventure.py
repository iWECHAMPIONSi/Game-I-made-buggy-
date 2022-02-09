import os
import random
import sys
import time
    
def sp(char):
    for char in char:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char == "\n":
            time.sleep(0.5)
        if char == "!":
            time.sleep(1)
        if char == "?":
            time.sleep(1)
        if char == ".":
            time.sleep(1)
        if char == ",":
            time.sleep(0.5)
        if char == "|":
            time.sleep(1)
        else:
            time.sleep(0.05)

    
def progress():
    win = False
    say = random.randint(1,5)
    if say == 1:
        sp("You observe your surroundings,")
    if say == 2:
        sp("You sit down on the cold stone floor,")
    if say == 3:
        sp("You lay against the moist, humid wall,")
    if say == 4:
        sp("You stretch to pass the time,")
    if say == 5:
        sp("You do an inventory check before you go on")
    sp("what will you do?" '\n'
       "1) Continue forward"'\n'
       "2) Shop" '\n'
       "3) Drink a potion")
    Progress = input
    if Progress == 1:
        pass
    elif Progress == 2:
        shop()
    elif Progress == 3:
        sp("1) Health potion 30 hp" '\n'
           "2) Mana potion 50 mana" '\n')
        drinkp = input
        if drinkp == 1:
            if player['healp'] <= 1:
                player['hp'] = player['hp'] + 30
                player['healp'] = player['healp'] - 1
                sp("You gained 30 hp"'\n')
            else:
                sp("You don't have any heal potions"'\n')
        if drinkp == '2':
            if player['manap'] <= 1:
                player['mana'] = player['mana'] + 50
                player['manap'] = player['manap'] - 1
                sp("You gained 50 mana"'\n')
            else:
                sp("You don't have any mana potions")
    else:
        sp("ERROR"'\n')
        progress()
    
Battle2 = False
Battle3 = False
Battle4 = False
Battle5 = False
win = False
lose = False
fireball = False
icewave = False
weakcurse = False
witherwind = False
shop = False
Game = False

def cobalt1():
    enemy['name'] = 'cobalt'
    enemy['hp'] = 30
    enemy['dmgmin'] = 5
    enemy['dmgmax'] = 15
    enemy['type'] = 0
    enemy['lvl'] = 1
    enemy['nextlvl'] = 25
    enemy['mana'] = 0
    enemy['arrows'] = 0
    enemy['bow'] = 'none'
    enemy['sword'] = 'dagger'
    enemy['coins'] = 30
    enemy['xp'] = 50
    enemy['intel'] = 1
    enemy['str'] = 3
    enemy['dex'] = 2
    enemy['intel'] = 1
    enemy['sdmg'] = 3
    enemy['bdmg'] = 0
    enemy['lvlxp'] = 0
    
def cobalt2():
    enemy2['name'] = 'cobalt 2'
    enemy2['hp'] = 30
    enemy2['dmgmin'] = 5
    enemy2['dmgmax'] = 15
    enemy2['type'] = 0
    enemy2['lvl'] = 1
    enemy2['nextlvl'] = 25
    enemy2['mana'] = 0
    enemy2['arrows'] = 0
    enemy2['bow'] = 'none'
    enemy2['sword'] = 'dagger'
    enemy2['coins'] = 30
    enemy2['xp'] = 50
    enemy2['intel'] = 1
    enemy2['str'] = 3
    enemy2['dex'] = 2
    enemy2['intel'] = 1
    enemy2['sdmg'] = 3
    enemy2['bdmg'] = 0
    enemy2['lvlxp'] = 0

def cobalt3():
    enemy3['name'] = 'cobalt 3'
    enemy3['hp'] = 30
    enemy3['dmgmin'] = 5
    enemy3['dmgmax'] = 15
    enemy3['type'] = 0
    enemy3['lvl'] = 1
    enemy3['nextlvl'] = 25
    enemy3['mana'] = 0
    enemy3['arrows'] = 0
    enemy3['bow'] = 'none'
    enemy3['sword'] = 'dagger'
    enemy3['coins'] = 30
    enemy3['xp'] = 50
    enemy3['intel'] = 1
    enemy3['str'] = 3
    enemy3['dex'] = 2
    enemy3['intel'] = 1
    enemy3['sdmg'] = 3
    enemy3['bdmg'] = 0
    enemy3['lvlxp'] = 0
    
def orc1():
    enemy['name'] = 'orc'
    enemy['hp'] = 100
    enemy['dmgmin'] = 10
    enemy['dmgmax'] = 18
    enemy['type'] = 0
    enemy['lvl'] = 1
    enemy['nextlvl'] = 25
    enemy['mana'] = 0
    enemy['arrows'] = 0
    enemy['bow'] = 'none'
    enemy['sword'] = 'club'
    enemy['coins'] = 100
    enemy['xp'] = 100
    enemy['intel'] = 0
    enemy['str'] = 5
    enemy['dex'] = 0
    enemy['intel'] = 1
    enemy['sdmg'] = 1
    enemy['bdmg'] = 0
    enemy['lvlxp'] = 0
    
def orc2():
    enemy2['name'] = 'orc 2'
    enemy2['hp'] = 100
    enemy2['dmgmin'] = 10
    enemy2['dmgmax'] = 18
    enemy2['type'] = 0
    enemy2['lvl'] = 1
    enemy2['nextlvl'] = 25
    enemy2['mana'] = 0
    enemy2['arrows'] = 0
    enemy2['bow'] = 'none'
    enemy2['sword'] = 'club'
    enemy2['coins'] = 100
    enemy2['xp'] = 100
    enemy2['intel'] = 0
    enemy2['str'] = 5
    enemy2['dex'] = 0
    enemy2['intel'] = 1
    enemy2['sdmg'] = 1
    enemy2['bdmg'] = 0
    enemy2['lvlxp'] = 0
    
def orc3():
    enemy3['name'] = 'orc 3'
    enemy3['hp'] = 100
    enemy3['dmgmin'] = 10
    enemy3['dmgmax'] = 18
    enemy3['type'] = 0
    enemy3['lvl'] = 1
    enemy3['nextlvl'] = 25
    enemy3['mana'] = 0
    enemy3['arrows'] = 0
    enemy3['bow'] = 'none'
    enemy3['sword'] = 'club'
    enemy3['coins'] = 100
    enemy3['xp'] = 100
    enemy3['intel'] = 0
    enemy3['str'] = 5
    enemy3['dex'] = 0
    enemy3['intel'] = 1
    enemy3['sdmg'] = 1
    enemy3['bdmg'] = 0
    enemy3['lvlxp'] = 0

def archer1():
    enemy['name'] = 'archer'
    enemy['hp'] = 30
    enemy['dmgmin'] = 6
    enemy['dmgmax'] = 15
    enemy['type'] = 1
    enemy['lvl'] = 1
    enemy['nextlvl'] = 25
    enemy['mana'] = 0
    enemy['arrows'] = 20
    enemy['bow'] = 'wood'
    enemy['sword'] = 'dagger'
    enemy['coins'] = 30
    enemy['xp'] = 50
    enemy['intel'] = 2
    enemy['str'] = 0
    enemy['dex'] = 5
    enemy['intel'] = 2
    enemy['sdmg'] = 1
    enemy['bdmg'] = 4
    enemy['lvlxp'] = 0
    
def archer2():
    enemy2['name'] = 'archer 2'
    enemy2['hp'] = 30
    enemy2['dmgmin'] = 6
    enemy2['dmgmax'] = 15
    enemy2['type'] = 1
    enemy2['lvl'] = 1
    enemy2['nextlvl'] = 25
    enemy2['mana'] = 0
    enemy2['arrows'] = 20
    enemy2['bow'] = 'wood'
    enemy2['sword'] = 'dagger'
    enemy2['coins'] = 30
    enemy2['xp'] = 50
    enemy2['intel'] = 2
    enemy2['str'] = 0
    enemy2['dex'] = 5
    enemy2['intel'] = 2
    enemy2['sdmg'] = 1
    enemy2['bdmg'] = 4
    enemy2['lvlxp'] = 0

def archer3():
    enemy3['name'] = 'archer 3'
    enemy3['hp'] = 30
    enemy3['dmgmin'] = 6
    enemy3['dmgmax'] = 15
    enemy3['type'] = 1
    enemy3['lvl'] = 1
    enemy3['nextlvl'] = 25
    enemy3['mana'] = 0
    enemy3['arrows'] = 20
    enemy3['bow'] = 'wood'
    enemy3['sword'] = 'dagger'
    enemy3['coins'] = 30
    enemy3['xp'] = 50
    enemy3['intel'] = 2
    enemy3['str'] = 0
    enemy3['dex'] = 5
    enemy3['intel'] = 2
    enemy3['sdmg'] = 1
    enemy3['bdmg'] = 4
    enemy3['lvlxp'] = 0

def spider1():
    enemy['name'] = 'spider'
    enemy['hp'] = 40
    enemy['dmgmin'] = 3
    enemy['dmgmax'] = 8
    enemy['type'] = 0
    enemy['lvl'] = 1
    enemy['nextlvl'] = 25
    enemy['mana'] = 0
    enemy['arrows'] = 0
    enemy['bow'] = 'none'
    enemy['sword'] = 'fangs'
    enemy['coins'] = 20
    enemy['xp'] = 20
    enemy['intel'] = 1
    enemy['str'] = 2
    enemy['dex'] = 1
    enemy['intel'] = 1
    enemy['sdmg'] = 1
    enemy['bdmg'] = 0
    enemy['lvlxp'] = 0
    
def spider2():
    enemy2['name'] = 'spider 2'
    enemy2['hp'] = 40
    enemy2['dmgmin'] = 3
    enemy2['dmgmax'] = 8
    enemy2['type'] = 0
    enemy2['lvl'] = 1
    enemy2['nextlvl'] = 25
    enemy2['mana'] = 0
    enemy2['arrows'] = 0
    enemy2['bow'] = 'none'
    enemy2['sword'] = 'fangs'
    enemy2['coins'] = 20
    enemy2['xp'] = 20
    enemy2['intel'] = 1
    enemy2['str'] = 2
    enemy2['dex'] = 1
    enemy2['intel'] = 1
    enemy2['sdmg'] = 1
    enemy2['bdmg'] = 0
    enemy2['lvlxp'] = 0

def spider3():
    enemy3['name'] = 'spider 3'
    enemy3['hp'] = 40
    enemy3['dmgmin'] = 3
    enemy3['dmgmax'] = 8
    enemy3['type'] = 0
    enemy3['lvl'] = 1
    enemy3['nextlvl'] = 25
    enemy3['mana'] = 0
    enemy3['arrows'] = 0
    enemy3['bow'] = 'none'
    enemy3['sword'] = 'fangs'
    enemy3['coins'] = 20
    enemy3['xp'] = 20
    enemy3['intel'] = 1
    enemy3['str'] = 2
    enemy3['dex'] = 1
    enemy3['intel'] = 1
    enemy3['sdmg'] = 1
    enemy3['bdmg'] = 0
    enemy3['lvlxp'] = 0

def imp1():
    enemy['name'] = 'imp'
    enemy['hp'] = 20
    enemy['dmgmin'] = 2
    enemy['dmgmax'] = 5
    enemy['type'] = 0
    enemy['lvl'] = 1
    enemy['nextlvl'] = 25
    enemy['mana'] = 0
    enemy['arrows'] = 0
    enemy['bow'] = 'none'
    enemy['sword'] = 'claws'
    enemy['coins'] = 10
    enemy['xp'] = 10
    enemy['intel'] = 1
    enemy['str'] = 1
    enemy['dex'] = 1
    enemy['intel'] = 1
    enemy['sdmg'] = 0
    enemy['bdmg'] = 0
    enemy['lvlxp'] = 0

def imp2():
    enemy2['name'] = 'imp 2'
    enemy2['hp'] = 20
    enemy2['dmgmin'] = 2
    enemy2['dmgmax'] = 5
    enemy2['type'] = 0
    enemy2['lvl'] = 1
    enemy2['nextlvl'] = 25
    enemy2['mana'] = 0
    enemy2['arrows'] = 0
    enemy2['bow'] = 'none'
    enemy2['sword'] = 'claws'
    enemy2['coins'] = 10
    enemy2['xp'] = 10
    enemy2['intel'] = 1
    enemy2['str'] = 1
    enemy2['dex'] = 1
    enemy2['intel'] = 1
    enemy2['sdmg'] = 0
    enemy2['bdmg'] = 0
    enemy2['lvlxp'] = 0

def imp3():
    enemy3['name'] = 'imp 3'
    enemy3['hp'] = 20
    enemy3['dmgmin'] = 2
    enemy3['dmgmax'] = 5
    enemy3['type'] = 0
    enemy3['lvl'] = 1
    enemy3['nextlvl'] = 25
    enemy3['mana'] = 0
    enemy3['arrows'] = 0
    enemy3['bow'] = 'none'
    enemy3['sword'] = 'claws'
    enemy3['coins'] = 10
    enemy3['xp'] = 10
    enemy3['intel'] = 1
    enemy3['str'] = 1
    enemy3['dex'] = 1
    enemy3['intel'] = 1
    enemy3['sdmg'] = 0
    enemy3['bdmg'] = 0
    enemy3['lvlxp'] = 0

def enemylvl():
    while enemy['lvlxp'] >= enemy['nextlvl']:
        enemy['lvlxp'] = enemy['lvlxp']-enemy['nextlvl']
        enemy['nextlvl'] = round(enemy['nextlvl'] * 1.5)
        enemy['maxhp'] = enemy['maxhp'] + 5
        enemy['maxmana'] = enemy['maxmana'] + 5
        enemy['str'] = enemy['str'] + 1
        enemy['dex'] = enemy['dex'] + 1
        enemy['hp'] = enemy['maxhp']
        enemy['dmgmin'] = enemy['dmgmin'] + 1
        enemy['dmgmax'] = enemy['dmgmax'] + 1
        enemy['lvl'] = enemy['lvl'] + 1
        enemy['intel'] = enemy['intel'] + 1
        enemy['xp'] = round(enemy['xp']*1.2)
        enemy['coins'] = round(enemy['coins']*1.2)
        enemy['arrows'] = round(enemy['arrows']*1.5)
    while enemy2['lvlxp'] >= enemy2['nextlvl']:
        enemy2['lvlxp'] = enemy2['lvlxp']-enemy2['nextlvl']
        enemy2['nextlvl'] = round(enemy2['nextlvl'] * 1.5)
        enemy2['maxhp'] = enemy2['maxhp'] + 5
        enemy2['maxmana'] = enemy2['maxmana'] + 5
        enemy2['str'] = enemy2['str'] + 1
        enemy2['dex'] = enemy2['dex'] + 1
        enemy2['hp'] = enemy2['maxhp']
        enemy2['dmgmin'] = enemy2['dmgmin'] + 1
        enemy2['dmgmax'] = enemy2['dmgmax'] + 1
        enemy2['lvl'] = enemy2['lvl'] + 1
        enemy2['intel'] = enemy2['intel'] + 1
        enemy2['xp'] = round(enemy2['xp']*1.2)
        enemy2['coins'] = round(enemy2['coins']*1.2)
        enemy2['arrows'] = round(enemy2['arrows']*1.5)
    while enemy3['lvlxp'] >= enemy3['nextlvl']:
        enemy3['lvlxp'] = enemy3['lvlxp']-enemy['nextlvl']
        enemy3['nextlvl'] = round(enemy3['nextlvl'] * 1.5)
        enemy3['maxhp'] = enemy3['maxhp'] + 5
        enemy3['maxmana'] = enemy3['maxmana'] + 5
        enemy3['str'] = enemy3['str'] + 1
        enemy3['dex'] = enemy3['dex'] + 1
        enemy3['hp'] = enemy3['maxhp']
        enemy3['dmgmin'] = enemy3['dmgmin'] + 1
        enemy3['dmgmax'] = enemy3['dmgmax'] + 1
        enemy3['lvl'] = enemy3['lvl'] + 1
        enemy3['intel'] = enemy3['intel'] + 1
        enemy3['xp'] = round(enemy3['xp']*1.2)
        enemy3['coins'] = round(enemy3['coins']*1.2)
        enemy3['arrows'] = round(enemy3['arrows']*1.5)

def loading():
    os.system('cls')
    sp("Loading |||||")
    os.system('cls')
    sp("Loading complete")
    time.sleep(3)
    os.system('cls')
    
def Loading():
    os.system('cls')
    sp("Loading |||||")
    os.system('cls')

def Win():
    Battle2 = False
    Battle3 = False
    Battle4 = False
    Battle5 = False
    win = True
    sp("You have won the battle!")
    player['xp'] = player['xp'] + enemy['xp']+ enemy2['xp']+ enemy3['xp']
    player['coins'] = player['coins'] + enemy['coins']+ enemy2['coins']+ enemy3['coins']
    level()
    
def lose():
    lose = True
    time.sleep(5)
    os.system('cls')
    sp("|||||")
    time.sleep(1)
    os.system('cls')
    sp("Game over")
    time.sleep(3)
    os.system('cls')
    time.sleep(3)
    while lose == True:
        os.system('cls')
        sp ("Game Over")
        time.sleep(3)
        os.system('cls')
        time.sleep(3)
    
def playerstat():
    print(player['name'], '\n'
    "Level:", player['lvl'], '\n'
    "XP:", player['xp'], '\n'
    "Next level:", player['nextlvl'], '\n'
    "Health:", player['hp'], '\n'
    "Damage:", player['dmgmin'],"to", player['dmgmax'], '\n'
    "Spell Damage", player['spelldmg'], '\n'
    "Dexterity:", player['dex'], '\n'
    "Strength:", player['str'], '\n'
    "Intelegence", player['intel'], '\n'
    "Mana:", player['mana'], '\n'
    "Arrows:", player['arrows'], '\n'
    "Sword:", player['sword'],'\n')

def enemystat():
    print(enemy['name'], '\n'
    "Level:",enemy['lvl'], '\n'
    "XP:",enemy['xp'], '\n'
    "Health:",enemy['hp'], '\n'
    "Damage:",enemy['dmgmin'],"to", enemy['dmgmax'], '\n'
    "Spell Damage", enemy['spelldmg'], '\n'
    "Dexterity:",enemy['dex'], '\n'
    "Strength",enemy['str'], '\n'
    "Intelegence", enemy['intel'], '\n'
    "Mana:",enemy['mana'], '\n'
    "Arrows:",enemy['arrows'], '\n'
    "Sword:",enemy['sword'], '\n'
    "Bow:",enemy['bow'], '\n'
    "Coins:",enemy['coins'],'\n')
    
def enemy2stat():
    print(enemy2['name'], '\n'
    "Level:",enemy2['lvl'], '\n'
    "XP:",enemy2['xp'], '\n'
    "Health:",enemy2['hp'], '\n'
    "Damage:",enemy2['dmgmin'],"to", enemy['dmgmax'], '\n'
    "Spell Damage", enemy2['spelldmg'], '\n'
    "Dexterity:",enemy2['dex'], '\n'
    "Strength",enemy2['str'], '\n'
    "Intelegence", enemy2['intel'], '\n'
    "Mana:",enemy2['mana'], '\n'
    "Arrows:",enemy2['arrows'], '\n'
    "Sword:",enemy2['sword'], '\n'
    "Bow:",enemy2['bow'], '\n'
    "Coins:",enemy2['coins'],'\n')

def enemy3stat():
    print(enemy3['name'], '\n'
    "Level:",enemy3['lvl'], '\n'
    "XP:",enemy3['xp'], '\n'
    "Health:",enemy3['hp'], '\n'
    "Damage:",enemy3['dmgmin'],"to", enemy['dmgmax'], '\n'
    "Spell Damage", enemy3['spelldmg'], '\n'
    "Dexterity:",enemy3['dex'], '\n'
    "Strength",enemy3['str'], '\n'
    "Intelegence", enemy3['intel'], '\n'
    "Mana:",enemy3['mana'], '\n'
    "Arrows:",enemy3['arrows'], '\n'
    "Sword:",enemy3['sword'], '\n'
    "Bow:",enemy3['bow'], '\n'
    "Coins:",enemy3['coins'],'\n')
    
def enemystat1():
    print(enemy['name'], '\n'
         "Level:",enemy['lvl'], '\n'
         "Damage", enemy['dmgmin'], "to", enemy['dmgmax'], '\n'
         "Health:",enemy['hp'], '\n')
    
def enemy2stat1():
    print(enemy2['name'], '\n'
         "Level:",enemy2['lvl'], '\n'
         "Damage", enemy2['dmgmin'], "to", enemy2['dmgmax'], '\n'
         "Health:",enemy2['hp'], '\n')

def enemy3stat1():
    print(enemy3['name'], '\n'
         "Level:",enemy3['lvl'], '\n'
         "Damage", enemy3['dmgmin'], "to", enemy3['dmgmax'], '\n'
         "Health:",enemy3['hp'], '\n')
def playerstat1():
    print(player['name'], '\n'
            "Level:", player['lvl'], '\n'
            "Health:", player['hp'], '\n'
            "Damage", player['dmgmin'], "to", player['dmgmax'], '\n'
            "Arrows:", player['arrows'], '\n'
            "Mana:", player['mana'], '\n')

player = {'name' : 'Hero', 'hp' : 100, 'maxhp' : 100, 'dmgmin' : 5, 'dmgmax' : 10, 'mana' : 0, 'maxmana' : 0, 'arrows' : 0, 'sword' : 'wood',
          'lvl' : 1,'nextlvl' : 25,'xp' : 0, 'dex' : 1, 'str' : 1, 'bow' : 'wood', 'coins' : 0, 'intel' : 1, 'spelldmg' : 0, 'bdmg' : 0,
          'sdmg' : 0, 'spells' : 0,'healp' : 0, 'manap' : 0, 'lhealp' : 0, 'lmanap' : 0}

enemy = {'name' : 'imp', 'dmgmin' : 2, 'dmgmax' : 8, 'hp' : 20, 'lvl' : 1, 'mana' : 0, 'arrows' : 0, 'dex' : 0, 'sword' : 'claws', 'bow' : 'none',
         'coins' : 10, 'str' : 1, 'dex' : 1, 'xp' : 10, 'intel' : 1, 'spelldmg' : 0, 'type' : 0, 'bdmg' : 0, 'sdmg' : 0, 'spells' : 0,
         'nextlvl' :25, 'lvlxp' : 0}

enemy2 = {'name' : 'imp', 'dmgmin' : 0, 'dmgmax' : 0, 'hp' : 0, 'lvl' : 0, 'mana' : 0, 'arrows' : 0, 'dex' : 0, 'sword' : 'claws', 'bow' : 'none',
         'coins' : 0, 'str' : 0, 'dex' : 0, 'xp' : 0, 'intel' : 0, 'spelldmg' : 0, 'type' : 0, 'bdmg' : 0, 'sdmg' : 0, 'spells' : 0,
         'nextlvl' : 25, 'lvlxp' : 0}

enemy3 = {'name' : 'imp', 'dmgmin' : 0, 'dmgmax' : 0, 'hp' : 0, 'lvl' : 0, 'mana' : 0, 'arrows' : 0, 'dex' : 0, 'sword' : 'claws', 'bow' : 'none',
         'coins' : 0, 'str' : 0, 'dex' : 0, 'xp' : 0, 'intel' : 0, 'spelldmg' : 0, 'type' : 0, 'bdmg' : 0, 'sdmg' : 0, 'spells' : 0,
         'nextlvl' : 25, 'lvlxp' : 0}

def level():
    while player['xp'] >= player['nextlvl']:
        os.system('cls')
        print("Level:", player['lvl'], "-->", player['lvl']+1, '\n'
              "Next level:",player['nextlvl'], "-->", round(player['nextlvl']*1.5), '\n'
              "Xp:", player['xp'], "-->", player['xp']-round(player['nextlvl']*1.5), '\n'
              "HP:", player['maxhp'], "-->", player['maxhp']+5, '\n'
              "Min damage:", player['dmgmin'], "-->", player['dmgmax']+1, '\n'
              "Max damage:", player['dmgmax'], "-->", player['dmgmax']+1, '\n'
              "Mana:",player['maxmana'], "-->", player['maxmana']+5, '\n'
              "Strength:", player['str'], "-->", player['str']+1, '\n'
              "Dexterity:", player['dex'], "-->", player['dex']+1, '\n'
              "Inteligence:", player['intel'], "-->", player['intel']+1, '\n') 
        player['xp'] = player['xp']-player['nextlvl']
        player['nextlvl'] = round(player['nextlvl'] * 1.5)
        player['maxhp'] = player['maxhp'] + 5
        player['maxmana'] = player['maxmana'] + 5
        player['str'] = player['str'] + 1
        player['dex'] = player['dex'] + 1
        player['hp'] = player['maxhp']
        player['dmgmin'] = player['dmgmin'] + 1
        player['dmgmax'] = player['dmgmax'] + 1
        player['lvl'] = player['lvl'] + 1
        player['intel'] = player['intel'] + 1
        

def battle():
    Battle2 = False
    os.system('cls')
    playerstat1()
    if Battle3 == True:
        enemystat1()
    if Battle4 == True:
        enemystat1()
        enemy2stat1()
    if Battle5 == True:
        enemystat1()
        enemy2stat1()
        enemy3stat1()
    time.sleep(3)
    print("Attack" '\n'
                    '\n'
            "1) Sword" '\n'
            "2) Bow" '\n'
            "3) Spells" '\n'
            "4) Items" '\n'
            "5) Escape", enemy['coins']+enemy2['coins']+enemy3['coins'],"coins")
    Attack = input()
    if Attack == '1':
        if Battle3 == True:
            enemy['hp'] = enemy['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['str']+player['sdmg']
            time.sleep(1)
        if Battle4 == True:
            print("Who will you attack?", '\n'
                                "1)", enemy['name'], '\n'
                                "2)", enemy2['name'],'\n')
            time.sleep(0.01)
            attack1 = input(
                            )
            if attack1 == '1':
                enemy['hp'] = enemy['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['str']+player['sdmg']
                time.sleep(1)
            elif attack1 == '2':
                enemy['hp'] = enemy2['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['str']+player['sdmg']
                time.sleep(1)
            else:
                sp("You fumble and recover but can't attack"'\n')
        if Battle5 == True:
            print("Who will you attack?", '\n'
                                "1)", enemy['name'], '\n'
                                "2)", enemy2['name'], '\n'
                                "3)", enemy3['name'],'\n')
            time.sleep(0.01)
            attack3 = input()
            if attack3 == '1':
                enemy['hp'] = enemy['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['str']+player['sdmg']
                time.sleep(1)
            elif attack3 == '2':
                enemy2['hp'] = enemy2['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['str']+player['sdmg']
                time.sleep(1)
            elif attack3 == '3':
                enemy3['hp'] = enemy3['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['str']+player['sdmg']
                time.sleep(1)
            else:
                sp("You fumble and recover but can't attack"'\n')
    elif Attack == '2':
        if Battle3 == True:
            enemy['hp'] = enemy['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['dex']+player['bdmg']
            time.sleep(1)
        if Battle4 == True:
            print("Who will you attack?", '\n'
                                "1)", enemy['name'], '\n'
                                "2)", enemy2['name'],'\n')
            time.sleep(0.01)
                                
            attack1 = input()
            enemystat1()
            enemy2stat1()
            if attack1 == '1':
                enemy['hp'] = enemy['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['dex']+player['bdmg']
                time.sleep(1)
            elif attack1 == '2':
                enemy2['hp'] = enemy2['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['dex']+player['bdmg']
                time.sleep(1)
            else:
                sp("You fumble and recover but can't attack"'\n')
        if Battle5 == True:
            print("Who will you attack?", '\n'
                                "1)", enemy['name'], '\n'
                                "2)", enemy2['name'], '\n'
                                "3)", enemy3['name'],'\n')
            time.sleep(0.01)
            attack2 = input(
                                )
            enemystat1()
            enemy2stat1()
            enemy3stat1()
            if attack2 == '1':
                enemy['hp'] = enemy['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['dex']+player['bdmg']
                time.sleep(1)
            elif attack2 == '2':
                enemy2['hp'] = enemy2['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['dex']+player['bdmg']
                time.sleep(1)
            elif attack2 == '3':
                enemy3['hp'] = enemy3['hp']-random.randint(player['dmgmin'], player['dmgmax'])+player['dex']+player['bdmg']
                time.sleep(1)
            else:
                sp("You fumble and recover but can't attack"'\n')
    elif Attack == '3':
        if player['mana'] >=15:
            if player['spells'] == 0:
                sp("You rifle through your empty spellbook and can't cast a spell"'\n')
            else:
                time.sleep(0.01)
                cast = input("What will you cast?" '\n'
                            "1) Fireball  15 mana" '\n'
                            "2) Ice wave  15 mana"'\n'
                            "3) Weakening curse 30 mana" '\n'
                            "4) Withering wind 75 mana" '\n')
                if cast == '1':
                    if player['mana'] >= 15:
                        if Battle3 == True:
                            enemy['hp'] = enemy['hp']-(30+player['intel'],'\n')
                            player['mana'] = player['mana'] - 15
                        if Battle4 == True:
                            print("Who will you attack?", '\n'
                                "1)", enemy['name'], '\n'
                                "2)", enemy2['name'],'\n')
                            attack1 = input
                            if attack1 == '1':
                                enemy['hp'] = enemy['hp']-(30+player['intel'],'\n')
                                player['mana'] = player['mana'] - 15
                            elif attack1 == '2':
                                enemy2['hp'] = enemy2['hp']-(30+player['intel'],'\n')
                                player['mana'] = player['mana'] - 15
                            else:
                                sp("You fumble and recover but can't attack"'\n')
                        if Battle5 == True:
                            print("Who will you attack?", '\n'
                                "1)", enemy['name'], '\n'
                                "2)", enemy2['name'],'\n'
                                "3)", enemy3['name'], '\n')
                            attack1 = input
                            if attack1 == '1':
                                enemy['hp'] = enemy['hp']-(30+player['intel'],'\n')
                                player['mana'] = player['mana'] - 15
                            elif attack1 == '2':
                                enemy2['hp'] = enemy2['hp']-(30+player['intel'],'\n')
                                player['mana'] = player['mana'] - 15
                            elif attack1 == '3':
                                enemy['hp'] = enemy['hp']-(30+player['intel'],'\n')
                                player['mana'] = player['mana'] - 15
                            else:
                                sp("You fumble and recover but can't attack"'\n')
                    else:
                        sp("You tried to cast but didn't have enough mana"'\n')
                elif cast == '2':
                    if player['mana'] >= 15:
                        if player['spells'] > 1:
                            if Battle3 == True:
                                enemy['hp'] = enemy['hp']-(5+player['intel'])
                                enemy['dex'] = enemy['dex']-(2+player['intel'])
                                player['mana'] = player['mana']-15
                            if Battle4 == True:
                                print("Who will you attack?", '\n'
                                    "1)", enemy['name'], '\n'
                                    "2)", enemy2['name'],'\n')
                                attack1 = input
                                if attack1 == '1':
                                    enemy['hp'] = enemy['hp']-(5+player['intel'])
                                    enemy['dex'] = enemy['dex']-(2+player['intel'])
                                    player['mana'] = player['mana']-15
                                elif attack1 == '2':
                                    enemy2['hp'] = enemy2['hp']-(5+player['intel'])
                                    enemy2['dex'] = enemy2['dex']-(2+player['intel'])
                                    player['mana'] = player['mana']-15
                                else:
                                    sp("You fumble and recover but can't attack"'\n')
                            if Battle5 == True:
                                print("Who will you attack?", '\n'
                                    "1)", enemy['name'], '\n'
                                    "2)", enemy2['name'],'\n'
                                    "3)", enemy3['name'], '\n')
                                attack1 = input
                                if attack1 == '1':
                                    enemy['hp'] = enemy['hp']-(5+player['intel'])
                                    enemy['dex'] = enemy['dex']-(2+player['intel'])
                                    player['mana'] = player['mana']-15
                                elif attack1 == '2':
                                    enemy2['hp'] = enemy2['hp']-(5+player['intel'])
                                    enemy2['dex'] = enemy2['dex']-(2+player['intel'])
                                    player['mana'] = player['mana']-15
                                elif attack1 == '3':
                                    enemy3['hp'] = enemy3['hp']-(5+player['intel'])
                                    enemy3['dex'] = enemy3['dex']-(2+player['intel'])
                                    player['mana'] = player['mana']-15
                                else:
                                    sp("You fumble and recover but can't attack"'\n')
                elif cast == '3':
                    if player['mana'] >= 30:
                        if player['spells'] > 2:
                            if Battle3 == True:
                                enemy['hp'] = enemy['hp']-(5+player['intel'])
                                enemy['str'] = enemy['str']-(2+player['intel'])
                                player['mana'] = player['mana']-30
                            if Battle4 == True:
                                print("Who will you attack?", '\n'
                                    "1)", enemy['name'], '\n'
                                    "2)", enemy2['name'],'\n')
                                attack1 = input
                                if attack1 == '1':
                                    enemy['hp'] = enemy['hp']-(5+player['intel'])
                                    enemy['str'] = enemy['str']-(2+player['intel'])
                                    player['mana'] = player['mana']-30
                                elif attack1 == '2':
                                    enemy2['hp'] = enemy2['hp']-(5+player['intel'])
                                    enemy2['str'] = enemy2['str']-(2+player['intel'])
                                    player['mana'] = player['mana']-30
                                else:
                                    sp("You fumble and recover but can't attack"'\n')
                            if Battle5 == True:
                                print("Who will you attack?", '\n'
                                    "1)", enemy['name'], '\n'
                                    "2)", enemy2['name'],'\n'
                                    "3)", enemy3['name'], '\n')
                                attack1 = input
                                if attack1 == '1':
                                    enemy['hp'] = enemy['hp']-(5+player['intel'])
                                    enemy['str'] = enemy['str']-(2+player['intel'])
                                    player['mana'] = player['mana']-30
                                elif attack1 == '2':
                                    enemy2['hp'] = enemy2['hp']-(5+player['intel'])
                                    enemy2['str'] = enemy2['str']-(2+player['intel'])
                                    player['mana'] = player['mana']-30
                                elif attack1 == '3':
                                    enemy3['hp'] = enemy3['hp']-(5+player['intel'])
                                    enemy3['str'] = enemy3['str']-(2+player['intel'])
                                    player['mana'] = player['mana']-30
                                else:
                                    sp("You fumble and recover but can't attack"'\n')
                    else:
                        sp("You tried to cast but didn't have enough mana"'\n')
                if cast == '1':
                    if player['mana'] >= 15:
                        if Battle3 == True:
                            enemy['hp'] = enemy['hp']-(60+player['intel'],'\n')
                            player['mana'] = player['mana'] - 75
                        if Battle4 == True:
                            print("Who will you attack?", '\n'
                                "1)", enemy['name'], '\n'
                                "2)", enemy2['name'],'\n')
                            attack1 = input
                            if attack1 == '1':
                                enemy['hp'] = enemy['hp']-(60+player['intel'],'\n')
                                player['mana'] = player['mana'] - 75
                            elif attack1 == '2':
                                enemy2['hp'] = enemy2['hp']-(60+player['intel'],'\n')
                                player['mana'] = player['mana'] - 75
                            else:
                                sp("You fumble and recover but can't attack"'\n')
                        if Battle5 == True:
                            print("Who will you attack?", '\n'
                                "1)", enemy['name'], '\n'
                                "2)", enemy2['name'],'\n'
                                "3)", enemy3['name'], '\n')
                            attack1 = input
                            if attack1 == '1':
                                enemy['hp'] = enemy['hp']-(60+player['intel'],'\n')
                                player['mana'] = player['mana'] - 75
                            elif attack1 == '2':
                                enemy2['hp'] = enemy2['hp']-(60+player['intel'],'\n')
                                player['mana'] = player['mana'] - 75
                            elif attack1 == '3':
                                enemy['hp'] = enemy['hp']-(60+player['intel'],'\n')
                                player['mana'] = player['mana'] - 75
                            else:
                                sp("You fumble and recover but can't attack"'\n')
                    else:
                        sp("You tried to cast but didn't have enough mana"'\n')
                else:
                    sp("You ruffled through your spellbook but couldn't find your spell"'\n')
                
        else:
            sp("You tried to cast but didn't have enough mana"'\n')        
    elif Attack == '4':
        time.sleep(0.01)
        item = input("1) Heal potion 30 hp" '\n'
                        "2) Mana potion 50 mana" '\n'
                        "3) Large health potion 60 hp" '\n'
                        "4) Large mana potion 100 mana" '\n')
        if item == '1':
            if player['healp'] <= 1:
                player['hp'] = player['hp'] + 30
                player['healp'] = player['healp'] - 1
                sp("You gained 30 hp"'\n')
            else:
                sp("You don't have any heal potions"'\n')
        elif item == '2':
            if player['manap'] <= 1:
                player['mana'] = player['mana'] + 50
                player['manap'] = player['manap'] - 1
                sp("You gained 50 mana"'\n')
            else:
                sp("You don't have any mana potions")
        elif item == '3':
            if player['lhealp'] <= 1:
                player['hp'] = player['hp'] + 60
                player['lhealp'] = player['lhealp'] - 1
                sp("You gained 60 hp"'\n')
            else:
                sp("You don't have any large heal potions"'\n')
        elif item == '4':
            if player['lmanap'] <= 1:
                player['mana'] = player['mana'] + 100
                player['lmanap'] = player['lmanap'] - 1
                sp("You gained 100 mana"'\n')
            else:
                sp("You don't have any large mana potions")
        else:
            sp("You fumble and recover but can't attack"'\n')

    elif Attack == '5':
        if player['coins'] >= enemy['coins']+enemy2['coins']+enemy3['coins']:
            print("Are you sure you want to spend", (enemy['coins']+enemy2['coins']+enemy3['coins']),
                        "coins to escape?" '\n'
                        "1) Yes" '\n'
                        "2) No"'\n')
            time.sleep(0.01)
            sure = input()
            if sure == '1':
                player['coins'] = player['coins']-(enemy['coins']+enemy2['coins']+enemy3['coins'])
                enemy['coins'] = 0
                enemy['xp'] = 0
                enemy['hp'] = 0
                enemy2['coins'] = 0
                enemy2['xp'] = 0
                enemy2['hp'] = 0
                enemy3['coins'] = 0
                enemy3['xp'] = 0
                enemy3['hp'] = 0
                win = False
                sp("You have succesfuly escaped!"'\n')
            elif sure == '2':
                sp("You fumble and recover but can't attack"'\n')
            else:
                sp("You fumble and recover but can't attack"'\n')
        else:
            sp("You fumble and recover but can't attack"'\n')
    else:
        sp("You fumble and recover but can't attack"'\n')
    
    if player['hp'] > player['maxhp']:
        player['hp'] = player['maxhp']
    if player['mana'] > player['maxmana']:
        player['mana'] = player['maxmana']
    if enemy['dex'] < 0:
        enemy['dex'] = 0
    if enemy2['dex'] < 0:
        enemy2['dex'] = 0
    if enemy3['dex'] < 0:
        enemy3['dex'] = 0
    if enemy['str'] < 0:
        enemy['str'] = 0
    time.sleep(2)
    
    if enemy['hp'] < 0:
        enemy['hp'] = 0
    if enemy2['hp'] < 0:
        enemy2['hp'] = 0
    if enemy3['hp'] < 0:
        enemy3['hp'] = 0
        
    if enemy['hp'] > 0:
        Battle2 = True
    if enemy2['hp'] > 0:
        Battle2 = True
    if enemy3['hp'] > 0:
        Battle2 = True
    if Battle2 == True:
        if Battle3 == True:
            enemystat1()
            if enemy['type'] == 0:
                print(enemy['name'], "used", enemy['sword'],'\n')
                player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])-enemy['str']-enemy['sdmg']
                time.sleep(1)
                
                if player['hp'] < 1:
                    lose()
                Battle2 = False
            if enemy['type'] == 1:
                
                if enemy['arrows'] > 0:
                    print(enemy['name'], "used", enemy['bow'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])+enemy['dex']+enemy['bdmg']
                else:
                    print(enemy['name'], "used", enemy['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])-enemy['str']-enemy['sdmg']
                time.sleep(1)
                
                if player['hp'] < 1:
                    lose()
                Battle2 = False
        if Battle4 == True:
            enemystat1()
            enemy2stat1()
            if enemy['hp'] > 0:
                if enemy['type'] == 0:
                    print(enemy['name'], "used", enemy['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])+enemy['str']+enemy['sdmg']
                    
                    if player['hp'] < 1:
                        lose()
                    Battle2 = False
                if enemy['type'] == 1:
                    if enemy['arrows'] > 0:
                        print(enemy['name'], "used", enemy['bow'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])+enemy['dex']+enemy['bdmg']
                else:
                    print(enemy['name'], "used", enemy['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])-enemy['str']-enemy['sdmg']
                    
                    if player['hp'] < 1:
                        lose()
                    Battle2 = False
            if enemy2['hp'] > 0:
                if enemy2['type'] == 0:
                    print(enemy2['name'], "used", enemy2['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy2['dmgmin'], enemy2['dmgmax'])+enemy2['str']+enemy2['sdmg']
                    Battle2 = False
                if enemy2['type'] == 1:
                    if enemy2['arrows'] > 0:
                        print(enemy2['name'], "used", enemy2['bow'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])+enemy2['dex']+enemy2['bdmg']
                else:
                    print(enemy2['name'], "used", enemy2['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])-enemy2['str']-enemy2['sdmg']
                    
                if player['hp'] < 1:
                    lose()
                Battle2 = False
        if Battle5 == True:
            enemystat1()
            enemy2stat1()
            enemy3stat1()
            if enemy['hp'] > 0:
                if enemy['type'] == 0:
                    print(enemy['name'], "used", enemy['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])+enemy['str']+enemy['sdmg']
                    
                if player['hp'] < 1:
                    lose()
                    Battle2 = False
                if enemy['type'] == 1:
                    if enemy['arrows'] > 0:
                        print(enemy['name'], "used", enemy['bow'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])+enemy['dex']+enemy['bdmg']
                else:
                    print(enemy['name'], "used", enemy['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy['dmgmin'], enemy['dmgmax'])-enemy['str']-enemy['sdmg']
                    
                if player['hp'] < 1:
                    lose()
                    Battle2 = False
            if enemy2['hp'] > 0:
                if enemy2['type'] == 0:
                    print(enemy2['name'], "used", enemy2['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy2['dmgmin'], enemy2['dmgmax'])+enemy2['str']+enemy2['sdmg']
                    
                    if player['hp'] < 1:
                        lose()
                    Battle2 = False
                if enemy2['type'] == 1:
                    if enemy2['arrows'] > 0:
                        print(enemy2['name'], "used", enemy2['bow'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy2['dmgmin'], enemy2['dmgmax'])+enemy2['dex']+enemy2['bdmg']
                else:
                    print(enemy2['name'], "used", enemy2['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy2['dmgmin'], enemy2['dmgmax'])-enemy2['str']-enemy2['sdmg']
                    
                if player['hp'] < 1:
                    lose()
                    Battle2 = False
            if enemy3['hp'] > 0:
                if enemy3['type'] == 0:
                    print(enemy3['name'], "used", enemy3['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy3['dmgmin'], enemy3['dmgmax'])+enemy3['str']+enemy3['sdmg']
                    time.sleep(1)
                    
                    if player['hp'] < 1:
                        lose()
                    Battle2 = False
                if enemy3['type'] == 1:
                    if enemy3['arrows'] > 0:
                        print(enemy3['name'], "used", enemy3['bow'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy3['dmgmin'], enemy3['dmgmax'])+enemy3['dex']+enemy3['bdmg']
                else:
                    print(enemy3['name'], "used", enemy3['sword'],'\n')
                    player['hp'] = player['hp']-random.randint(enemy3['dmgmin'], enemy3['dmgmax'])-enemy3['str']-enemy3['sdmg']
                    
                if player['hp'] < 1:
                    lose()
        battle()
    else:
        Win()
            
                    
def shop():
    sp("You stuble on a cave and find an old merchant." '\n'
        "Merchant: What would you like to buy?"'\n')
    buy = input("1) Sword" '\n'
                "2) Bow" '\n'
                "3) Spell" '\n'
                "4) Supplies"'\n')
    if buy == '1':
        sword = input("1) Stone sword  20 coins" '\n'
                "2) Iron sword 50 coins" '\n'
                "3) Crystal sword 100 coins" '\n'
                "4) Obsidian sword 500 coins")
        if sword == '1':
            if player['coins'] >= 20:
                if player['sdmg'] == 0:
                    player['coins'] = player['coins'] - 20
                    player['sdmg'] = 2
                    sp("You have bought the stone sword"'\n')
                else:
                    sp("You already have bought this item"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif sword == '2':
            if player['coins'] >= 50:
                if player['sdmg'] <=2:
                    player['coins'] = player['coins'] - 50
                    player['sdmg'] = 5
                    sp("You have bought the iron sword"'\n')
                else:
                    sp("You already have bought this item"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif sword == '3':
            if player['coins'] >= 100:
                if player['sdmg'] <=5:
                    player['coins'] = player['coins'] - 100
                    player['sdmg'] = 10
                    sp("You have bought the crystal sword"'\n')
                else:
                    sp("You already have bought this item"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif sword == '4':
            if player['coins'] >= 500:
                if player['sdmg'] <=10:
                    player['coins'] = player['coins'] - 500
                    player['sdmg'] = 15
                    sp("You have bought the obsidian sword"'\n')
                else:
                    sp("You already have bought this item"'\n')
            else:
                sp("You don't have enough coins"'\n')
        else:
            sp("ERROR")
    elif buy == '2':
        bow = input("1) Stone bow  20 coins" '\n'
                "2) Iron bow 50 coins" '\n'
                "3) Crystal bow 100 coins" '\n'
                "4) Obsidian bow" '\n')
        if bow == '1':
            if player['coins'] >= 20:
                if player['bdmg'] == 0:
                    player['coins'] = player['coins'] - 20
                    player['bdmg'] = 2
                    sp("You have bought the stone bow")
                else:
                    sp("You already have bought this item")
            else:
                sp("You don't have enough coins"'\n')
        elif bow == '2':
            if player['coins'] >= 50:
                if player['bdmg'] <=2:
                    player['coins'] = player['coins'] - 50
                    player['bdmg'] = 5
                    sp("You have bought the iron bow"'\n')
                else:
                    sp("You already have bought this item"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif bow == '3':
            if player['coins'] >= 100:
                if player['bdmg'] <=5:
                    player['coins'] = player['coins'] - 100
                    player['bdmg'] = 10
                    sp("You have bought the crystal bow"'\n')
                else:
                    sp("You already have bought this item"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif bow == '4':
            if player['coins'] >= 500:
                if player['bdmg'] <=10:
                    player['coins'] = player['coins'] - 500
                    player['bdmg'] = 15
                    sp("You have bought the obsidian bow"'\n')
                else:
                    sp("You already have bought this item"'\n')
            else:
                sp("You don't have enough coins"'\n')
        else:
            sp("ERROR")
    elif buy == '3':
        spell = input("1) Fireball  30 coins" '\n'
                "2) Ice wave 40 coins" '\n'
                "3) Weakening curse 150 coins" '\n'
                "4) Withering wind 700 coins" '\n')
        if spell == '1':
            if player['coins'] >= 30:
                if player['spells'] == 0:
                    player['coins'] = player['coins'] - 30
                    player['spells'] = player['spells'] + 1
                    sp("You have bought the fireball"'\n')
                else:
                    sp("You already have bought this item"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif spell == '2':
            if player['coins'] >= 40:
                if player['spells'] > 1:
                    sp("You already have bought this item"'\n')
                else:
                    if player['spells'] == 1:
                        player['coins'] = player['coins'] - 40
                        player['spells'] = player['spells'] + 1
                        sp("You have bought ice wave"'\n')
                    else:
                        sp("You need to buy fireball first")
                
            else:
                sp("You don't have enough coins"'\n')
        elif spell == '3':
            if player['coins'] >= 150:
                if player['spells'] > 2:
                    sp("You already have bought this item"'\n')
                else:
                    if player['spells'] == 2:
                        player['coins'] = player['coins'] - 150
                        player['spells'] = player['spells'] + 1
                        sp("You have bought weakening curse"'\n')
                    else:
                        sp("You need to buy ice wave first")
                
            else:
                sp("You don't have enough coins"'\n')
        elif spell == '4':
            if player['coins'] >= 700:
                if player['spells'] > 3:
                    sp("You already have bought this item"'\n')
                else:
                    if player['spells'] == 3:
                        player['coins'] = player['coins'] - 700
                        player['spells'] = player['spells'] + 1
                        sp("You have bought withering wind"'\n')
                    else:
                        sp("You need to buy weakening curse first")
                
            else:
                sp("You don't have enough coins"'\n')
        else:
            sp("ERROR")
    elif buy == '4':
        supply = input("1) 10 Arrows 20 coins", '\n'
                        "2) Health potion 20 coins", '\n'
                        "3) Mana potion 20 coins"'\n'
                        "4) Large mana potion 60 coins" '\n'
                        "5) Latge health potion 60 coins" '\n')
        if supply == '1':
            if player['coins'] >= 20:
                    player['coins'] = player['coins'] - 20
                    player['arrows'] = player['arrows'] + 10
                    sp("You have bought 10 arrows"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif supply == '2':
            if player['coins'] >= 20:
                    player['coins'] = player['coins'] - 20
                    player['healp'] = player['healp'] + 1
                    sp("You have bought a heal potion"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif supply == '3':
            if player['coins'] >= 20:
                player['coins'] = player['coins'] - 20
                player['healp'] = player['manap'] + 1
                sp("You have bought a mana potion"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif supply == '4':
            if player['coins'] >= 60:
                    player['coins'] = player['coins'] - 60
                    player['lhealp'] = player['lhealp'] + 1
                    sp("You have bought a large heal potion"'\n')
            else:
                sp("You don't have enough coins"'\n')
        elif supply == '5':
            if player['coins'] >= 60:
                player['coins'] = player['coins'] - 60
                player['lhealp'] = player['lmanap'] + 1
                sp("You have bought a large mana potion"'\n')
            else:
                sp("You don't have enough coins"'\n')
        else:
            sp("ERROR")
    else:
        sp("Merchant: What?")
    continues = input("Merchant: Would you like to buy anything else?" '\n'
                        "1) Yes" '\n'
                        "2) No"'\n')
    if continues == '1':
        shop()
    else:
        progress()         
           
os.system('cls')

sp("This is just a demo version of the game. \n")

    
sp("For the full game, please contact the game coder (Tristan Clendenen) for pricing.")


loading()
time.sleep(1)
os.system('cls')
player['name'] = input("Welcome adveturer!" '\n'
             "Before we start, please, tell us your name."'\n')
time.sleep(3)
Loading()
game = input("Would you like to play?" '\n')
if game == 'Yes':
    Game = True
    time.sleep(1)
    loading()
elif game == 'No':
    sp("Well I don't care and we will begin anyways.")
    Game = True
    time.sleep(1)
    loading()
elif game == 'UUDDLRLRBA':
    sp("Testing mode")
    time.sleep(3)
    Loading()
    player['xp'] = 250
    level()
    time.sleep(5)
    loading()
    Game = True
    time.sleep(3)
else:
    sp("I'm not sure what you said but we are going to start anyways")
    Game = True
    loading()
while Game == True:
    os.system('cls')
    sp("You walk down into the dungion. Exiled from the kingdom of your birth, you were told to never come up until" '\n'
        "you killed the mithicle beast that's name was forbbiden. With only crude weapons made of wood, you must go through the dungion," '\n'
        "slay the beast, and come back with proof of your victory. But while you walk down you hear a scratching of claws and stone," '\n'
        "and soon realise that you can't just walk to the beast without a fight...")
    imp1()
    Battle3 = True
    battle()
    if win == True:
        Game1 = True
        while Game1 == True:
            progress()
            sp("After being shooken up by an unexpected attack by an imp, you know that this is going to be a long trip." '\n'
            "So you continue to walk down deeper into the damp dungion. The sight of human skeletons litering the floor is disturbing," '\n'
            "but even though every twist and turn takes you deeper into the dungion, it's the chance you have to survive." '\n'
            "The entire point of this was just a way for the king to look more moral towards his people. But if you stop and think," '\n'
            "this is less moral than strait execution, no person has ever made it back alive with proof of the killed beast," '\n'
            "but that is the point, it's an execution that no one sees but the person who gets exectued. Lost in your own thought," '\n'
            "you don't see the spider's web until you feel it touch your skin.")
            spider1()
            Battle3 = True
            battle()