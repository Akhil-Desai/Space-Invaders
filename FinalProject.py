#Dhyaaneshvaran Ravichandran, dxv9ym
#Akhil Desai, wyd7mz

"""
This game will be a "space invaders" like game in which enemies will fall from the sky along with coins
To stay alive, players must shoot the enemies by holding the space button which shoots lazers that kill enemies and cause them to spawn in a different position
A timer to see how long the player lasts is there and the objective is to get the highest time without losing all your lives
When an enemy touches the character, the character loses a life
Characters can collect coins that also drop from the sky to increase their time of being alive

Basic Features:
User Input- For this game, the user uses the right and left arrows to move the character left and right, and holds the space button to shoot at enemies
Game Over- If the user runs out of all 3 lives, the game will end and a game over screen will appear. Players lose lives when enemies touch the starship
Graphics/Images- We have a starship and enemies that are images, and the healthbar and gameover screen are images are images as well

Additional Features:
Enemies- This game has enemies that fall from the top of the screen, and the character has to shoot them
Collectibles- This game contains coins that fall from the top of the screen that increases their survived time by 3 seconds if collected
Timer- This game has a timer that counts up, and the main objective is to survive for as long as you can
Health Bar- This game has a health bar that is graphical and it displays different levels of health
"""

import uvage
import random

def setup():
    """
    return: Does not return anything, this function sets up all of our elements for the game including the character, healthbar, background, timer, enemies, and the lazer
    """
    global camera, character, spawn, enemies, game_on, game_over, background, walls, enemyMake, xpos, ypos, lazer, time, lazers, health, coin, coins, time, timerdisplay, health, healthbar1, healthbar2, healthbar3, gameover_screen, go_screen

    enemyMake = True
    camera = uvage.Camera(800,600)

    character = uvage.from_image(400,550, 'character.png')
    character.scale_by(0.09)

    xpos = character.x
    ypos = character.y - 30
    lazer = uvage.from_image(xpos, ypos, 'laser.png.jpeg')
    lazer.scale_by(0.05)
    lazers = []

    enemies = []
    spawn = random.randint(1,800)
    enemy = uvage.from_image(spawn, 50, 'enemy.png')
    enemy_speed = 0
    enemy.yspeed = enemy_speed
    enemy.xspeed = enemy_speed

    coins = []
    coin = uvage.from_image(spawn, 25, 'coins.png')
    coin.scale_by(0.2)


    game_on = False
    game_over = False

    character_speed = 0
    character.xspeed = character_speed
    character.yspeed = character_speed
 
    backdrop = uvage.from_image(400,300, 'deathstar.gif')
    background = [backdrop]

    gameover_screen = uvage.from_image(400,400, 'gameover.jpg')
    go_screen = [gameover_screen]

    healthbar3 = uvage.from_image(625, 50, 'healthbar3.png')
    healthbar3.scale_by(0.5)
    healthbar2 = uvage.from_image(625, 50, 'healthbar2.png')
    healthbar2.scale_by(0.5)
    healthbar1 = uvage.from_image(625, 50, 'healthbar1.png')
    healthbar1.scale_by(0.5)

    walls = [
    uvage.from_color(0, 300, "black", 25, 600),
    uvage.from_color(800, 300, "black", 25, 800),
    uvage.from_color(400, 600, 'black', 800, 25),
    uvage.from_color(400, 0, 'black', 800, 25)
    ]

    time = 0
    timerdisplay = uvage.from_text(400, 500, str(time), 50, 'red', True)
    
    health = 3

def shooting():
    """
    return: Does not return anything, this function sets up shooting the lazer for when the space button is being held 
    """
    global character,lazer, xpos, ypos, enemies, lazers

    
    if uvage.is_pressing('space'):
        camera.draw(lazer)    
        lazer.y -= 50
        if lazer.y < -1:
             lazer.y = ypos
             lazer.x = character.x

    for e in enemies:
        if lazer.top_touches(e):
            enemies.remove(e)
            lazer.y = ypos
            lazer.x = character.x
    
def healthbar():
    """
    return: Does not return anything, this function draws the healthbar based on what number the health is at
    """
    global camera, character, spawn, enemies, game_on, game_over, background, walls, enemyMake, health, score, healthbar1, healthbar2, healthbar3
    if health == 3:
        camera.draw(healthbar3)
    elif health == 2:
        camera.draw(healthbar2)
    elif health == 1:
        camera.draw(healthbar1)
    elif health == 0:
        game_over = True

       

