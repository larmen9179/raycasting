import numpy as np
from matplotlib import pyplot as plt
import keyboard

size = 15
map = [[list(np.random.uniform(0, 1, 3))] * size for i in range(size)]
for i in range(size - 2):
    for j in range(size - 2):
        if np.random.uniform() > .33:
            map[i + 1][j + 1] = 0

posx, posy = (1, np.random.randint(1, size - 1))
rot = np.pi/4

x, y = (posx, posy)
map[x][y] = 0

count = 0
while True:
    testx, testy = (x, y)
    if np.random.uniform() > 0.5:
        testx = testx + np.random.choice([-1, 1])
    else:
        testy = testy + np.random.choice([-1, 1])
    if testx > 0 and testx < size - 1 and testy > 0 and testy < size - 1:
        if map[testx][testy] == 0 or count > 5:
            count = 0
            x, y = (testx, testy)
            map[x][y] = 0
            if x == size - 2:
                exitx, exity = (x, y)
                break
        else:
            count = count = 1

while True:

    plt.hlines(-.6, 0, 60, colors='gray', lw=165, alpha=.5)
    plt.hlines(.6, 0, 60, colors='lightblue', lw=165, alpha=.5)
    tilex, tiley, tilec = ([], [], [])


    for i in range(60):
        rot_i = rot + np.deg2rad(i - 30)
        x, y = (posx, posy)
        n = 0
        while True:
            xx, yy = (x, y)
            x, y = (x + .02 * np.cos(rot_i), y + .02 * np.sin(rot_i))
            n = n + 1
            
            if abs(int(3*xx)-int(3*x)) > 0 or abs(int(3*yy)-int(3*y)) > 0:
                tilex.append(i)
                tiley.append(-1/np.sqrt((x-posx)**2 + (y-posy) ** 2) + .0001)
                if int(x) == exitx and int(y) == exity:
                    tilec.append('b')
                else:
                    tilec.append('k')

            if map[int(x)][int(y)] != 0:
                dist = np.sqrt((x-posx)**2 + (y-posy)**2)
                h = 1/(dist+.00001)
                c = np.asarray(map[int(x)][int(y)]) * (.3 + .7/(dist**2 + 1))
                break
    
        plt.vlines(i, -h, h, lw = 8, colors = c)

    plt.scatter(tilex, tiley, c=tilec)

    plt.axis("off"); plt.tight_layout(); plt.axis([0, 60, -1, 1])
    plt.draw(); plt.pause(0.0001); plt.clf()

    key = keyboard.read_key()
    x, y = (posx, posy)

    if key == 'up':
        x, y = (x + .3*np.cos(rot), y + .3*np.sin(rot))
    elif key == 'down':
        x, y = (x - .3*np.cos(rot), y - .3*np.sin(rot))
    elif key == 'left':
        rot = rot - np.pi/8
    elif key == 'right':
        rot = rot + np.pi/8
    elif key == "esc":
        break

    if map[int(x)][int(y)] == 0:
        if int(posx) == exitx and int(posy) == exity:
            break
        posx, posy = (x, y)
        

plt.close()