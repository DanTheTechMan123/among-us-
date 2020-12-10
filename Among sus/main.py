import pygame
import tkinter as tk

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption('Among us')
right_run = [pygame.image.load("images/r1.png"), pygame.image.load("images/r2.png"), pygame.image.load("images/r3.png"), pygame.image.load("images/r4.png")]
left_run = [pygame.image.load("images/l1.png"), pygame.image.load("images/l2.png"), pygame.image.load("images/l3.png"), pygame.image.load("images/l4.png")]
idler = pygame.image.load("images/idler.png")
idlel = pygame.image.load("images/idlel.png")
bg = pygame.image.load("images/bg.png")
task_complete = pygame.image.load("images/tc.png")
button_use = pygame.image.load("images/Use.png")
walking = pygame.mixer.Sound("Sounds/walk.wav")
comsound = pygame.mixer.Sound("Sounds/TC.wav")
fail = pygame.mixer.Sound("Sounds/Fail.wav")
victory = pygame.image.load("images/vic.png")
vroy = pygame.mixer.Sound("Sounds/vroy.wav")
title = pygame.image.load("images/title.png")
window = pygame.display.set_mode((500, 500))
pygame.mouse.set_visible(True)

mousex = 0
mousey = 0
tasks_complete = [False] * 5
bgx = -1000
bgy = -100
ins = True
run = False
is_button = False
timer = 0
tc = False
myfont = pygame.font.SysFont('Comic Sans MS', 20)
global is_clicked
while ins:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if keys[pygame.K_1]:
        ins = False
        run = True
    window.blit(title, (0, 0))
    pygame.display.update()

def gameloop():
    window.blit(bg, (bgx, bgy))
    if is_button == True:
        window.blit(button_use, (436, 420))
    else:
        pass
    if player1.isRight == True:
        if player1.move == True:
            pygame.mixer.Sound.play(walking)
            window.blit(right_run[player1.walkcount%4], (player1.x,player1.y))
        else:
            pygame.mixer.Sound.stop(walking)
            window.blit(idler, (player1.x,player1.y))
    elif player1.isLeft == True:
        if player1.move == True:
            pygame.mixer.Sound.play(walking)
            window.blit(left_run[player1.walkcount%4], (player1.x,player1.y))
        else:
            pygame.mixer.Sound.stop(walking)
            window.blit(idlel, (player1.x,player1.y))
    if tc == True:
        window.blit(task_complete, (175, 175))
    else:
        pass
    textsurface = myfont.render("Tasks Complete: " + str(tasks_complete.count(True)) + "/5", False, (255,255,0))
    window.blit(textsurface, (0, 0))
    pygame.display.update()

class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isRight = True
        self.isLeft = False
        self.move = False
        self.jumpCount = 10
        self.walkcount = 0
        self.dir = 1

def tasks(label, c1, c2, ans):
    tasks.is_complete = False
    def check():
        answer = task_entry.get()
        if answer == ans:
            task.destroy()
            tasks.is_complete = True
        else:
            pygame.mixer.Sound.play(fail)

    def close():
        task.destroy()

    task = tk.Tk()
    task.title("Task")
    task.configure(width=200, height=200)
    task_title = tk.Label(task, text=label)
    task_title.pack(side="top", pady=10)
    task_content = tk.Label(task,
                            text=c1)
    task_content.pack(side="top", pady=0)
    task_content2 = tk.Label(task,
                             text=c2)
    task_content2.pack(side="top", pady=0)
    task_entry = tk.Entry(task)
    task_entry.pack(side="top", pady=10)
    button = tk.Button(task, text="Submit", command=check)
    button.pack(side="top", pady=10)
    task.protocol("WM_DELETE_WINDOW", close)
    task.mainloop()

player1 = player(200,200,100,100)

