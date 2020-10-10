import pygame as py
import sys
import random


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, opponent_speed, player_speed, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        score_time = py.time.get_ticks()

    if ball.right >= screen_width:
        opponent_score += 1
        opponent_speed += 2
        score_time = py.time.get_ticks()

    if ball.colliderect(player):
        ball_speed_x *= -1

    if ball.colliderect(player):
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
    global score_time, basic_font

    ball.center = (screen_width / 2, screen_height / 2)
    current_time = py.time.get_ticks()
    ball_speed_x = 7
    ball_speed_y = 7

    if current_time - score_time < 600:
        number_three = basic_font.render("3", False, (200, 200, 200))
        screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 600 < current_time - score_time < 1200:
        number_two = basic_font.render("2", False, (200, 200, 200))
        screen.blit(number_two, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 1200 < current_time - score_time < 1800:
        number_one = basic_font.render("1", False, (200, 200, 200))
        screen.blit(number_one, (screen_width / 2 - 10, screen_height / 2 + 20))

    if current_time - score_time < 1800:
        ball_speed_y, ball_speed_x = 0, 0
    else:
        ball_speed_x = ball_speed_x * random.choice((1, -1))
        ball_speed_y = ball_speed_y * random.choice((1, -1))
        score_time = None
        ball_speed_x += 1
        ball_speed_y += 1
        return ball_speed_x
        return ball_speed_y

py.init()
clock = py.time.Clock()

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 6
screen_width = 1028
screen_height = 760
bg_color = py.Color("grey12")
light_gray = (200, 200, 200)
player_score = 0
opponent_score = 0
game_font = py.font.Font('freesansbold.ttf', 32)
basic_font = game_font

score_time = True

screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption('Pong')

ball = py.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = py.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = py.Rect(10, screen_height / 2 - 70, 10, 140)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

        if event.type == py.KEYDOWN:
            if event.key == py.K_DOWN:
                player_speed += 8
            if event.key == py.K_UP:
                player_speed -= 8
        if event.type == py.KEYUP:
            if event.key == py.K_DOWN:
                player_speed -= 8
            if event.key == py.K_UP:
                player_speed += 8

    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill(bg_color)
    py.draw.rect(screen, light_gray, player)
    py.draw.rect(screen, light_gray, opponent)
    py.draw.ellipse(screen, light_gray, ball)
    py.draw.aaline(screen, light_gray, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if score_time:
        ball_restart()

    player_text = game_font.render(f'{player_score}', False, light_gray)
    screen.blit(player_text, (screen_width / 2 + 80, screen_height / 2))

    opponent_text = game_font.render(f'{opponent_score}', False, light_gray)
    screen.blit(opponent_text, (screen_width / 2 - 100, screen_height / 2))

    py.display.flip()
    clock.tick(60)
