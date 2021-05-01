#coding=utf-8
from tkinter import *
import random

#Initializes global variables
global windows
global human
global number_total
global number_win
global number_lose
global number_draw
windows = 0
human = 0
number_total = 0
number_win = 0
number_lose = 0
number_draw = 0

#Random display  window of gestures
def windows_function():

    global windows
    windows = random.randint(0, 2)

    if windows == 0:
        label_image_window.configure(image = image_Scissors)
    elif windows == 1:
        label_image_window.configure(image = image_Rock)
    else:
        label_image_window.configure(image = image_Paper)

#judge human and windows's Victory or defeat
def judgement(human,windows):
    global number_win
    global number_lose
    global number_draw
    global number_total

    if (human == 0 and windows == 2) or (human == 1 and windows == 0) or (human == 2 and windows == 1):
        number_win+=1
        label_down.configure(text='Congratulations, You Won !')
    elif human == windows:
        label_down.configure(text = 'Draw, Cheer up !')
        number_draw+=1
    else:
        number_lose+=1
        label_down.configure(text='Sorry, You Lost !')

    label_result.configure(text = 'Win: '+str(number_win)+
                               '\nLose: '+str(number_lose)+
                               '\nDraw: '+str(number_draw)+
                               '\n Total: '+str(number_total))

def hit_Scissors():
    global number_total
    number_total+=1
    label_image.configure(image = image_Scissors)
    windows_function()
    human = 0
    judgement(human,windows)

def hit_Rock():
    global number_total
    number_total+=1
    label_image.configure(image = image_Rock)
    windows_function()
    human = 1
    judgement(human,windows)

def hit_Paper():
    global number_total
    number_total+=1
    label_image.configure(image = image_Paper)
    windows_function()
    human = 2
    judgement(human,windows)

def pass_function():
    pass


top = Tk()
top.title('Heimu Python')
top.geometry('450x400')

############-------设置label--------##############

#label_human
label_human = Label(top,text = 'Human',
                    bg = 'green',
                    fg = 'Ghostwhite',
                    font = ('Arial',12)
                    )
label_human.place(x=70,y=172,ancho='nw')

#label_windows
label_windows = Label(top,text = 'windows',
                      bg = 'green',
                      fg = 'Ghostwhite',
                      font = ('Arial',12)
                      )
label_windows.place(x=332,y=172,ancho='nw')

#label_down
label_down = Label(top,text = 'Are You Ready? Go!Go!Go!!!',
                   bg = 'green',
                   fg = 'ghostwhite',
                   font = ('Arial',12),
                   width=30,height=2
                   )
label_down.place(x=90,y=330,ancho='nw')

#label_result
label_result = Label(top,text = 'Win: '+str(number_win)+
                               '\nLose: '+str(number_lose)+
                               '\nDraw: '+str(number_draw)+
                               '\n Total: '+str(number_total),
                     bg = 'green',
                     fg = 'Ghostwhite')
label_result.place(x=0,y=315,ancho='nw')

############------------Set display image'slabel-------------#############

#Read the images used, PNG format
image_Scissors = PhotoImage(file='./photo/jiandao.png')
image_Rock = PhotoImage(file='./photo/shitou.png')
image_Paper = PhotoImage(file='./photo/bu.png')
image_kobe = PhotoImage(file='./photo/keo.png')
image_kobe1 = PhotoImage(file='./photo/keo.png')
image_welcome = PhotoImage(file='./photo/welcome.png')

#initialize human's image shows kobe
label_image = Label(top,image=image_kobe1)
label_image.place(x=40,y=200,ancho='nw')

# initialize windows's image shows kobe
label_image_window = Label(top,image=image_kobe1)
label_image_window.place(x=315,y=200,ancho='nw')

#show welcome image
label_welcome = Label(top,image=image_welcome)
label_welcome.place(x=0,y=40,ancho='nw')

#show kobe,logo
label_kobe = Label(top,image=image_kobe)
label_kobe.place(x=220,y=40,ancho='nw')

############-------------setting button-----------------################

#button_main
button_main = Button(top,text = 'Heimu Game !',

                   bg = 'green',
                    fg = 'Ghostwhite',
                   command = pass_function,
                   font = ('Arial',12),

                   )
button_main.place(x=180,y=3,ancho='nw')

#button_Scissors
button_Scissors = Button(top,text = 'Scissors',
                        command = hit_Scissors,
                        bg = 'green',
                        fg = 'Ghostwhite',
                        font = ('Arial',12)
                        )
button_Scissors.place(x=200,y=190,ancho='nw')

#button_Rock
button_Rock = Button(top,text = 'Rock',
                       command = hit_Rock,
                       bg = 'green',
                       fg = 'Ghostwhite',
                       font = ('Arial',12)
                       )
button_Rock.place(x=211,y=230,ancho='nw')

#button_Paper
button_Paper = Button(top,text = 'Paper',
                   command = hit_Paper,
                   bg = 'green',
                   fg = 'Ghostwhite',
                   font = ('Arial',12)
                   )
button_Paper.place(x=207,y=270,ancho='nw')


top.mainloop()
