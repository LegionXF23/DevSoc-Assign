import pygame,sys,random

def ball_anim():
    global ballspeedx,ballspeedy
    ball.x += ballspeedx
    ball.y += ballspeedy

    if ball.top <= 0 or ball.bottom >= screen_height:
        ballspeedy *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ballrestart()

    if ball.colliderect(player) or ball.colliderect(opp):
        ballspeedx *= -1

def player_anim():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opp_anim():
    if opp.top < ball.y:
        opp.top += opp_speed
    if opp.bottom > ball.y:
        opp.bottom -= opp_speed
    if opp.top <= 0:
        opp.top = 0
    if opp.bottom >= screen_height:
        opp.bottom = screen_height

def ballrestart():
    global ballspeedx,ballspeedy
    ball.center =  (screen_width/2,screen_height/2)
    ballspeedy *= random.choice((1,-1))
    ballspeedx *= random.choice((1,-1))

pygame.init
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

ball = pygame.Rect(screen_width/2-15, screen_height/2-15,30,30)
player = pygame.Rect(screen_width-20, screen_height/2-70,10,140)
opp = pygame.Rect(10, screen_height/2-70,10,140)

bgc = pygame.Color('grey12')
lightgrey = (200,200,200)

ballspeedx = 7 * random.choice((1,-1))
ballspeedy = 7 * random.choice((1,-1))
player_speed = 0
opp_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_anim()
    player.y += player_speed

    player_anim()
    opp_anim()
    screen.fill(bgc)
    pygame.draw.rect(screen,lightgrey,player)
    pygame.draw.rect(screen,lightgrey,opp)
    pygame.draw.ellipse(screen,lightgrey,ball)
    pygame.draw.aaline(screen,lightgrey,(screen_width/2,0),(screen_width/2,screen_height))

    pygame.display.flip()
    clock.tick(60)