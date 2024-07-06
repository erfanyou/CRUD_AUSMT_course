from tkinter import *
from tkinter import ttk
import pygame
from PIL import Image, ImageTk
from pymongo import MongoClient
import webbrowser

# ---------------------- Database Connection -------------------------
def create_connection():
    client = MongoClient("localhost", 27017)
    return client

connection = create_connection()
db = connection['crud_app']
users_collection = db['users']

# ---------------------- CRUD Functions -------------------------
def create_user(users_collection, username, email, firstname, lastname, password):
    user = {"username": username, "email": email, "firstname": firstname, "lastname": lastname, "password": password}
    users_collection.insert_one(user)

def read_users(users_collection):
    return list(users_collection.find())

def update_user(users_collection, username, password, email):
    users_collection.update_one({"username": username}, {"$set": {"password":password, "email": email}})

def delete_user(users_collection, username, password, email):
    users_collection.delete_one({"username": username, "password": password, "email": email})

# ---------------------- GUI Functions -------------------------
def bt_delete():
    delete_user(users_collection, y1.get(), y2.get(), y3.get())
    master.destroy()

def play_game():
    url ='https://www.msn.com/en-us/play/games/krunker-frvr/cg-9mw6fcv4wcgf?ocid=winp1taskbar&cvid=d947c695dad34e8ea2bafe2b37c0e608&cgfrom=cg_prong1_cardgameitem&hideNativeSidebar=1'
    webbrowser.open(url)
def delete():
    global y1, y2, y3, master

    master = Tk()
    master.config(background="black")
    master.title("Delete")
    master.geometry("250x150")
    font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"

    try:
        custom_font = (font_path, 10)
    except:
        custom_font = ("Helvetica", 10)

    x=0
    e=['Username','Password','Email']
    y1 = Entry(master)
    y2 = Entry(master)
    y3 = Entry(master)
    y_entries = [y1, y2, y3]

    for i in e:
        Label(master, text=i, bg="black", fg="white", font=custom_font).grid(row=x)
        y_entries[x].grid(row=x, column=1)
        x+=1

    delete_btn = Button(master, text="delete", font=custom_font, bg="white", fg="black", command=bt_delete)
    delete_btn.grid(row=3, columnspan=2, pady=10)

    master.mainloop()

def bt_update():
    update_user(users_collection, x1.get(), x2.get(), x3.get())
    users = read_users(users_collection)
    for user in users:
        if user['username'] == x1.get():
            filewin = Toplevel(window)
            font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"
            try:
                custom_font = (font_path, 10)
            except:
                custom_font = ("Helvetica", 10)

            button = Button(filewin, text="successful! , play now", font=custom_font, bg="black", fg="white", command=play_game)
            button.pack()
            break
    else:
        filewin = Toplevel(window)
        font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"
        try:
            custom_font = (font_path, 10)
        except:
            custom_font = ("Helvetica", 10)

        button = Button(filewin, text="username is wrong!", font=custom_font, bg="black", fg="white", command=bt_update)
        button.pack()
    master.destroy()

def update():
    global x1, x2, x3, master

    master = Tk()
    master.config(background="black")
    master.title("Update")
    master.geometry("250x150")
    font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"

    try:
        custom_font = (font_path, 10)
    except:
        custom_font = ("Helvetica", 10)

    x=0
    e=['Username','New Password','New Email']
    x1 = Entry(master)
    x2 = Entry(master)
    x3 = Entry(master)
    x_entries = [x1, x2, x3]

    for i in e:
        Label(master, text=i, bg="black", fg="white", font=custom_font).grid(row=x)
        x_entries[x].grid(row=x, column=1)
        x+=1

    update_btn = Button(master, text="Update", font=custom_font, bg="white", fg="black", command=bt_update)
    update_btn.grid(row=3, columnspan=2, pady=10)

    master.mainloop()

