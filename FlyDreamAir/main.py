import tkinter as tk
from FlyDreamAir.Database import Database

print("Fly Dream Air")
print("Group Project")
print("Poh Yamone")


def register_user():

    # Check if the username already exists
    cursor = Database.conn.execute("SELECT COUNT(*) FROM USER WHERE USERNAME = ?", (rName_entry.get(),))
    exists = cursor.fetchone()[0]

    if exists > 0:
        print("Username already Exists")
        exist_label = tk.Label(rFrame, text="User already exists")
        exist_label.grid(row=10, columnspan=2, pady=20)
        return

    else:

        Database.conn.execute("INSERT INTO USER (USERNAME, EMAIL, PASSWORD) VALUES (?, ?, ?)", (rName_entry.get(), rEmail_entry.get(), rPass_entry.get()))
        Database.conn.commit()

        rWindow.destroy()

def register_user_window():

    global rWindow,rName_entry, rEmail_entry, rPass_entry, rFrame

    rWindow = tk.Toplevel(win)
    rWindow.geometry("400x300")

    rFrame = tk.Frame(rWindow)
    rFrame.pack(pady=20)

    rName_label = tk.Label(rFrame, text="Username:")
    rName_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    rName_entry = tk.Entry(rFrame)
    rName_entry.grid(row=0, column=1, padx=10, pady=10)

    rEmail_label = tk.Label(rFrame, text="Email:")
    rEmail_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    rEmail_entry = tk.Entry(rFrame)
    rEmail_entry.grid(row=2, column=1, padx=10, pady=10)

    rPass_label = tk.Label(rFrame, text="Password:")
    rPass_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    rPass_entry = tk.Entry(rFrame)
    rPass_entry.grid(row=4, column=1, padx=10, pady=10)

    r_button = tk.Button(rFrame, text="Register", command=register_user)
    r_button.grid(row=6, columnspan=2, pady=20)

def login_user_window():

    global lWindow,lName_entry,lPass_entry,lFrame,exist_label

    lWindow = tk.Toplevel(win)
    lWindow.geometry("400x300")

    lFrame = tk.Frame(lWindow)
    lFrame.pack(pady=20)

    lName_label = tk.Label(lFrame, text="Username:")
    lName_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    lName_entry = tk.Entry(lFrame)
    lName_entry.grid(row=0, column=1, padx=10, pady=10)

    lPass_label = tk.Label(lFrame, text="Password:")
    lPass_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    lPass_entry = tk.Entry(lFrame)
    lPass_entry.grid(row=4, column=1, padx=10, pady=10)

    l_button = tk.Button(lFrame, text="Login", command=login_user)
    l_button.grid(row=6, columnspan=2, pady=20)

    exist_label = tk.Label(lFrame, text="")
    exist_label.grid(row=10, columnspan=2, pady=20)

def login_user():

    username = lName_entry.get()
    loginCursor = Database.conn.execute("SELECT USERNAME,PASSWORD FROM USER WHERE USERNAME = ?", (username,))
    exists = loginCursor.fetchone()

    if exists is None:

        exist_label.config(text="username or password is incorrect")

    elif exists[0] == username and exists[1] == lPass_entry.get():
        exist_label.config(text="Login successful")

    else:
        exist_label.config( text="username or password is incorrect")

def mainWindow():
    global win
    win = tk.Tk()
    win.title("Fly Dream Air")
    win.geometry("600x400")

    # Load the image
    bgimg = tk.PhotoImage(file="p.png")

    # Create a canvas for the background image
    canvas = tk.Canvas(win, width=600, height=400)
    canvas.pack()

    bg_label = tk.Label(canvas, image=bgimg)
    bg_label.place(relwidth=1, relheight=1)

    # Calculate the space between buttons
    button_space = 50  # Adjust this value as needed

    # Calculate button width and height
    button_width = 100

    # Calculate total width of buttons including space
    total_button_width = 2 * button_width + button_space

    # Calculate the starting x-coordinate for the first button
    start_x = (600 - total_button_width) / 2

    # Make the Register button
    register_button = tk.Button(canvas, text="Register", command=register_user_window, width=15, height=3)
    canvas.create_window(start_x, 180, anchor="nw", window=register_button)

    # Make the Login button
    login_button = tk.Button(canvas, text="Login", command=login_user_window, width=15, height=3)
    canvas.create_window(start_x + button_width + button_space, 180, anchor="nw", window=login_button)

    win.mainloop()


def main():

    mainWindow()

if __name__ == "__main__":

   main()

