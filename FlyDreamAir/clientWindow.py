import tkinter as tk
from pathlib import Path
from Database import Database

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Resources\clientImages")

text = ""
def updateInfo(user):

    global username, tier, points, email
    loginCursor = Database.conn.execute("SELECT USERNAME,TIER,POINTS,EMAIL FROM USER WHERE USERNAME = ?", (user,))
    results = loginCursor.fetchone()
    username = results[0]
    tier = results[1]
    points = results[2]
    email = results[3]

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def faqOnClick(event):
    frame.destroy()
    updateInfo(username)
    faqWindow()

def homeClick(event):
    frame.destroy()
    updateInfo(username)
    clientWindow()

def loyalOnClick(event):
    frame.destroy()
    updateInfo(username)
    loyaltyWindow()

def accountOnClick(event):
    frame.destroy()
    updateInfo(username)
    accountWindow()

def basketOnClick(event):
    frame.destroy()
    updateInfo(username)
    cartWindow()

def itemOnClick(item):

    print(f"Clicked item {item}")

    match item:
        case 1:
            print("Item 1")
        case 2:
            print("Item 2")
        case 3:
            print("Item 3")
        case 4:
            print("Item 4")
        case 5:
            print("Item 5")
        case 6:
            print("Item 6")
        case 7:
            print("Item 7")
        case 8:
            print("Item 8")
        case 9:
            print("Item 9")
        case 10:
            print("Item 10")
        case 11:
            print("Item 11")
        case 12:
            print("Item 12")
        case 13:
            print("Item 13")


def update_text():

    global text
    Database.conn.execute("UPDATE USER SET TIER = ? WHERE USERNAME = ?", ("SILVER", username))
    Database.conn.commit()

    updated = f"{text}\n{username,tier,points}"

    text = f"{text}\n{updated}"



def mainClientWindow(user):

    updateInfo(user)

    global window
    window = tk.Tk()
    window.title("Fly Dream Air")
    window.geometry("1280x720")

    clientWindow()

    window.resizable(False, False)
    window.mainloop()

