import tkinter as tk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Resources\clientImages")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def faqOnClick(event):
    frame.destroy()
    faqWindow()

def mainClientWindow():

    global window

    window = tk.Tk()
    window.title("Fly Dream Air")
    window.geometry("1280x720")

    clientWindow()

    window.resizable(False, False)
    window.mainloop()

def clientWindow():

    global frame

    frame = tk.Frame(window, bg="#FFFFFF")
    frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(
        frame,
        bg="#EFFBFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    global circlePlane
    circlePlane = tk.PhotoImage(file=relative_to_assets("circlePlane.png"))
    canvas.create_image(1056.0,100.0,image=circlePlane)

    global lock
    lock = tk.PhotoImage(file=relative_to_assets("lock.png"))
    canvas.create_image(1234.0, 55.0, image=lock)

    global faqButton
    faqButton = tk.PhotoImage(file=relative_to_assets("faqButton.png"))
    image_3 = canvas.create_image(972.0,51.0,image=faqButton)
    canvas.tag_bind(image_3, '<Button-1>', faqOnClick)

    global image_image_4
    image_image_4 = tk.PhotoImage(file=relative_to_assets("loyaltyStoreButton.png"))
    image_4 = canvas.create_image(838.0,51.0,image=image_image_4)

    global image_image_5
    image_image_5 = tk.PhotoImage(file=relative_to_assets("aboutButton.png"))
    image_5 = canvas.create_image(685.0,51.0,image=image_image_5)

    global image_image_6
    image_image_6 = tk.PhotoImage(file=relative_to_assets("splashInfo.png"))
    image_6 = canvas.create_image(303.0,391.0,image=image_image_6)

    global image_image_7
    image_image_7 = tk.PhotoImage(file=relative_to_assets("loyaltyButton.png"))
    image_7 = canvas.create_image(220.0,559.0,image=image_image_7)

    global image_image_8
    image_image_8 = tk.PhotoImage(file=relative_to_assets("chessIconv.png"))
    image_8 = canvas.create_image(72.0,61.0,image=image_image_8)

    global image_image_9
    image_image_9 = tk.PhotoImage(file=relative_to_assets("holder.png"))
    image_9 = canvas.create_image(198.0,66.0,image=image_image_9)

def faqWindow():

    global frame
    frame = tk.Frame(window, bg="#FFFFFF")
    frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(
        frame,
        bg="#EFFBFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    global image_image_1
    image_image_1 = tk.PhotoImage(
        file=relative_to_assets("lock.png"))
    image_1 = canvas.create_image(
        1234.0,
        55.0,
        image=image_image_1
    )

    global image_image_2
    image_image_2 = tk.PhotoImage(
        file=relative_to_assets("clickedFAQ.png"))
    image_2 = canvas.create_image(
        972.0,
        51.0,
        image=image_image_2
    )

    global image_image_3
    image_image_3 = tk.PhotoImage(
        file=relative_to_assets("loyaltyStoreButton.png"))
    image_3 = canvas.create_image(
        838.0,
        51.0,
        image=image_image_3
    )

    global image_image_4
    image_image_4 = tk.PhotoImage(
        file=relative_to_assets("aboutButton.png"))
    image_4 = canvas.create_image(
        685.0,
        51.0,
        image=image_image_4
    )

    global image_image_5
    image_image_5 = tk.PhotoImage(
        file=relative_to_assets("chessIconv.png"))
    image_5 = canvas.create_image(72.0,61.0,image=image_image_5
    )

    global image_image_6
    image_image_6 = tk.PhotoImage(
        file=relative_to_assets("holder.png"))
    image_6 = canvas.create_image(
        198.0,
        66.0,
        image=image_image_6
    )

    global image_image_7
    image_image_7 = tk.PhotoImage(
        file=relative_to_assets("faqHolder.png"))
    image_7 = canvas.create_image(
        639.0,
        151.0,
        image=image_image_7
    )

    global image_image_8
    image_image_8 = tk.PhotoImage(
        file=relative_to_assets("loyaltyHolder.png"))
    image_8 = canvas.create_image(
        195.0,
        198.0,
        image=image_image_8
    )

    global image_image_9
    image_image_9 = tk.PhotoImage(
        file=relative_to_assets("loyaltyInfo.png"))
    image_9 = canvas.create_image(
        635.0,
        284.0,
        image=image_image_9
    )

    global image_image_10
    image_image_10 = tk.PhotoImage(
        file=relative_to_assets("pointsHolder.png"))
    image_10 = canvas.create_image(
        200.0,
        381.0,
        image=image_image_10
    )

    global image_image_11
    image_image_11 = tk.PhotoImage(
        file=relative_to_assets("pointsInfo.png"))
    image_11 = canvas.create_image(
        637.0,
        458.0,
        image=image_image_11
    )

    global image_image_12
    image_image_12 = tk.PhotoImage(
        file=relative_to_assets("requireHolder.png"))
    image_12 = canvas.create_image(
        292.0,
        546.0,
        image=image_image_12
    )

    global image_image_13
    image_image_13 = tk.PhotoImage(
        file=relative_to_assets("requireInfo.png"))
    image_13 = canvas.create_image(
        650.0,
        631.0,
        image=image_image_13
    )
