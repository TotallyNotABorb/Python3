from tkinter import *

window=Tk()
window.title("JobFinder")
window.geometry("750x1000+0+0")
window.resizable(False,False)
#window.iconbitmap("images/magnifying-glass.ico")
window.config(bg="#3e3e3e")
text1=Label(window,text="Job")
text1.config(bg="#3e3e3e",fg="#c172e8",font=("Comic Sans MS",24,"italic"))
text1.place(x=300,y=50)
text2=Label(window,text="Finder")
text2.config(bg="#3e3e3e",fg="#ffffff",font=("Comic Sans MS",24,"italic"))
text2.place(x=360,y=50)
text3=Label(window,text="Login:")
text3.config(bg="#3e3e3e",fg="#c172e8",font=("Comic Sans MS",20,"italic"))
text3.place(x=220,y=110)
login=Entry()
login.config(width=20,font=("Comic Sans MS",20,"italic"),fg="#c172e8",border=1)
login.place(x=220,y=150)
log_but=Button(window,text="-Log in-")
log_but.config(bg="#c172e8",fg="#3e3e3e",width=40,height=2,activebackground="#3e3e3e",activeforeground="#c172e8",font=("Comic Sans MC",10),border=1)
log_but.place(x=220,y=400)
login2=Entry()
login2.config(width=20,font=("Comic Sans MS",20,"italic"),fg="#c172e8",border=1)
login2.place(x=220,y=250)
text3=Label(window,text="Password:")
text3.config(bg="#3e3e3e",fg="#c172e8",font=("Comic Sans MS",20,"italic"))
text3.place(x=220,y=200)
text3=Label(window,text="Mail:")
text3.config(bg="#3e3e3e",fg="#c172e8",font=("Comic Sans MS",20,"italic"))
text3.place(x=220,y=300)
login3=Entry()
login3.config(width=20,font=("Comic Sans MS",20,"italic"),fg="#c172e8",border=1)
login3.place(x=220,y=350)






window.mainloop()