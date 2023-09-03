import tkinter  as tk
from FlyDreamAir.Database import Database
import Client as client
print("Fly Dream Air")
print("Group Project")


def register_user():

    # Check if the username already exists
    cursor = Database.conn.execute("SELECT COUNT(*) FROM USER WHERE USERNAME = ?", (rName_entry.get(),))
    exists = cursor.fetchone()[0]

    if exists > 0:
        print("Username already Exists")
        return

    else:

        Database.conn.execute("INSERT INTO USER (USERNAME, EMAIL, PASSWORD) VALUES (?, ?, ?)", (rName_entry.get(), rEmail_entry.get(), rPass_entry.get()))
        Database.conn.commit()

        win.destroy()
        main()

def destroy():

    win.destroy()

def login_window():

    global lName_entry, win, lPass_entry
    destroy()

    win = tk.Tk()

    win.geometry("393x690")
    win.configure(bg="#DEF7FF")

    canvas = tk.Canvas(
        win,
        bg="#DEF7FF",
        height=690,
        width=393,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        20.0,
        117.0,
        anchor="nw",
        text="Log in",
        fill="#000000",
        font=("Poppins Bold", 30 * -1)
    )

    canvas.create_text(
        91.0,
        621.0,
        anchor="nw",
        text="Don’t have an account? Sign up",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    canvas.create_text(
        172.0,
        494.0,
        anchor="nw",
        text="Log in",
        fill="#FFFFFF",
        font=("Inter SemiBold", 16 * -1)
    )

    button_image_1 = tk.PhotoImage(
        file=("Resources/button_1.png"))
    button_1 = tk.Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: login_user(),
        relief="flat"
    )
    button_1.place(
        x=19.0,
        y=514.0,
        width=353.0,
        height=56.0
    )

    button_image_2 = tk.PhotoImage(
        file=("Resources/arrow.png"))
    button_2 = tk.Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=main_destroy,
        relief="flat"
    )
    button_2.place(
        x=7.0,
        y=11.0,
        width=47.0,
        height=47.0
    )

    image_image_1 = tk.PhotoImage(
        file=("Resources/image_1.png"))
    image_1 = canvas.create_image(
        343.0,
        69.0,
        image=image_image_1
    )

    entry_image_1 = tk.PhotoImage(
        file=("Resources/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        195.5,
        396.0,
        image=entry_image_1
    )
    lName_entry = tk.Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    lName_entry.place(
        x=29.0,
        y=368.0,
        width=333.0,
        height=54.0
    )

    canvas.create_text(
        20.0,
        336.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    entry_image_2 = tk.PhotoImage(
        file=("Resources/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        196.5,
        262.0,
        image=entry_image_2
    )
    lPass_entry = tk.Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    lPass_entry.place(
        x=30.0,
        y=234.0,
        width=333.0,
        height=54.0
    )

    canvas.create_text(
        20.0,
        204.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("Inter", 14 * -1)
    )
    win.resizable(False, False)
    win.mainloop()

def register_window():

    global rName_entry,rPass_entry,rEmail_entry,lFrame,exist_label,win

    destroy()

    win = tk.Tk()
    win.title("Fly Dream Air")
    win.geometry("800x400")
    win.configure(bg="#EFFEFF")

    canvas = tk.Canvas(
        win,
        bg="#F6FFFD",
        height=400,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    canvas.create_text(
        481.0,
        65.0,
        anchor="nw",
        text="Create account",
        fill="#000000",
        font=("Poppins Bold", 30 * -1)
    )

    image_image_1 = tk.PhotoImage(
        file="Resources/image_2.png")
    image_1 = canvas.create_image(
        400.0,
        38.0,
        image=image_image_1
    )

    canvas.create_text(
        481.0,
        264.0,
        anchor="nw",
        text="Already have an account?  Log in",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    entry_image_1 = tk.PhotoImage(
        file=("Resources/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        200.5,
        119.0,
        image=entry_image_1
    )
    rName_entry = tk.Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    rName_entry.place(
        x=34.0,
        y=91.0,
        width=333.0,
        height=54.0
    )

    canvas.create_text(
        24.0,
        51.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    entry_image_2 = tk.PhotoImage(
        file=("Resources/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        200.5,
        228.0,
        image=entry_image_2
    )
    rEmail_entry = tk.Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    rEmail_entry.place(
        x=34.0,
        y=200.0,
        width=333.0,
        height=54.0
    )

    canvas.create_text(
        24.0,
        161.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    entry_image_3 = tk.PhotoImage(
        file=("Resources/entry_3.png"))
    canvas.create_image(
        198.5,
        345.0,
        image=entry_image_3
    )
    rPass_entry = tk.Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    rPass_entry.place(
        x=32.0,
        y=317.0,
        width=333.0,
        height=54.0
    )

    canvas.create_text(
        24.0,
        278.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    button_image_1 = tk.PhotoImage(
        file=("Resources/button_2.png"))

    button_3 = tk.Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=register_user,
        relief="flat"
    )
    button_3.place(
        x=414.0,
        y=175.0,
        width=353.0,
        height=56.0
    )
    win.resizable(False, False)
    win.mainloop()

def main_destroy():

    win.destroy()
    main()

def login_user():

    username = lName_entry.get()

    loginCursor = Database.conn.execute("SELECT USERNAME,PASSWORD FROM USER WHERE USERNAME = ?", (username,))
    exists = loginCursor.fetchone()

    if exists is None:
        print("username or password is incorrect")

    elif exists[0] == username and exists[1] == lPass_entry.get():
        print("Login successful")
        print("Loading client")
        destroy()
        client.clientWindow()

    else:
        print("username or password is incorrect")

def mainWindow():

    global win,register_button,login_button,canvas,button_1,canvas


    win = tk.Tk()
    win.title("Fly Dream Air")
    win.geometry("800x400")
    win.configure(bg="#EFFEFF")

    canvas = tk.Canvas(
        win,
        bg="#EFFEFF",
        height=400,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = tk.PhotoImage(
        file=("Resources/p.png"))
    image_1 = canvas.create_image(
        599.0,
        124.0,
        image=image_image_1
    )

    button_image_1 = tk.PhotoImage(
        file=("Resources/button_1.png"))

    button_1 = tk.Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=login_window,
        relief="flat"
    )
    button_1.place(
        x=36.0,
        y=96.0,
        width=353.0,
        height=56.0
    )

    button_image_2 = tk.PhotoImage(
        file=("Resources/button_2.png"))
    button_2 = tk.Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=register_window,
        relief="flat"
    )
    button_2.place(
        x=36.0,
        y=248.0,
        width=353.0,
        height=56.0
    )

    canvas.create_text(
        509.0,
        276.0,
        anchor="nw",
        text="Welcome To Fly Dream Air\nThe one place where dreaming\ncan become the reality\n",
        fill="#000000",
        font=("Inter", 17 * -1)
    )

    canvas.create_text(
        503.0,
        219.0,
        anchor="nw",
        text="Fly Dream Air",
        fill="#000000",
        font=("Inter ExtraBold", 32 * -1)
    )
    win.resizable(False, False)
    win.mainloop()


def userWindow():

    win.geometry("1000x800")
    register_button.destroy()
    login_button.destroy()


def main():

    mainWindow()

if __name__ == "__main__":

   main()