def accountWindow():

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
    canvas.create_image(300.0,380.0, image=circlePlane)

    global account
    account = tk.PhotoImage(
        file=relative_to_assets("clickedAccount.png"))
    canvas.create_image(550.0, 51.0, image=account)

    global lock
    lock = tk.PhotoImage(file=relative_to_assets("lock.png"))
    cart = canvas.create_image(1234.0, 55.0, image=lock)
    canvas.tag_bind(cart, '<Button-1>', basketOnClick)

    global faqButton
    faqButton = tk.PhotoImage(file=relative_to_assets("faqButton.png"))
    image_3 = canvas.create_image(972.0, 51.0, image=faqButton)
    canvas.tag_bind(image_3, '<Button-1>', faqOnClick)

    global image_image_4
    image_image_4 = tk.PhotoImage(file=relative_to_assets("loyaltyStoreButton.png"))
    image_4 = canvas.create_image(838.0, 51.0, image=image_image_4)
    canvas.tag_bind(image_4, '<Button-1>', loyalOnClick)

    global image_image_5
    image_image_5 = tk.PhotoImage(file=relative_to_assets("aboutButton.png"))
    image_5 = canvas.create_image(685.0, 51.0, image=image_image_5)

    global image_image_8
    image_image_8 = tk.PhotoImage(file=relative_to_assets("chessIconv.png"))
    image_8 = canvas.create_image(72.0, 61.0, image=image_image_8)

    global image_image_9
    image_image_9 = tk.PhotoImage(file=relative_to_assets("holder.png"))
    image_9 = canvas.create_image(198.0, 66.0, image=image_image_9)

    canvas.create_text(
        118.0,
        336.0,
        anchor="nw",
        text=f"{username.upper()}",
        fill="#000000",
        font=("Poppins Bold", 32 * -1)
    )

    canvas.create_text(
        91.0,
        429.0,
        anchor="nw",
        text= f"Current Points: {points}",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    canvas.create_text(
        90.0,
        465.0,
        anchor="nw",
        text=f"Tier: {tier}",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    canvas.create_text(
        91.0,
        501.0,
        anchor="nw",
        text= f"Email: {email}",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    canvas.create_text(
        91.0,
        537.0,
        anchor="nw",
        text=f"Username: {username}",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    canvas.create_text(
        90.0,
        573.0,
        anchor="nw",
        text="Date of Birth:  ****",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    global accountIcon
    accountIcon = tk.PhotoImage(
        file=relative_to_assets("userIcon.png"))
    image_9 = canvas.create_image(
        208.0,
        232.0,
        image=accountIcon
    )

    global tierInfo
    tierInfo = tk.PhotoImage(
        file=relative_to_assets("tierInfo.png"))
    canvas.create_image(
        883.0,
        393.0,
        image=tierInfo
    )

def cartWindow():

    global frame
    frame = tk.Frame(window, bg="#FFFFFF")
    frame.pack(fill="both", expand=True)

    global canvas
    canvas = tk.Canvas(
        window,
        bg="#EFFBFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    global baskI
    baskI = tk.PhotoImage(
        file=relative_to_assets("basketIcon.png"))
    image_1 = canvas.create_image(
        1227.0,
        48.0,
        image=baskI
    )
    canvas.tag_bind(image_1, '<Button-1>', lambda event: update_text())


    global account
    account = tk.PhotoImage(
        file=relative_to_assets("account.png"))
    accountI = canvas.create_image(550.0, 51.0, image=account)
    canvas.tag_bind(accountI, '<Button-1>', accountOnClick)


    global faqButton
    faqButton = tk.PhotoImage(
        file=relative_to_assets("faqButton.png"))
    image_2 = canvas.create_image(
        972.0,
        51.0,
        image=faqButton
    )
    canvas.tag_bind(image_2, '<Button-1>', faqOnClick)

    global lB
    lB = tk.PhotoImage(
        file=relative_to_assets("loyaltyStoreButton.png"))
    image_3 = canvas.create_image(
        838.0,
        51.0,
        image=lB
    )
    canvas.tag_bind(image_3, '<Button-1>', loyalOnClick)


    global aB
    aB = tk.PhotoImage(
        file=relative_to_assets("aboutButton.png"))
    image_4 = canvas.create_image(
        685.0,
        51.0,
        image=aB
    )


    global cI
    cI = tk.PhotoImage(
        file=relative_to_assets("chessIconv.png"))
    image_5 = canvas.create_image(
        72.0,
        61.0,
        image=cI
    )
    canvas.tag_bind(image_5, '<Button-1>', homeClick)

    global textHolder
    textHolder = tk.PhotoImage(
        file=relative_to_assets("holder.png"))
    image_6 = canvas.create_image(
        198.0,
        66.0,
        image=textHolder
    )

    canvas.create_rectangle(
        315.0,
        166.0,
        991.0,
        701.0,
        fill="#FFFFFF",
        outline="")

    global shopTitle
    shopTitle = tk.PhotoImage(
        file=relative_to_assets("shopTitle.png"))
    image_7 = canvas.create_image(
        640.0,
        124.0,
        image=shopTitle
    )

    text_item = canvas.create_text(
        324.0,
        176.0,
        anchor="nw",
        text=f"{text}",
        fill="#000000",
        font=("Jaldi Bold", 32 * -1)
    )



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

    global account
    account = tk.PhotoImage(
        file=relative_to_assets("account.png"))
    accountB = canvas.create_image(550.0, 51.0, image=account)
    canvas.tag_bind(accountB, '<Button-1>', accountOnClick)

    global lock
    lock = tk.PhotoImage(file=relative_to_assets("lock.png"))
    cart = canvas.create_image(1234.0, 55.0, image=lock)
    canvas.tag_bind(cart, '<Button-1>', basketOnClick)

    global faqButton
    faqButton = tk.PhotoImage(file=relative_to_assets("faqButton.png"))
    image_3 = canvas.create_image(972.0,51.0,image=faqButton)
    canvas.tag_bind(image_3, '<Button-1>', faqOnClick)

    global image_image_4
    image_image_4 = tk.PhotoImage(file=relative_to_assets("loyaltyStoreButton.png"))
    image_4 = canvas.create_image(838.0,51.0,image=image_image_4)
    canvas.tag_bind(image_4, '<Button-1>', loyalOnClick)

    global image_image_5
    image_image_5 = tk.PhotoImage(file=relative_to_assets("aboutButton.png"))
    image_5 = canvas.create_image(685.0,51.0,image=image_image_5)

    global image_image_6
    image_image_6 = tk.PhotoImage(file=relative_to_assets("splashInfo.png"))
    image_6 = canvas.create_image(303.0,391.0,image=image_image_6)

    global image_image_7
    image_image_7 = tk.PhotoImage(file=relative_to_assets("loyaltyButton.png"))
    image_7 = canvas.create_image(220.0,559.0,image=image_image_7)
    canvas.tag_bind(image_7, '<Button-1>', loyalOnClick)

    global image_image_8
    image_image_8 = tk.PhotoImage(file=relative_to_assets("chessIconv.png"))
    image_8 = canvas.create_image(72.0,61.0,image=image_image_8)

    global image_image_9
    image_image_9 = tk.PhotoImage(file=relative_to_assets("holder.png"))
    image_9 = canvas.create_image(198.0,66.0,image=image_image_9)


def loyaltyWindow():

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

    global basket
    basket = tk.PhotoImage(
        file=relative_to_assets("lock.png"))
    cart = canvas.create_image(
        1234.0,
        55.0,
        image=basket
    )
    canvas.tag_bind(cart, '<Button-1>', basketOnClick)

    global account
    account = tk.PhotoImage(
        file=relative_to_assets("account.png"))
    accountI = canvas.create_image(550.0, 51.0, image=account)
    canvas.tag_bind(accountI, '<Button-1>', accountOnClick)

    global faqB
    faqB = tk.PhotoImage(
        file=relative_to_assets("faqButton.png"))
    image_2 = canvas.create_image(
        972.0,
        51.0,
        image=faqB
    )
    canvas.tag_bind(image_2, '<Button-1>', faqOnClick)

    global loyaltyC
    loyaltyC = tk.PhotoImage(
        file=relative_to_assets("lotaltyClicked.png"))
    image_3 = canvas.create_image(
        838.0,
        51.0,
        image=loyaltyC
    )

    global aboutB
    aboutB = tk.PhotoImage(
        file=relative_to_assets("aboutButton.png"))
    image_4 = canvas.create_image(
        685.0,
        51.0,
        image=aboutB
    )

    global ChessI
    ChessI = tk.PhotoImage(
        file=relative_to_assets("chessIconv.png"))
    image_5 = canvas.create_image(
        72.0,
        61.0,
        image=ChessI
    )
    canvas.tag_bind(image_5, '<Button-1>', homeClick)

    global textH
    textH = tk.PhotoImage(
        file=relative_to_assets("holder.png"))
    image_6 = canvas.create_image(
        198.0,
        66.0,
        image=textH
    )

    global shopItem1
    shopItem1 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_7 = canvas.create_image(
        332.0,
        287.0,
        image=shopItem1
    )
    canvas.tag_bind(image_7, '<Button-1>', lambda event, item=1: itemOnClick(item))

    global shopItem2
    shopItem2 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_8 = canvas.create_image(
        736.0,
        287.0,
        image= shopItem2
    )
    canvas.tag_bind(image_8, '<Button-1>', lambda event, item=2: itemOnClick(item))

    global shopItem3
    shopItem3 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_9 = canvas.create_image(
        945.0,
        287.0,
        image=shopItem3
    )
    canvas.tag_bind(image_9, '<Button-1>', lambda event, item=3: itemOnClick(item))

    global shopItem4
    shopItem4 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_10 = canvas.create_image(
        1146.0,
        287.0,
        image=shopItem4
    )
    canvas.tag_bind(image_10, '<Button-1>', lambda event, item=4: itemOnClick(item))

    global shopItem5
    shopItem5 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_11 = canvas.create_image(
        133.0,
        548.0,
        image=shopItem5
    )
    canvas.tag_bind(image_11, '<Button-1>', lambda event, item=5: itemOnClick(item))

    global shopItem6
    shopItem6 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_12 = canvas.create_image(
        332.0,
        548.0,
        image=shopItem6
    )
    canvas.tag_bind(image_12, '<Button-1>', lambda event, item=6: itemOnClick(item))

    global shopItem7
    shopItem7 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_13 = canvas.create_image(
        531.0,
        548.0,
        image=shopItem7
    )
    canvas.tag_bind(image_13, '<Button-1>', lambda event, item=7: itemOnClick(item))

    global shopItem8
    shopItem8 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_14 = canvas.create_image(
        736.0,
        548.0,
        image=shopItem8
    )
    canvas.tag_bind(image_14, '<Button-1>', lambda event, item=8: itemOnClick(item))

    global shopItem9
    shopItem9 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_15 = canvas.create_image(
        945.0,
        548.0,
        image=shopItem9
    )
    canvas.tag_bind(image_15, '<Button-1>', lambda event, item=9: itemOnClick(item))

    global shopItem10
    shopItem10 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_16 = canvas.create_image(
        1146.0,
        548.0,
        image=shopItem10
    )
    canvas.tag_bind(image_16, '<Button-1>', lambda event, item=10: itemOnClick(item))

    global shopItem11
    shopItem11 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_17 = canvas.create_image(
        531.0,
        287.0,
        image=shopItem11
    )
    canvas.tag_bind(image_17, '<Button-1>', lambda event, item=11: itemOnClick(item))

    global shopItem12
    shopItem12 = tk.PhotoImage(
        file=relative_to_assets("shopItem.png"))
    image_18 = canvas.create_image(
        133.0,
        287.0,
        image=shopItem12
    )
    canvas.tag_bind(image_18, '<Button-1>', lambda event, item=12: itemOnClick(item))

    global image_image_19
    image_image_19 = tk.PhotoImage(
        file=relative_to_assets("holder2.png"))
    image_19 = canvas.create_image(
        640.0,
        120.0,
        image=image_image_19
    )
    canvas.tag_bind(image_19, '<Button-1>', lambda event, item=13: itemOnClick(item))


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

    global account
    account = tk.PhotoImage(
        file=relative_to_assets("account.png"))
    accountI = canvas.create_image(550.0, 51.0, image=account)
    canvas.tag_bind(accountI, '<Button-1>', accountOnClick)

    global image_image_1
    image_image_1 = tk.PhotoImage(
        file=relative_to_assets("lock.png"))
    cart = canvas.create_image(
        1234.0,
        55.0,
        image=image_image_1
    )
    canvas.tag_bind(cart, '<Button-1>', basketOnClick)

    global image_image_2
    image_image_2 = tk.PhotoImage(
        file=relative_to_assets("clickedFAQ.png"))
    image_2 = canvas.create_image(972.0,51.0,image=image_image_2)

    global image_image_3
    image_image_3 = tk.PhotoImage(
        file=relative_to_assets("loyaltyStoreButton.png"))
    image_3 = canvas.create_image(838.0,51.0,image=image_image_3)
    canvas.tag_bind(image_3, '<Button-1>', loyalOnClick)


    global image_image_4
    image_image_4 = tk.PhotoImage(
        file=relative_to_assets("aboutButton.png"))
    image_4 = canvas.create_image(685.0,51.0,image=image_image_4)

    global image_image_5
    image_image_5 = tk.PhotoImage(
        file=relative_to_assets("chessIconv.png"))
    image_5 = canvas.create_image(72.0,61.0,image=image_image_5
    )
    canvas.tag_bind(image_5, '<Button-1>', homeClick)

    global image_image_6
    image_image_6 = tk.PhotoImage(
        file=relative_to_assets("holder.png"))
    image_6 = canvas.create_image(198.0,66.0,image=image_image_6)

    global image_image_7
    image_image_7 = tk.PhotoImage(
        file=relative_to_assets("faqHolder.png"))
    image_7 = canvas.create_image(639.0,151.0,image=image_image_7)

    global image_image_8
    image_image_8 = tk.PhotoImage(
        file=relative_to_assets("loyaltyHolder.png"))
    image_8 = canvas.create_image(195.0,198.0,image=image_image_8)

    global image_image_9
    image_image_9 = tk.PhotoImage(
        file=relative_to_assets("loyaltyInfo.png"))
    image_9 = canvas.create_image(635.0,284.0,image=image_image_9)

    global image_image_10
    image_image_10 = tk.PhotoImage(
        file=relative_to_assets("pointsHolder.png"))
    image_10 = canvas.create_image(200.0,381.0,image=image_image_10)

    global image_image_11
    image_image_11 = tk.PhotoImage(
        file=relative_to_assets("pointsInfo.png"))
    image_11 = canvas.create_image(610.0,458.0,image=image_image_11)

    global image_image_12
    image_image_12 = tk.PhotoImage(
        file=relative_to_assets("requireHolder.png"))
    image_12 = canvas.create_image(292.0,546.0,image=image_image_12)

    global image_image_13
    image_image_13 = tk.PhotoImage(
        file=relative_to_assets("requireInfo.png"))
    image_13 = canvas.create_image(650.0,631.0,image=image_image_13)
