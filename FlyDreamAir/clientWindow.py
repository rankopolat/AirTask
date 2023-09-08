import tkinter as tk

def clientWindow():
    window = tk.Tk()

    window.geometry("1555x879")
    window.configure(bg="#FFE9F9")

    canvas = tk.Canvas(
        window,
        bg="#FFE9F9",
        height=879,
        width=1555,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        266.0,
        543.0,
        1290.0,
        800.0,
        fill="#FFFFFF",
        outline="")

    button_image_1 = tk.PhotoImage(
        file=("Resources/b1.png"))
    button_1 = tk.Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=286.0,
        y=563.0,
        width=208.0,
        height=217.0
    )

    button_image_2 = tk.PhotoImage(
        file=("Resources/b2.png"))
    button_2 = tk.Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=1060.0,
        y=563.0,
        width=208.0,
        height=217.0
    )

    button_image_3 = tk.PhotoImage(
        file=("Resources/b3.png"))
    button_3 = tk.Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=802.0,
        y=563.0,
        width=208.0,
        height=217.0
    )

    button_image_4 = tk.PhotoImage(
        file=("Resources/b4.png"))
    button_4 = tk.Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=544.0,
        y=563.0,
        width=208.0,
        height=217.0
    )
    window.resizable(False, False)
    window.mainloop()

