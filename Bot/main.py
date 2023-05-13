from tkinter import *
from pynput.keyboard import Key, Controller
import time
import glob
import threading

keyboard = Controller()
root = Tk()  # tworzenie nowego okienka
root.resizable(width=FALSE, height=FALSE)
IsOpen = 0  # flaga sprawdzajaca czy okienko jest juz otworzone np kiedy kilka razy kliknie sie przycisk ustawienie
global ButtonList
ButtonList = []
global PressList
PressList = []



def Start():  # funkcja przycisku ktora otwiera nowe okno
    if ButtonList:
        Clock()
        time.sleep(5)
        for i, nazwa in enumerate(ButtonList):
            Active(nazwa)
            keyboard.press(nazwa)
            time.sleep(int(PressList[i]))
            keyboard.release(nazwa)
    else:
        error="Wybierz najpierw przyciski"
        Error(error)
def Clock():
    i = 5
    while (i > 0):
        clock = Label(root, text=f'{i}', bg="white")
        clock.place(relwidth=0.05, relheight=0.07, relx=0.59, rely=0.114)
        time.sleep(1)
        i = i - 1
        clock.destroy()
def Error(errortext):
    def Error_Exit():
        error.destroy()
    error = Tk()
    error.resizable(width=FALSE, height=FALSE)
    error.title("Blad")
    boxerror = Frame(error, height=150, width=300)
    errorlabel = Label(error, text=errortext)
    errorlabel.place(relwidth=1, relheight=0.1, rely=0.3)
    error_exit = Button(error, text="Wyjscie", command=Error_Exit)
    error_exit.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.7)
    boxerror.pack()
    error.attributes('-topmost', True)
def OpenSetting():  # funkcja przycisku ktora otwiera nowe okno
    setting = Tk()
    setting.resizable(width=FALSE, height=FALSE)
    setting.title("Ustawienia")
    boxsetting = Frame(setting, height=900, width=500)

    # buttony
    button_add = Button(setting, text="Zapisz", command=NewFile)
    button_add.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.1)
    button_add = Button(setting, text="Wczytaj", command=Load)
    button_add.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.25)
    button_setting_exit = Button(setting, text="Wyjscie", command=lambda: setting.destroy())
    button_setting_exit.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.5)

    # pojemnik
    buttonlist = Canvas(setting, bg="brown", height=200, width=300)
    buttonlist.place(relwidth=0.5, relheight=0.5, rely=0.05)
    buttonInformation = Label(setting, text="Lista wykrytych szablonow")
    buttonInformation.place(rely=0.0, relwidth=0.5)
    filename = glob.glob('*.txt')  # wyciaganie nazw wszystkich plikow tekstowtych do zmiennej filename
    for i, nazwa in enumerate(filename):  # przekazuje tekst z fumckji tk.Entry
        x = Label(buttonlist, bg="orange", text=nazwa)
        x.place(relwidth=1, relheight=0.05, relx=0, rely=0 + i * 0.05)
    boxsetting.pack()



def File():
    file = open("file.txt", "w")
    for i, nazwa in enumerate(ButtonList):
        file.writelines(nazwa + " " + PressList[i])
        file.writelines("\n")


def Load():
    file = open("file.txt", "r")
    file = file.readlines()
    Reset()
    for line in file:
        SetOption(line[0], line[2])
def NewFile():
    if ButtonList:
        print("zapisano")
        file = open("filenowyszablon.txt", "w")
        for i, nazwa in enumerate(ButtonList):  # przekazuje tekst z funkcji tk.Entry
            file.write(nazwa + " " + PressList[i] + "\n")


    else:
        error = "Nie wlasciwy szablon"
        Error(error)
    Reset()

def Exit():
    root.destroy()
#########################################################################################################
def Active(nazwa):
    print("sloflsofgko")
    x = Label(box, bg="green", text="pdkaokdoakdoakdeaokoderzez")
    x.place(relwidth=1, relheight=0.05, relx=0, rely=0 + 2 * 0.05)
    x.attributes('-topmost', True)
###################################################################################################################
def SetOption(x, y):
    if len(x) == 1:
        ButtonList.append(x)
        if y.isdigit():
            PressList.append(y)
            for i, nazwa in enumerate(ButtonList):  # przekazuje tekst z funkcji tk.Entry
                x = Label(buttonlist, justify='left', bg="orange", text=nazwa + " przez " + PressList[i])
                x.place(relwidth=1, relheight=0.05, relx=0, rely=0 + i * 0.05)
        else:
            error = "Wartosc powinna byc liczba"
            Error(error)
    else:
        error="Przycisk powienien byc pojedyncz"
        Error(error)
def Reset():
    del PressList[:]
    del ButtonList[:]
def AddButton():
    addbutton = Tk()
    addbutton.resizable(width=FALSE, height=FALSE)
    addbutton.title("Dodaj przycisk")
    boxaddbutton = Frame(addbutton, height=200, width=300)
    information = Label(addbutton, text="Przycisk do dodania")
    information.place(relwidth=1, relheight=0.1, rely=0.1)
    entrybutton = Entry(addbutton)
    entrybutton.place(relwidth=0.5, relheight=0.1, rely=0.2, relx=0.1)
    informationhowlong = Label(addbutton, text="Przez ile sekund przytrzymac przycisk")
    informationhowlong.place(relwidth=1, relheight=0.1, rely=0.5)
    entryhowlong = Entry(addbutton)
    entryhowlong.place(relwidth=0.2, relheight=0.1, relx=0.1, rely=0.7)
    setconfiguration = Button(addbutton, text="Set", command=lambda: SetOption(entrybutton.get(), entryhowlong.get()))
    setconfiguration.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.75)
    boxaddbutton.pack()
    addbutton.attributes('-topmost', True)


box = Frame(root, height=500, width=1200)  # tworzy okienko o parametrach
box.pack()
# lista z informacjami o przyciskach
buttonlist = Canvas(box, bg="brown", height=200, width=300)
buttonlist.place(relwidth=0.5, relheight=0.9, rely=0.05)
buttonInformation = Label(root, text="Lista dodanych przyciskow")
buttonInformation.place(rely=0.0, relwidth=0.5)


# buttony
button_add = Button(root, text="Start", command=Start)
button_add.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.1)
button_add = Button(root, text="Dodaj przycisk", command=AddButton)
button_add.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.25)
button_setting = Button(root, text="Stop", command=OpenSetting)
button_setting.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.4)
button_setting = Button(root, text="Ustawienia", command=OpenSetting)
button_setting.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.55)
button_add = Button(root, text="Wyjscie", command=Exit)
button_add.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.7)


root.mainloop()
