import tkinter as tk
import time
from pynput.keyboard import Controller

import add
import function
import setting
import variable

#flagi globalne do sprawdzania stanu programu
isOpen = 0
run=False
buttonId=[]
buttonTime=[]

keyboard = Controller()
size=variable.main_Width+"x"+variable.main_Height
size_width=int(variable.main_Width)
size_height=int(variable.main_Height)

#Funkcje
def check_state_fun():
    """Update button states based on the program's run state"""
    if run:
        buttonStart.config(state=tk.DISABLED)
        buttonAdd.config(state=tk.DISABLED)
        buttonSetting.config(state=tk.DISABLED)
        buttonStop.config(state=tk.NORMAL)
    else:
        buttonStart.config(state=tk.NORMAL)
        buttonAdd.config(state=tk.NORMAL)
        buttonSetting.config(state=tk.NORMAL)
        buttonStop.config(state=tk.DISABLED)
    root.update()
def clock_fun(i):
    """Countdown clock function"""
    if i > 0:
        clock.config(text=f'{i}')
        root.after(1000, clock_fun, i - 1)
    else:
        clock.config(text=" ")
        start_fun()
def label_reset_fun(labellist):
    """Reset the background color of labels in the list"""
    for i, id in enumerate(labellist):
        labellist[i].config(bg='white')
    root.update()
def start_fun():
    global run
    if not buttonId or not buttonTime:
        error = "Wybierz najpierw przyciski"
        function.error_fun(error)
    else:
        run=True
        check_state_fun()
        label_reset_fun(labelIdButtonList)
        label_reset_fun(labelTimeButtonList)
        for i, id in enumerate(buttonId):
            labelIdButtonList[i].config(bg='green')
            labelTimeButtonList[i].config(bg='green')
            root.update()
            if not run:  #Sprawdza czy program powinnien w tym momencie byc uruchomiony
                break
            keyboard.press(id)
            time.sleep(int(buttonTime[i]))
            keyboard.release(id)
            labelIdButtonList[i].config(bg='white')
            labelTimeButtonList[i].config(bg='white')
            root.update()
        run=False
        check_state_fun()
def stop_fun():
    global run
    run = False
    check_state_fun()
def add_button_fun():
    addButton=add.Add()
def open_setting_fun():
    settingButton=setting.Setting()
def exit_fun():
    root.destroy()




#Wczytywanie potrzebnych danych
try:
    information=function.file_read_fun(variable.file_Name) #pobieranie informacji z pliku, dane sa zapisane w formacie [a b] gdzie a to przycisk ktory ma byc symulowany, b to czas
    buttonId=function.spliter_fun(information,0) #rozbicie tablicy i pobranie parametru a
    buttonTime=function.spliter_fun(information,1) #rozbicie tablicy i pobranie parametru b
except Exception as e:
    function.error_fun(e)


root = tk.Tk()  #tworzenie nowego okienka
root.geometry(size) #wymiary okienka
root.resizable(True,True)
root.minsize(width=500, height=500)
root.title("Bot")

mainFrame = tk.Frame(root)  #tworzy glowna ramke programu na ktorej beda umieszczane nastepne elementy
mainFrame.pack(fill=tk.BOTH, expand=True) #ustawia rozmiary ramki na takie jakie ma glowne okienko root
#lewa kolumna
leftColumn=tk.Canvas(mainFrame,width=size_width/2)
leftColumn.grid(row=0, column=0, sticky="nsew")

#prawa kolumna
rightColumn=tk.Frame(mainFrame,bg="green",width=size_width/2)
rightColumn.grid(row=0, column=1, sticky="nsew")

#ustawianie siatki 1x2
mainFrame.grid_rowconfigure(0, weight=1)
mainFrame.grid_columnconfigure(0, weight=1)
mainFrame.grid_columnconfigure(1, weight=1)


#Ukladanie elementow w lewej kolumnie
#scrollbar = tk.Scrollbar(leftColumn, orient="vertical") jezeli bedzie mi sie chcialo to dodam scrollbar
counter=0

idLabelList=[] #Inicjowanie tablicy w ktorej beda przechowywane nastepe obiekty "label" by sie pozniej do nich odnieść
labelIdButtonList=[]
labelTimeButtonList=[]

headerLabel = tk.Label(leftColumn, text="BUTTON LIST")
headerLabel.place(relwidth=1, relheight=0.1)
#Dynamiczna tabela (Ilosc elementow label jest zalezna od bazy danych information)
for item in buttonId:
    label=tk.Label(leftColumn)
    label.place(relwidth=1, relheight=0.1, relx=0, rely=0.1*(counter+1))
    labelIdButton=tk.Label(label,text=item,bg="white")
    labelIdButton.place(relwidth=0.5,relheight=1)
    labelTimeButton = tk.Label(label, text=buttonTime[counter],bg="white")
    labelTimeButton.place(relwidth=0.5,relheight=1,relx=0.5)
    labelIdButtonList.append(labelIdButton)
    labelTimeButtonList.append(labelTimeButton)
    idLabelList.append(label)
    counter=counter+1
#idLabelList[2].config(bg='white') #linia sprawdzajaca czy wszystko jest poprawnie polaczone
#labelIdButtonList[2].config(bg='green') #linia sprawdzajaca czy wszystko jest poprawnie polaczone
#labelTimeButtonList[2].config(bg='green') #linia sprawdzajaca czy wszystko jest poprawnie polaczone

#Ukladanie elementow w prawej kolumnie
clock = tk.Label(rightColumn, text="", bg="white")
clock.place(relwidth=0.1, relheight=0.1, relx=0.1, rely=0.1)
#Dodawanie panelu sterowania
buttonStart = tk.Button(root, text="Start", command=lambda:clock_fun(5))
buttonStart.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.1)
buttonAdd = tk.Button(root, text="Dodaj przycisk", command=add_button_fun)
buttonAdd.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.25)
buttonStop = tk.Button(root, text="Stop", command=stop_fun, state=tk.DISABLED)
buttonStop.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.4)
buttonSetting = tk.Button(root, text="Ustawienia", command=open_setting_fun)
buttonSetting.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.55)
buttonExit = tk.Button(root, text="Wyjscie", command=exit_fun)
buttonExit.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.7)

root.mainloop()
