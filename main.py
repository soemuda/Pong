import pygame as py
import sys
import random

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

py.init()
clock = py.time.Clock()

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7
screen_width = 1028
screen_height = 760
bg_color = py.Color("grey12")
light_gray = (200, 200, 200)


screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption('Pong')

ball = py.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = py.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = py.Rect(10, screen_height/2 - 70, 10, 140)


while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit

        if event.type == py.KEYDOWN:
            if event.key == py.K_DOWN:
                player_speed += 7
            if event.key == py.K_UP:
                player_speed -= 7
        if event.type == py.KEYUP:
            if event.key == py.K_DOWN:
                player_speed -= 7
            if event.key == py.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill(bg_color)
    py.draw.rect(screen, light_gray, player)
    py.draw.rect(screen, light_gray, opponent)
    py.draw.ellipse(screen, light_gray, ball)
    py.draw.aaline(screen, light_gray, (screen_width/2, 0), (screen_width/2, screen_height))



    py.display.flip()
    clock.tick(60)