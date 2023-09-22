import tkinter as tk
from pathlib import Path

#file imports
from Database import Database
import clientWindow as client

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Resources\loginImages")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

##Onclick Event Handlers
def loginOnClick(event):
    frame.destroy()
    loginWindow()

def regOnClick(event):
    frame.destroy()
    register_window()

def chessOnClick(event):
    frame.destroy()
    entrance()

##global constants
inputFont = ('Calibri',20)

def centre(window):

    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (win.winfo_x() + win.winfo_width() // 2) - (width // 2)
    y = (win.winfo_y() + win.winfo_height() // 2) - (height // 2)
    window.geometry(f"+{x}+{y}")

def toast(message):

    toast = tk.Toplevel()
    toast.geometry("200x80")
    toast.title("Toast")
    toast.attributes('-topmost', True)
    label = tk.Label(toast, text=message, font=("Helvetica", 12))
    label.pack(pady=20)
    centre(toast)
    toast.after(1000, toast.destroy)

def register_user(rName_entry,rEmail_entry,rPass_entry,rPass2):

    if(rPass2.get() != rPass_entry.get()):
        toast("Passwords dont match")
        return
    # Check if the username already exists
    cursor = Database.conn.execute("SELECT COUNT(*) FROM USER WHERE USERNAME = ?", (rName_entry.get(),))
    exists = cursor.fetchone()[0]

    if exists > 0:
        toast("User already Exists")
        return

    else:

        Database.conn.execute("INSERT INTO USER (USERNAME, EMAIL, PASSWORD) VALUES (?, ?, ?)", (rName_entry.get(), rEmail_entry.get(), rPass_entry.get()))
        Database.conn.commit()
        toast("User Created")
        frame.destroy()
        entrance()

def login_user(lName_entry,lPass_entry):

    username = lName_entry.get()

    loginCursor = Database.conn.execute("SELECT USERNAME,PASSWORD FROM USER WHERE USERNAME = ?", (username,))
    exists = loginCursor.fetchone()

    if exists is None:
        print("user doesnt exist")

    elif exists[0] == username and exists[1] == lPass_entry.get():
        print("Login successful")
        print("Loading client")

        win.destroy()
        client.mainClientWindow()

    else:
        print("password is incorrect")
def register_window():

    global frame
    frame = tk.Frame(win, bg="#FFFFFF")
    frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(
        frame,
        bg="#FFFFFF",
        height=651,
        width=1044,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    global background
    background = tk.PhotoImage(file=relative_to_assets("Background.png"))
    canvas.create_image(533.0, 336.0, image=background)

    global loginButton
    loginButton = tk.PhotoImage(file=relative_to_assets("loginButtonReg.png"))
    lButton = canvas.create_image(922.0, 94.0, image=loginButton)
    canvas.tag_bind(lButton, '<Button-1>', loginOnClick)

    global chessIcon
    chessIcon = tk.PhotoImage(file=relative_to_assets("chessIcon.png"))
    chessI = canvas.create_image(117.0, 94.0, image=chessIcon)
    canvas.tag_bind(chessI, '<Button-1>', chessOnClick)

    canvas.create_text(160.0,76.0,anchor="nw",text="Fly Dream Air",fill="#000000",font=("Jaldi Bold", 32 * -1))

    global textArea
    textArea = tk.PhotoImage(file=relative_to_assets("textAreaReg.png"))
    canvas.create_image(528.0, 187.0, image=textArea)
    canvas.create_image(528.0, 281.0, image=textArea)
    canvas.create_image(528.0, 376.0, image=textArea)
    canvas.create_image(528.0, 469.0, image=textArea)

    rName_entry = tk.Entry(bd=0,font=inputFont)
    rName_entry.place(x=330.0, y=158.0, width=412.0, height=53.0)

    rEmail_entry = tk.Entry(bd=0,font=inputFont)
    rEmail_entry.place(x=330.0, y=252.0, width=412.0, height=53.0)

    rPass_entry = tk.Entry(bd=0,font=inputFont)
    rPass_entry.place(x=330.0, y=347.0, width=412.0, height=53.0)

    rPassConfirm = tk.Entry(bd=0,font=inputFont)
    rPassConfirm.place(x=330.0, y=442.0, width=412.0, height=53.0)

    global emailIcon
    emailIcon = tk.PhotoImage(file=relative_to_assets("regEmailIcon.png"))
    canvas.create_image(297.0, 281.0, image=emailIcon)

    global userIcon
    userIcon = tk.PhotoImage(file=relative_to_assets("regUserIcon.png"))
    canvas.create_image(297.0, 187.0, image=userIcon)

    global passIcon
    passIcon = tk.PhotoImage(file=relative_to_assets("regPassIcon.png"))
    canvas.create_image(297.0, 469.0, image=passIcon)
    canvas.create_image(297.0, 376.0, image=passIcon)

    global smallRights
    smallRights = tk.PhotoImage(file=relative_to_assets("smallRights.png"))
    canvas.create_image(858.0, 629.0, image=smallRights)

    global regButton
    regButton = tk.PhotoImage(file=relative_to_assets("regButtonReg.png"))
    rButton = canvas.create_image(529.0, 559.0, image=regButton)

    register_button_click = lambda event, rName=rName_entry, rEmail=rEmail_entry, rPass=rPass_entry, rPass2 = rPassConfirm: register_user(rName, rEmail, rPass,rPass2)
    canvas.tag_bind(rButton, '<Button-1>', register_button_click)

    bold = ("bold", 12, "bold")
    canvas.create_text(297.0,133.0,anchor="nw",text="Username",fill="#000000",font=bold)
    canvas.create_text(297.0, 414.0,anchor="nw",text="Re-Enter Password",fill="#000000",font=bold)
    canvas.create_text(297.0,224.0,anchor="nw",text="Email",fill="#000000",font=bold)
    canvas.create_text(297.0,319.0,anchor="nw",text="Password",fill="#000000",font=bold)

def loginWindow():

    global frame
    frame = tk.Frame(win, bg="#FFFFFF")
    frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(
        frame,
        bg = "#FFFFFF",
        height = 651,
        width = 1044,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    global background
    background = tk.PhotoImage(file=relative_to_assets("Background.png"))
    canvas.create_image(533.0,336.0,image=background)

    global regButton
    regButton = tk.PhotoImage(file=relative_to_assets("RegButton.png"))
    rButton = canvas.create_image(920.0,94.0,image=regButton)
    canvas.tag_bind(rButton, '<Button-1>', regOnClick)

    global cIcon
    cIcon = tk.PhotoImage(file=relative_to_assets("chessIcon.png"))
    chessI = canvas.create_image(117.0,94.0,image=cIcon)
    canvas.tag_bind(chessI, '<Button-1>', chessOnClick)

    canvas.create_text(
        160.0,
        76.0,
        anchor="nw",
        text="Fly Dream Air",
        fill="#000000",
        font=("Jaldi Bold", 32 * -1)
    )

    global textArea
    textArea = tk.PhotoImage(file=relative_to_assets("textArea.png"))
    canvas.create_image(528.0,250.0,image=textArea)
    canvas.create_image(528.0,362.0,image=textArea)

    global loginIcon
    loginIcon = tk.PhotoImage(file=relative_to_assets("loginIcon.png"))
    canvas.create_image(309.0,250.0,image=loginIcon)

    global passIcon
    passIcon = tk.PhotoImage(file=relative_to_assets("passIcon.png"))
    canvas.create_image(309.0,362.0,image=passIcon)

    global smallRights
    smallRights = tk.PhotoImage(file=relative_to_assets("smallRights.png"))
    canvas.create_image(858.0, 629.0, image=smallRights)

    global lPass_entry
    lPass_entry = tk.Entry(bd=0,font=inputFont)
    lPass_entry.place(x=343.0,y=336.0,width=412.0,height=51.0)

    global lName_entry
    lName_entry = tk.Entry(bd=0,font=inputFont)
    lName_entry.place(x=343.0,y=224.0, width=412.0,height=53.0)

    global loginButton
    loginButton = tk.PhotoImage(file=relative_to_assets("loginButton.png"))
    lButtons = canvas.create_image(529.0, 478.0, image=loginButton)

    loginclick = lambda event, lName=lName_entry, lPass=lPass_entry: login_user(lName, lPass)
    canvas.tag_bind(lButtons, '<Button-1>', loginclick)


def entrance():

    global frame

    frame = tk.Frame(win, bg="#FFFFFF")
    frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(
        frame,
        bg="#FFFFFF",
        height=651,
        width=1044,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    global backGround
    backGround = tk.PhotoImage(file=relative_to_assets("Background.png"))
    canvas.create_image(533.0, 336.0, image=backGround)

    global about
    about = tk.PhotoImage(file=relative_to_assets("about.png"))
    canvas.create_image(920.0, 94.0, image=about)

    global chess
    chess = tk.PhotoImage(file=relative_to_assets("chessIcon.png"))
    canvas.create_image(117.0, 94.0, image=chess)

    canvas.create_text(
        160.0,
        76.0,
        anchor="nw",
        text="Fly Dream Air",
        fill="#000000",
        font=("Inika", 32 * -1)
    )

    global rights
    rights = tk.PhotoImage(file=relative_to_assets("smallRights.png"))
    canvas.create_image(727.0, 609.0, image=rights)

    global loginButt
    loginButt = tk.PhotoImage(file=relative_to_assets("lLogin.png"))
    image_5 = canvas.create_image(293.0, 493.0, image=loginButt)
    canvas.tag_bind(image_5, '<Button-1>', loginOnClick)

    global regButt
    regButt = tk.PhotoImage(file=relative_to_assets("lRegister.png"))
    image_6 = canvas.create_image(736.0, 493.0, image=regButt)
    canvas.tag_bind(image_6, '<Button-1>', regOnClick)

    canvas.create_text(
        261.0,
        210.0,
        anchor="nw",
        text="Welcome To Fly Dream Air\nThe one place where dreaming\ncan become the Reality",
        fill="#000000",
        font=("MS Serif", 40 * -1, 'bold')
    )

def mainWindow():

    global win

    win = tk.Tk()
    win.title("Fly Dream Air")
    win.geometry("1044x651")

    entrance()

    win.resizable(False, False)
    win.mainloop()

def attemptWindow():

    frame.destroy()
    loginWindow()

def attemptRegister():

    frame.destroy()
    register_window()

