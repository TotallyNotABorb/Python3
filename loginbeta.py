from tkinter import *
from PIL import Image, ImageTk

def sign_in_frame():

    window = Tk()
    window.title("SpaceGlass")
    window.iconbitmap(r"images/mag_glass.ico")
    window.resizable(False,False)
    window.geometry("1160x690+50+50")

    image = Image.open(r"images/backgrounddd.jpg")
    resize_image = image.resize((1160, 690))
    img = ImageTk.PhotoImage(resize_image)

    background_label = Label(window, image=img)
    background_label.place(x=0, y=0)
    background_label.image = img

    name1_label=Label(window,text="Space")
    name1_label.config(bg="#000a3d",fg="#0f0fef",font=("Arial",20,"bold"))
    name1_label.place(x=482,y=50)

    name2_label=Label(window,text="Glass")
    name2_label.config(bg="#000a3d",fg="#ffffff",font=("Arial",20,"bold"))
    name2_label.place(x=565,y=50)

    login_label=Label(window,text="Login:")
    login_label.config(bg="#011047",fg="#ffffff",font=("Arial",18))
    login_label.place(x=440,y=120)

    login_entry=Entry(window)
    login_entry.config(bg="#ffffff",width=20,font=("Arial",18),border=1)
    login_entry.place(x=440,y=150)

    password_label=Label(window,text="Password:")
    password_label.config(bg="#011047",fg="#ffffff",font=("Arial",18))
    password_label.place(x=440,y=190)

    password_entry=Entry(window)
    password_entry.config(bg="#ffffff",width=20,font=("Arial",18),border=1)
    password_entry.place(x=440,y=220)

    def sign_check():
        accounts={}
        login_save=login_entry2.get()
        pass_save=password_entry2.get()
        number_save=number_entry.get()
        accounts.update({login_save:{password:pass_save,number:number_save}})
    def sign_up_frame():


        window.destroy()

        window_log=Tk()
        window_log.title("SpaceGlass")
        window_log.iconbitmap(r"images/mag_glass.ico")
        window_log.resizable(False,False)
        window_log.geometry("1160x690+50+50")

        image = Image.open(r"images/backgrounddd.jpg")
        resize_image = image.resize((1160, 690))
        img = ImageTk.PhotoImage(resize_image)

        background_label1 = Label(window_log, image=img)
        background_label1.place(x=0, y=0)
        background_label1.image = img

        name1_label = Label(window_log, text="Space")
        name1_label.config(bg="#000a3d", fg="#0f0fef", font=("Arial", 20, "bold"))
        name1_label.place(x=482, y=50)

        name2_label = Label(window_log, text="Glass")
        name2_label.config(bg="#000a3d", fg="#ffffff", font=("Arial", 20, "bold"))
        name2_label.place(x=565, y=50)

        login_label2 = Label(window_log, text="Login:")
        login_label2.config(bg="#011047", fg="#ffffff", font=("Arial", 18))
        login_label2.place(x=440, y=120)

        login_entry2 = Entry(window_log)
        login_entry2.config(bg="#ffffff", width=20, font=("Arial", 18), border=1)
        login_entry2.place(x=440, y=150)

        password_label2 = Label(window_log, text="Password:")
        password_label2.config(bg="#011047", fg="#ffffff", font=("Arial", 18))
        password_label2.place(x=440, y=190)

        password_entry2 = Entry(window_log)
        password_entry2.config(bg="#ffffff", width=20, font=("Arial", 18), border=1)
        password_entry2.place(x=440, y=220)

        number_label = Label(window_log, text="Number:")
        number_label.config(bg="#09154F", fg="#ffffff", font=("Arial", 18))
        number_label.place(x=440, y=260)

        number_entry = Entry(window_log)
        number_entry.config(bg="#ffffff", width=20, font=("Arial", 18), border=1)
        number_entry.place(x=440, y=290)




        




        window_log.mainloop()


        


    def sign_check():
        log_get=login_entry.get()
        pass_get=password_entry.get()
        if log_get=="Bagel" and pass_get=="UwU":
            window.destroy()
            window_main=Tk()
            window_main.resizable(False,False)
            window_main.title("SpaceGlass")
            window_main.config(bg="#3f3f3f")
            window_main.state("zoomed")
            window_main.place(x=0,y=0)







    sign_button=Button(window,text="Sign in",command=sign_check)
    sign_button.config(bg="#0f0fef",fg="#ffffff",activebackground="#ffffff",activeforeground="#0f0fef",width=20,font=("Arial",17),border=1)
    sign_button.place(x=440,y=270)

    log_sit_button=Button(window,text="Have no account? Press here to sign up!",command=sign_up_frame)
    log_sit_button.config(bg="#010010",fg="#ffffff",activebackground="#000000",activeforeground="#0f0fef",border=0)
    log_sit_button.place(x=480,y=650)






    window.geometry("1160x690")

    sign_fr=Frame(window)
    sign_fr.mainloop()




sign_in_frame()
