#Import Module
from tkinter import *
import tkinter.messagebox as tm
import random
def guess(): #Define the guessing function
    while 1: #If true, execute
        root = Tk()
        root.title("Let's guess")
        Label(root, text="Please enter: Scissors (0) Rock (1) paper (2):", font=("Arial", 25)).grid(row=0, column=0)#Set options
        num = Entry(root, width=20)
        num.grid(row=0, column=1)
        Button(root, text="make a comparison", command=root.quit, font=("Arial", 25)).grid(row=1, column=1)#Button Settings
        root.mainloop()
        player = int(num.get())

        computer = random.randint(0,2)#The computer picks one at random
#The judgment of various situations
        if player==0:
            txt1="You come out of the scissors,"
        elif player==1:
            txt1 = "You come out of the stone,"
        elif player==2:
            txt1 = " you come out of the peper,"
        if computer==0:
            txt2 = "Computer scissors,"
        elif computer==1:
            txt2 = "Computer stone,"
        elif computer==2:
            txt2 = "Computer paper,"
        if ((player == 0) and (computer == 2)) or ((player ==1) and (computer == 0)) or ((player == 2) and (computer == 1)):
            tm.showinfo("reminder", "%s\nYou win.，haha，You're so cool！"%(txt1+txt2))
            break
        elif player == computer:
            tm.showinfo("reminder", "%s\nDraw. One more game" % (txt1 + txt2))
        elif player not in (0,1,2):
            tm.showinfo("reminder", "Stop punching and start over!")
        else:
            tm.showinfo("reminder", "%s\nLose, don't go, wash your hands and come on, fight till dawn" % (txt1 + txt2))
guess()#execute