from tkinter import*
import random
import tkinter.font as font
playerscore=0
computerscore=0
def computerwins():
    global computerscore,playerscore
    computerscore+=1
    l1.config(text="Computer Wins!")
    cs.config(text="Computer Score: "+str(computerscore))
    ps.config(text="Your Score: "+str(playerscore))
def playerwins():
    global computerscore,playerscore
    playerscore+=1
    l1.config(text="You Win!")
    cs.config(text="Computer Score: "+str(computerscore))
    ps.config(text="Your Score: "+str(playerscore))
def tie():
    global computerscore,playerscore
    l1.config(text="It's a tie!")
    cs.config(text="Computer Score: "+str(computerscore))
    ps.config(text="Your Score: "+str(playerscore))
options=[("rock",0),("paper",1),("scissors",2)]
def computerchoice():
    global options
    return random.choice(options)
def playerchoice(playerinput):
    print(playerinput)
    computerinput=computerchoice()
    print(computerchoice)
    pc.config(text="You selected "+playerinput[0])
    cc.config(text="Computer selected "+computerinput[0])
    if(playerinput == computerinput):
        tie()
    if(playerinput[1] == 0):
        if(computerinput[1] == 1):
            computerwins()
        elif(computerinput[1] == 2):
            playerwins()
    if(playerinput[1] == 1):
        if(computerinput[1] == 0):
            playerwins()
        elif(computerinput[1] == 2):
            computerwins()
    if(playerinput[1] == 2):
        if(computerinput[1] == 0):
            computerwins()
        elif(computerinput[1] == 1):
            playerwins()
root=Tk()
root.title("Rock,Paper,Scissors")
a=Label(root,text="Rock,Paper,Scissors",font=font.Font(size=20),fg="sky blue")
a.pack()
l1=Label(root,text="Let's start the game!",font=font.Font(size=10),fg="purple")
l1.pack()
a=Frame(root)
a.pack()
l2=Label(a,text="You can choose between: ",font=font.Font(size=10),fg="purple")
l2.grid(row=1,column=0,pady=7)
b1=Button(a,text="rock",width=15,bd=0,bg="pink",pady=10,command=lambda: playerchoice(options[0]))
b1.grid(row=1,column=1,pady=7,padx=7)
b2=Button(a,text="paper",width=15,bd=0,bg="pink",pady=10,command=lambda: playerchoice(options[1]))
b2.grid(row=1,column=2,pady=7,padx=7)
b3=Button(a,text="scissors",width=15,bd=0,bg="pink",pady=10,command=lambda: playerchoice(options[2]))
b3.grid(row=1,column=3,pady=7,padx=7)
score=Label(a,text="Score: ",font=font.Font(size=10),fg="purple")
score.grid(row=2,column=0,pady=7)
pc=Label(a,text="Your Choice: ",font=font.Font(size=10),fg="black")
pc.grid(row=3,column=0,pady=7)
cc=Label(a,text="Computer Choice: ",font=font.Font(size=10),fg="black")
cc.grid(row=4,column=0,pady=7)
ps=Label(a,text="Your Score: ",font=font.Font(size=10),fg="black")
ps.grid(row=3,column=2,pady=7)
cs=Label(a,text="Computer Score: ",font=font.Font(size=10),fg="black")
cs.grid(row=4,column=2,pady=7)
root.mainloop()