def register():
    create_user(users_collection, e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
    filewin = Toplevel(window)
    font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"
    try:
        custom_font = (font_path, 10)
    except:
        custom_font = ("Helvetica", 10)

    button = Button(filewin, text="successful! , play now", font=custom_font, bg="black", fg="white",command=play_game)
    button.pack()
    master.destroy()

def enter():
    global e1, e2
    users = read_users(users_collection)
    for user in users:
        if (user['username'] == e1.get() or user['email'] == e1.get()) and user['password'] == e2.get():
            filewin = Tk()
            filewin.geometry("300x200")
            font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"
            try:
                custom_font = (font_path, 10)
            except:
                custom_font = ("Helvetica", 10)
            Label(filewin, text="welcome , play now", font=custom_font , command=play_game)
            break
    else:
        filewin = Toplevel(window)
        font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"

        try:
            custom_font = (font_path, 10)
        except:
            custom_font = ("Helvetica", 10)

        button = Button(filewin, text="you have no account so create account", font=custom_font, bg="black", fg="white" , command=sign_up)
        button.pack()
    master.destroy()

def sign_up():
    global e1, e2, e3, e4, e5, e6, master

    master = Tk()
    master.config(background="black")
    master.title('Sign Up')
    master.geometry("250x180")
    font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"

    try:
        custom_font = (font_path, 10)
    except:
        custom_font = ("Helvetica", 10)
    x=0
    e=['username', 'email', 'firstname', 'lastname', 'password', 'confirm password']
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e6 = Entry(master)
    e_entries = [e1, e2, e3, e4, e5, e6]

    for i in e:
        Label(master, text=i, bg="black", fg="white", font=custom_font).grid(row=x)
        e_entries[x].grid(row=x, column=1)
        x+=1

    register_btn = Button(master, text="register", font=custom_font, bg="white", fg="black", command=register)
    register_btn.grid(row=6, columnspan=2, pady=10)

    master.mainloop()

def login():
    global e1, e2, master

    master = Tk()
    master.config(background="black")
    master.title('Login')
    master.geometry("250x100")
    font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"

    try:
        custom_font = (font_path, 10)
    except:
        custom_font = ("Helvetica", 10)

    Label(master, text='Username or Email', background="black", fg="white", font=custom_font).grid(row=0)
    Label(master, text='Password', background="black", fg="white", font=custom_font).grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)
    e_entries = [e1, e2]

    for i in range(2):
        e_entries[i].grid(row=i, column=1)

    enter_btn = Button(master, text="Enter", font=custom_font, bg="white", fg="black", command=enter)
    enter_btn.grid(row=2, columnspan=2, pady=10)
    master.mainloop()

def donothing():
    filewin = Toplevel(window)
    font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"

    try:
        custom_font = (font_path, 10)
    except:
        custom_font = ("Helvetica", 10)

    button = Button(filewin, text="Sorry! I don't know", font=custom_font, bg="black", fg="white")
    button.pack()

def music():
    mu = Tk()
    mu.geometry("200x150")
    mu.title("Music")
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    font_path = r"F:\python\crud\font\FiraCode-Bold.ttf"
    try:
        custom_font = (font_path, 10)
    except:
        custom_font = ("Helvetica", 10)
    def play_music():
        pygame.mixer.music.play(-1)
    def stop_music():
        pygame.mixer.music.stop()

    C1 = Checkbutton(mu, text="On", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20, font=custom_font,bg="black", fg="white", command=play_music)
    C2 = Checkbutton(mu, text="Off", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20, font=custom_font,bg="black", fg="white", command=stop_music)
    C1.pack()
    C2.pack()
    mu.mainloop()

def chart():
    master = Tk()
    master.config(background="black")
    master.title("Chart")
    master.geometry("800x400")

    columns= ["id", "username", "email", "firstname", "lastname", "password"]
    table = ttk.Treeview(master, columns=columns, show='headings')
    for i in range(len(columns)):
        table.heading(columns[i], text=columns[i])
        table.column(columns[i], width=100)
        table.pack()
    table.place(x=100, y=100)
    master.mainloop()

# ---------------------- Main Window Configuration -------------------------
CRUD_WITH = 1000
CRUD_HEIGHT = 600
BACKGROUND_COLOR = "white"

window = Tk()
window.title("CRUD")
window.resizable(False, False)
window.iconbitmap(r'F:\python\crud\icons\lucidvirtumvp.ico')

image = Image.open(r"F:\python\crud\image\WallpaperGram.IR_1575471265_1211.png")
image = image.resize((CRUD_WITH, CRUD_HEIGHT))
bg_image = ImageTk.PhotoImage(image)

background_label = Label(window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

pygame.mixer.init()
pygame.mixer.music.load(r"F:\python\crud\music\september instrumental.mp3")
pygame.mixer.music.play(-1)

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Log In', command=login)
filemenu.add_command(label='Sign Up', command=sign_up)
filemenu.add_command(label='Update account', command=update)
filemenu.add_command(label='Delete account', command=delete)
menubar.add_cascade(label="Menu", menu=filemenu)
menubar.add_cascade(label='User Chart', command=chart)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Music", command=music)
menubar.add_cascade(label="Setting", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{CRUD_WITH}x{CRUD_HEIGHT}+{x}+{y}")
window.config(menu=menubar)
window.mainloop()
