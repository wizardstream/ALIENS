import pgzrun
import sys
from random import *
import time
mod = sys.modules['__main__']

TITLE = "ALIENS..."
WIDTH = 1000
HEIGHT = 1000
FONT = 'calibri'

IMG_PREFIX = "player"

k = True
in_house = False
start1 = True
start2 = False
game_over = True

start_delay = 2

# a counter to delay between changes
delay_timer = 0
# which of the 3 images to display (value from 1 to 3)
image_number = 1


player = mod.Actor(IMG_PREFIX+"-down-1")
house = mod.Actor('houseoverworldbig')
stairs = mod.Actor('stairs')
speach = mod.Actor('dialoguebox')
arrow = mod.Actor('smallarrow')
sword = mod.Actor('sword2')
player.x = 100
player.y = 100

def place_actors():
    player.x = randint(40, 300)
    player.y = randint(40, 300)


    house.x = 500
    house.y = 500

    stairs.pos = 500, 850

    speach.pos = 500, 100

    arrow.pos = 450, 850

    sword.pos = 500, 400



def start_music():
    mod.music.play('background')

def stop_music():
    mod.music.stop()

def kai():
    global k
    k = False

def update():
    global delay_timer, image_number
    global in_house, playerTouchingHouse, touchingStairs
    playerTouchingHouse = player.colliderect(house)
    if playerTouchingHouse and mod.keyboard.space:
        in_house = True

    touchingStairs = player.colliderect(stairs)
    if touchingStairs and in_house:
        player.pos = 500, 520
        in_house = False

    direction = "none"
    if mod.keyboard.a or mod.keyboard.left:
        player.x -= 3
        direction = "left"
    if mod.keyboard.d or mod.keyboard.right:
        player.x += 3
        direction = "right"
    if mod.keyboard.s or mod.keyboard.down:
        player.y += 3
        direction = "down"
    if mod.keyboard.w or mod.keyboard.up:
        player.y -= 3
        direction = "up"

    # Only move whilst key is pressed
    if (delay_timer == 10):
        delay_timer = 0

        if (direction != 'none'):
            image_number += 1
            if (image_number > 2):
                image_number = 1
    else:
        delay_timer += 1

    if (direction != 'none'):
        image_name = "{}-{}-{}".format(IMG_PREFIX, direction, image_number)
        player.image = image_name


def nextStart1():
    global start1, start2
    if start1:
        start1 = False
        start2 = True

def nextStart2():
    global start1, start2
    if start2:
        start1 = False
        start2 = False

def draw():
    global start1, start2
    global game_over, playerTouchingHouse, in_house
    mod.screen.clear()

    if start1:
        mod.screen.fill((0, 0, 0))
        mod.screen.draw.text('K-NOX GAMES PRESENTS:', (250, 400), fontsize=64, color="green", background="orange", fontname=FONT)
        mod.clock.schedule(nextStart1, start_delay)
    elif start2:
        mod.screen.fill((0, 0, 0))
        mod.screen.draw.text('ALIENS', (400, 400),  fontsize=64, color='green', background="orange", fontname=FONT)
        mod.clock.schedule(nextStart2, start_delay)
    else:
        mod.screen.fill((4, 139, 87))
        start1 = False
        start2 = False
        game_over = False

    if not game_over and not playerTouchingHouse:
        mod.screen.fill((4, 139, 87))
        mod.screen.draw.text('x: ' + str(player.x), (40, 40), fontname=FONT)
        mod.screen.draw.text('y: ' + str(player.y), (40, 60), fontname=FONT)

        house.draw()
        player.draw()

    if not game_over and playerTouchingHouse:
        house.draw()
        player.draw()
        mod.screen.draw.text('x: ' + str(player.x), (40, 40), fontname=FONT)
        mod.screen.draw.text('y: ' + str(player.y), (40, 60), fontname=FONT)
        mod.screen.draw.text('SPACE TO OPEN DOOR', (40, 80), fontname=FONT)

    if not game_over and in_house:
        mod.screen.fill((165, 42, 42))
        stairs.draw()
        arrow.draw()
        sword.draw()
        player.draw()
        speach.draw()
        mod.screen.draw.text('YOU ARE IN THE CASTLE.', (400, 100), fontsize=20, color='green', fontname=FONT)

        mod.clock.schedule(kai, 1)
        mod.screen.draw.text('x: ' + str(player.x), (40, 40), fontname=FONT)
        mod.screen.draw.text('y: ' + str(player.y), (40, 60), fontname=FONT)



    if player.x == 500 and player.y == 500:
        mod.clock.schedule(stop_music, 0.1)

start_music()
place_actors()
pgzrun.go()