while run:
    pygame.time.delay(50)
    is_clicked = False
    mousex, mousey = pygame.mouse.get_pos()
    timer += 50
    if timer%500 == 0:
        tc = False
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mousex >= 426 and mousex <= 500:
                if mousey >= 420 and mousey <= 500:
                    is_clicked = True
                    pygame.time.delay(500)
        if event.type == pygame.QUIT:
            pygame.quit()
    if keys[pygame.K_LEFT]:
        player1.isLeft = True
        player1.isRight = False
        player1.move = True
        if timer%250 == 0:
            player1.walkcount += 1
        dir = 1
        if bgx >= 100:
            pass
        else:
            bgx += 20 * dir
    elif keys[pygame.K_RIGHT]:
        player1.isRight = True
        player1.isLeft = False
        player1.move = True
        if timer%250 == 0:
            player1.walkcount += 1
        dir = -1
        if bgx <= -3000:
            pass
        else:
            bgx += 20 * dir
    elif keys[pygame.K_UP]:
        player1.move = True
        if timer%250 == 0:
            player1.walkcount += 1
        dir = 1
        if bgy >= 0:
            pass
        else:
            bgy += 20 * dir
    elif keys[pygame.K_DOWN]:
        player1.move = True
        if timer%250 == 0:
            player1.walkcount += 1
        dir = -1
        if bgy <= -1924:
            pass
        else:
            bgy += 20 * dir
    else:
        player1.move = False
    if bgx <= - 2140 and bgx >= - 2340:
        if bgy <= -1020 and bgy >= - 1220:
            is_button = True
            if is_clicked == True:
                is_clicked = False
                tasks("Fill in the blank (hint: you want temperature to be equal): "
                     ,"if temperature _______ 100:\n\tprint(\"Task completed\")",
                     "else:\t\t\t\n\tprint(\"task not completed\")","==")
                if tasks.is_complete == True:
                    tc = True
                    tasks_complete[0] = True
                    pygame.mixer.Sound.play(comsound)
                else:
                    pass
                tasks.is_complete = False
        else:
            is_button = False
    elif bgx <= -520  and bgx >= - 720:
        if bgy <= -1600 and bgy >= -1800:
            is_button = True
            if is_clicked == True:
                is_clicked = False
                tasks("Fill in the blank: (hint: you want to run it 20 times)"
                     , "for i in range(0, _____):",
                     "\tprint(\"shot an asteroid\")", "20")
                if tasks.is_complete == True:
                    tc = True
                    tasks_complete[1] = True
                    pygame.mixer.Sound.play(comsound)
                else:
                    pass
                tasks.is_complete = False
        else:
            is_button = False
    elif bgx <= -2900  and bgx >= - 3100:
        if bgy <= -360 and bgy >= -560:
            is_button = True
            if is_clicked == True:
                is_clicked = False
                tasks("Fill in the blank: (hint: you want to print scan complete)"
                     , "time = 0\t\t\t\t\nwhile(time < 5):\t\t\t\n\tprint(\"Scan complete in\" + str(time))\n\ttime += 1\t\t\t",
                     "___________________________\t\t", "print(\"scan complete\")")
                if tasks.is_complete == True:
                    tc = True
                    tasks_complete[2] = True
                    pygame.mixer.Sound.play(comsound)
                else:
                    pass
                tasks.is_complete = False
        else:
            is_button = False
    elif bgx <= 160  and bgx >= -40:
        if bgy <= -1120 and bgy >= -1320:
            is_button = True
            if is_clicked == True:
                is_clicked = False
                tasks("Write an else statment for oxygen levels, printing 'oxygen not set' on one line(write \\n for new line, \\t for tab)"
                     ,"if o_levels == 0.5:\n\tprint(\"oxygen set\")","____________________", "else:\\n\\tprint(\"oxygen not set\")")
                if tasks.is_complete == True:
                    tc = True
                    tasks_complete[3] = True
                    pygame.mixer.Sound.play(comsound)
                else:
                    pass
                tasks.is_complete = False
        elif bgy <= -1380 and bgy >= -1580:
            is_button = True
            if is_clicked == True:
                is_clicked = False
                tasks("Fill in the blanks to create the while loop(make it repeat twice, also make it print: can #i filled, spaces between blanks, but no spaces in blanks)"
                    , "i = 0\t\t\nwhile(_____):\t", "________\n\ti += 1\t\t",
                    "i<2 print(\"can#\"+str(i)+\"filled\")")
                if tasks.is_complete == True:
                    tc = True
                    tasks_complete[4] = True
                    pygame.mixer.Sound.play(comsound)
                else:
                    pass
                tasks.is_complete = False
        else:
            is_button = False
    else:
        is_button = False
    if tasks_complete.count(True) == len(tasks_complete):
        run = False
        end = True
    print(bgx)
    print(bgy)
    gameloop()

while end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.blit(victory, (-100,0))
    pygame.mixer.Sound.play(vroy)
    pygame.display.update()




