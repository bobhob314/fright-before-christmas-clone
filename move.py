import pyglet # necessary?
import math # necessary?
import const
import time

################################################################################
# All movement should be assuming the bottom of the screen is 60 above the
# actual bottom (720-60=660)
################################################################################
#This function in test.py too
def get_time():
    return int(round(time.time() * 1000))

def move_enemy(enemy):
    if get_time() - enemy.freeze_time < 2000: # FREEZE TIME IS 2000 MS
        return
    enemy.x += enemy.vel_x # technically kinda pointless
    enemy.y += enemy.vel_y # this too
    enemy.sprite.x += enemy.vel_x
    enemy.sprite.y += enemy.vel_y


################################################################################
# Current sketchiness level: 3/10
################################################################################
def move_enemy_line(enemy):
    # proximity
    HALF_WIDTH = const.WINDOW_WIDTH/2 - enemy.width/2
    if const.in_safe_space(enemy.x, enemy.y, enemy.width):
        enemy.vel_x = 0
        enemy.vel_y = 0

    elif enemy.x == HALF_WIDTH:
        enemy.vel_y = -enemy.max_speed
        enemy.vel_x = 0
    elif enemy.y <= const.BOTTOM_BORDER:
        enemy.vel_y = 0
        if enemy.x < HALF_WIDTH:
            enemy.vel_x = enemy.max_speed
        elif enemy.x > HALF_WIDTH:
            enemy.vel_x = -enemy.max_speed
    else:
        #print(enemy.x, enemy.y)
        slope = (enemy.y - const.BOTTOM_BORDER)/(enemy.x - HALF_WIDTH)
        tan_of_theta = 1/slope
        radians = math.atan(tan_of_theta)
        enemy.vel_y = -math.cos(radians)*enemy.max_speed
        enemy.vel_x = -math.sin(radians)*enemy.max_speed
        degrees = radians * 180.0 / math.pi

def move_enemy_hori(enemy):
    # movement is fucked
    if const.HORI_LEFT <= enemy.x <= const.HORI_RIGHT:
        enemy.vel_x = 0
    elif enemy.x < 540:
        enemy.vel_x = enemy.max_speed
    else:
        enemy.vel_x = -enemy.max_speed
    enemy.vel_y = 0
