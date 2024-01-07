import tkinter as tk
from PIL import Image, ImageTk

class Error:
    def __init__(self,info):
       self.root = tk.Tk()
       self.root.geometry("500x200")
       self.root.resizable(False, False)
       self.root.title("Error!")
       self.info=info
       self.path = "photo/error.png"
       print(self.info)
       # Load the image using Pillow
       self.image_file = Image.open(self.path)
       self.image = ImageTk.PhotoImage(self.image_file)

       self.mainFrame = tk.Frame(self.root)
       self.mainFrame.pack(fill=tk.BOTH, expand=True)

       self.leftColumn = tk.Frame(self.mainFrame)
       self.leftColumn.place(relwidth=0.5, relheight=1, relx=0, rely=0)

       #nie mam pojecia czemu nie dziala xd
       #self.label = tk.Label(self.leftColumn, image=self.image)
       #self.label.pack()

       self.rightColumn = tk.Frame(self.mainFrame)
       self.rightColumn.place(relwidth=0.5, relheight=1, relx=0.5, rely=0)

       self.informationFrame=tk.Frame(self.rightColumn)
       self.informationFrame.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.25)
       self.errorinfo = tk.Label(self.informationFrame, text="Error!")
       self.errorinfo.pack()
       self.errordescription = tk.Label(self.informationFrame, text=self.info)
       self.errordescription.pack()

       self.button = tk.Button(self.root, text="Ok", command=self.exit_fun)
       self.button.place(relwidth=0.1, relheight=0.2, relx=0.7, rely=0.7)
       self.root.attributes('-topmost', True)
       self.root.mainloop()

    def exit_fun(self):
        self.root.destroy()


'''
#########################################################################################################
def Active(nazwa):
    x = Label(box, bg="green", text="aktywny")
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


'''