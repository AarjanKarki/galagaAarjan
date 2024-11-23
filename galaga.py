import pgzrun, random
WIDTH=500
HEIGHT=500

game_over=False
score=0
galaga=Actor('galaga')
galaga.pos=(WIDTH//2, HEIGHT-60)
bullets=[]
speed=5
enemies=[]
for x in range(8):
    for y in range(4):
        enemies.append(Actor('bug'))
        enemies[-1].x=100+ 50*x
        enemies[-1].y=80 + 50*y

def draw():
    screen.clear()
    screen.fill('blue')
    for bullet in bullets:
        bullet.draw()
    galaga.draw()
    for enemy in enemies:
        enemy.y+=2
        if enemy.y>HEIGHT:
            enemy.y=-100
    enemy.draw()
    screen.draw.text(score)

def update():
    if keyboard.left:
        galaga.x-=2
        if galaga.x<0:
            galaga.x=10
    if keyboard.right:
        galaga.x+=2
        if galaga.x>WIDTH:
            galaga.x=WIDTH-10
    for bullet in bullets:
        bullet.y-=10
    if enemy.colliderect(bullet):
        score+=1


def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x=galaga.x
        bullets[-1].y=galaga.y-20




pgzrun.go()
