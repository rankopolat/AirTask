import tkinter as tk
import Database
print("Fly Dream Air")
print("Group Project")

def login_user_window():
    rWindow.destroy()

def register_user():

    Database.conn.execute("INSERT INTO USER (USERNAME, EMAIL, PASSWORD) VALUES (?, ?, ?)", (rName_entry.get(), rEmail_entry.get(), rPass_entry.get()))

    rWindow.destroy()



    rWindow.destroy()
def register_user_window():

    global rWindow
    rWindow = tk.Toplevel(win)
    rWindow.geometry("400x300")

    rFrame = tk.Frame(rWindow)
    rFrame.pack(pady=20)

    global rName_entry, rEmail_entry, rPass_entry

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

# Create the main window
win = tk.Tk()
win.title("Fly Dream Air")
win.geometry("600x400")

# Create a frame for better organization
frame = tk.Frame(win)
frame.pack(pady=20)



register_button = tk.Button(frame, text="Register", command=register_user_window)
register_button.grid(row=3, columnspan=2, pady=20)

# Start the Tkinter event loop
win.mainloop()




'''Database.conn.execute("INSERT INTO USER (ID,NAME,AGE) \
      VALUES (1, 'Paul', 32)");

cursor = Database.conn.execute("SELECT id, name from USER")

for x in cursor:
    print("NAME =", x[1])

Database.conn.close()'''


'''win = tk.Tk()

win.geometry("1200x800")
win.title("Fly Dream Air")
greet = tk.Label(text="hellooo, im jesus")
greet.pack()
win.mainloop()'''