def enemy_attributes():
    """
    return: This function sets up all necessary attributes for the enemies including setting them up, moving them down, and making them dissapear if shot
    """
    global camera, character, spawn, enemies, game_on, game_over, background, walls, enemyMake, health

    spawnx = random.randint(50,750)
    spawny = random.randint(0,100)
    enemy = uvage.from_image(spawnx, spawny, 'enemy.png')
    enemy.scale_by(0.2)
    enemies.append(enemy)

    count = 0

    for e in enemies:
        if enemyMake == True:
            camera.draw(e)
            count += 1
        if count == 5:
            break
        if lazer.top_touches(e):
            enemies.remove(e)
        if e.touches(character):
            health -= 1
            enemies.remove(e)
        
    for i in walls:
        camera.draw(i)
    
    for e in enemies:
        for w in walls:
            if e.bottom_touches(w):
               e.x = spawnx
               e.y = spawny
               
            


def spawn_coins():
    """
    return: Does not return anything, this function sets up the coins and allows players to collect them
    """
    global camera, character, spawn, enemies, game_on, game_over, background, walls, enemyMake, xpos, ypos, lazer, time, lazers, health, coin, coins

    spawnx = random.randint(20,790)
    spawny = random.randint(0,100)

    coin = uvage.from_image(spawnx, spawny, 'coins.png')
    coin.scale_by(0.03)
    coins.append(coin)

    count = 0
    for c in coins:
        camera.draw(c)
        count += 1
        if count == 5:
            break
        if c.touches(character):
            coins.remove(c)
            time += 3
    
    for i in coins:
        for w in walls:
            if i.bottom_touches(w):
               i.x = spawnx
               i.y = spawny

    
    
def clock():
    """
    return: Does not return anything, this function sets up the timer so that it displays and allows a player to see how long they've lasted in the game
    """
    global camera, character, spawn, enemies, game_on, game_over, background, walls, enemyMake, xpos, ypos, lazer, time, lazers, health, coin, coins, time, timerdisplay

    time = 0
    timerdisplay = uvage.from_text(400, 500, str(time), 50, 'red', True)

    camera.draw(timerdisplay)



def handlexmovement():
    """
    return: Does not return anything, this function handles the x position movements for the different elements
    """
    global camera, character, spawn, enemies, game_on, game_over, background, walls, enemyMake

    if uvage.is_pressing('right arrow'):
        character.x += 5
    if uvage.is_pressing('left arrow'):
        character.x -= 5

    for w in walls:
        if character.left_touches(w):
            character.move_to_stop_overlapping(w)
        if character.right_touches(w):
            character.move_to_stop_overlapping(w)

def handleymovement():
    """
    return: This function handles the y position movements for the different elements
    """
    global camera, character, spawn, enemies, game_on, game_over, background, walls, enemyMake, coins
    
    for e in enemies:
        e.y += 1.5

    for c in coins:
        c.y += 1
    
    

def draw():
    """
    return: This function draws the background and the walls as well as the character
    """
    global camera, character, spawn, enemies, game_on, game_over, background, walls, enemyMake
    for item in background:
        camera.draw(item)
    for i in walls:
        camera.draw(i)
    
    camera.draw(character)
       

def tick():
    """
    return: if game_over is True, then then the game over screen is displayed, however, if game_over is false, the function calls all necessary functions to play the game
    """
    global camera, character, spawn, enemies, game_on, game_over, background, walls, enemyMake, lazer, xpos, ypos, time, timerdisplay, go_screen, gameover_screen

    if game_over == True:
        camera.display()
        for item in go_screen:
            camera.draw(item)
        camera.draw(uvage.from_text(400, 50, 'Time Survived: ' + str(int(time)) + 's', 50, 'white'))
    else:
        handlexmovement()
        handleymovement()
        draw()
        healthbar()
        enemy_attributes()
        spawn_coins()
        shooting()
        
        time += 1/30
        time_display = uvage.from_text(50, 50, str(int(time)), 50, "grey", bold = False, italic= True)
        camera.draw(time_display)
        camera.display()


setup()
uvage.timer_loop(30, tick)
    
    