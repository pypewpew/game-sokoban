import pew


pew.init()
screen = pew.Pix.from_iter((
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 3, 1, 0, 0, 0, 1),
    (1, 0, 0, 1, 0, 1, 1, 1),
    (1, 0, 0, 3, 0, 2, 0, 1),
    (1, 0, 2, 1, 0, 1, 0, 1),
    (1, 0, 0, 0, 0, 1, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
))
x = 1
y = 1
blink = 1
last = screen.pixel(x, y)

while True:
    screen.pixel(x, y, last)
    pressed = pew.keys()
    dx = 0
    dy = 0
    if pressed & pew.K_UP:
        dy = -1
    elif pressed & pew.K_DOWN:
        dy = 1
    elif pressed & pew.K_LEFT:
        dx = -1
    elif pressed & pew.K_RIGHT:
        dx = 1
    if screen.pixel(x + dx, y + dy) in {0, 2}:
        x += dx
        y += dy
    elif screen.pixel(x + dx, y + dy) == 3:
        if screen.pixel(x + dx + dx, y + dy + dy) == 1:
            pass
        else:
            if screen.pixel(x + dx + dx, y + dy + dy) == 2:
                screen.pixel(x + dx + dx, y + dy + dy, 1)
            else:
                screen.pixel(x + dx + dx, y + dy + dy, 3)
            screen.pixel(x + + dx, y + dy, 0)
            x += dx
            y += dy
    last = screen.pixel(x, y)
    for a in range(8):
        for b in range(8):
            if screen.pixel(a, b) == 2:
                break
        else:
            continue
        break
    else:
        break
    screen.pixel(x, y, 2 + blink)
    blink = 0 if blink else 1
    pew.show(screen)
    pew.tick(1 / 6)
