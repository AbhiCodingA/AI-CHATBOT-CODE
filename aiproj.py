from tkinter import *
from PIL import Image,ImageTk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time


time.clock=time.time()
bot=ChatBot('Bot')
data=open('ai.yml','r',encoding='utf-8').readlines()
trainer=ListTrainer(bot)
trainer.train(data)
def reply():
     question = quesfld.get()
     question = question.capitalize()
     answer = bot.get_response(question)
     txtfld.insert(END, 'You:  ' + question + '\n')
     txtfld.insert(END, 'Bot:  ' + str(answer) + '\n\n')
     quesfld.delete(0,END)
root=Tk()
root.geometry("500x570+500+150")
root.title("Chatbot")
root.config(bg="#2F2F4F")
image=Image.open('03b5063e4d6ecf649ef1c005e6e1fb15.png')
img=image.resize((75,75))
logo=ImageTk.PhotoImage(img)
lab1=Label(root,image=logo,bg="#2F2F4F")
lab1.pack()
frame=Frame(root)
frame.pack()
bar=Scrollbar(frame)
bar.pack(side="right")
txtfld=Text(frame,bg="#69698B",font=("Berlin Sans",14,"bold"),height=18,yscrollcommand=bar.set)
txtfld.pack()
bar.config(command=txtfld.yview)
quesfld=Entry(root,font=("Times new Roman",14,"bold"),bg="#69698B")
quesfld.pack(pady=9,fill=X)
but1=Button(root,width=15,text="ASK",bg="#69698B",command=reply)
but1.pack()
root.mainloop()