import random

from PIL import ImageColor
from pygame import display
from pygame import draw
from pygame import event
from pygame import font
from pygame import init
from pygame import K_DOWN
from pygame import K_l
from pygame import K_LEFT
from pygame import K_p
from pygame import K_RIGHT
from pygame import K_UP
from pygame import KEYDOWN
from pygame import QUIT
from pygame import quit as pyquit
from pygame import time as pytime

init()

white = ImageColor.getrgb("white")
red = ImageColor.getrgb("red")
blue = ImageColor.getrgb("blue")
black = ImageColor.getrgb("black")

width = 600
height = 600

snake_body = 10


dis = display.set_mode((width, height))
display.set_caption("Crossing the Road")

clock = pytime.Clock()

score = lambda s: dis.blit(
    font.SysFont("arial.ttf", 35).render(f"Score: {s-1}", True, blue), [0, 0]
)

message = lambda message, color, pos: dis.blit(
    font.SysFont("Segoe UI", 25).render(message, True, color), pos
)

create_enemy = lambda space, pos: round(random.randrange(space, pos - 10) / 10) * 10


def game():
    game_over = False
    close = False

    level = 10

    body = []
    size = 2

    x1 = width / 2
    y1 = height / 2

    x_enemy = create_enemy(0, width)
    y_enemy = create_enemy(30, height)

    x1_change = 0
    y1_change = 0

    while not game_over:
        while close:
            dis.fill(white)
            message("Game Over", red, [250, 60])
            message(
                "Press 'P' to play again or 'L' to leave the game.", black, [50, 100]
            )
            display.update()
            events_list = event.get()

            for e in events_list:
                if e.type == KEYDOWN:
                    if e.key == QUIT:
                        game_over = True
                        close = False

                    if e.key == K_l:
                        game_over = True
                        close = False

                    if e.key == K_p:
                        game()

        events_list = event.get()

        for e in events_list:

            if e.type == QUIT:
                game_over = True

            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    x1_change = -snake_body
                    y1_change = 0

                elif e.key == K_RIGHT:
                    x1_change = snake_body
                    y1_change = 0

                elif e.key == K_UP:
                    x1_change = 0
                    y1_change = -snake_body

                elif e.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake_body

        if any([x1 >= width, x1 < 0, y1 >= height, y1 < 0]):
            close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(white)
        draw.rect(dis, red, [x_enemy, y_enemy, snake_body, snake_body])

        head = []
        head.append(x1)
        head.append(y1)

        body.append(head)
        if len(body) > size:
            del body[0]

        [draw.rect(dis, red, [x[0], x[1], snake_body, snake_body]) for x in body]
        score(size)

        display.update()

        if x1 == x_enemy and y1 == y_enemy:
            x_enemy = create_enemy(0, width)
            y_enemy = create_enemy(30, height)
            size += 1
            level += 5
        clock.tick(level)

    pyquit()
    quit()


game()
