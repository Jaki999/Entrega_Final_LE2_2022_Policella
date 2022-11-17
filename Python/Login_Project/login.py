from cProfile import label
from sys import displayhook
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

###usuario
user={
    'username': '1',
    'password': '1'
}

###funcion para conectar
def connection():
    if user["password"] == entry_password.get() and user["username"] == entry_username.get():
        correctUser()
    else:
        incorrectUser()

####popups para commit
def correctUser():
    messagebox.showinfo("","Iniciaste sesion correctamente")
def incorrectUser():
    messagebox.showerror("","Su password o username es incorrecto")

###ventana main
ventana_login = Tk()
ventana_login.title("Login")
ventana_login.geometry("925x500+350+50")
ventana_login.resizable(False, False)
ventana_login.config(bg='White')



###marcos
frame_1 = Frame(ventana_login, width=350, height=350, bg='#256D85')
frame_1.place(x=520, y=70)

frame_2 = Frame(ventana_login, width=463, height=500, bg='#5DA7DB')
frame_2.place(x=0, y=0)

Frame(frame_1, width=295, height=2, bg='black').place(x=25, y=107)
Frame(frame_1, width=295, height=2, bg='black').place(x=25, y=177)

###imagen
img = ImageTk.PhotoImage(Image.open("Login_Project\candado_3_300x300.png"))
displayimg = Label(frame_2, image=img, bg='#5DA7DB').place(x=50, y=75)

###labels
Singin = Label(frame_1, text="Log In", fg='#256D85', bg='#256D85', font=('Microsoft YaHei UI Light', 20, 'bold')) 
Singin.place(x=135,y=0)

###entrys
def on_enter(e):
    entry_username.delete(0, 'end')
def on_leave(e):
    name=entry_username.get()
    if name=='':
        entry_username.insert(0, 'Username')

entry_username = Entry(frame_1, width=20, border=0, bg='#256D85', font=('Microsoft YaHei UI Light', 11))
entry_username.place(x=30, y=80)
entry_username.insert(0,'Username')
entry_username.bind('<FocusIn>', on_enter)
entry_username.bind('<FocusOut>', on_leave)
#--------------------------------------------------------------------------------
def on_enter(e):
    entry_password.delete(0, 'end')
def on_leave(e):
    passwrd=entry_password.get()
    if passwrd=='':
        entry_password.insert(0, 'Password')

entry_password = Entry(frame_1, width=20, border=0, bg='#256D85', show='*', font=('Microsoft YaHei UI Light', 11))
entry_password.place(x=30, y=150)
entry_password.insert(0,'Password')
entry_password.bind('<FocusIn>', on_enter)
entry_password.bind('<FocusOut>', on_leave)

###botones
accept = Button(frame_1, width=39, pady=7, command=connection, text="Commit")
accept.place(x=30, y=200)
quit = Button(frame_1, width=15, pady=5, command=ventana_login.destroy, text="Quit")
quit.place(x=114, y=250)




ventana_login.mainloop()