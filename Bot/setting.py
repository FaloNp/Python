import glob
import variable
import tkinter as tk
class Setting:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.title("Setting")
        self.width=500
        self.clicked=0

        self.leftColumn = tk.Label(self.root, bg="white")
        self.leftColumn.place(relwidth=0.5, relheight=1, relx=0, rely=0)

        self.header=tk.Label(self.leftColumn, text="Lista wykrytych szablonow")
        self.header.pack()
        filename = glob.glob('*.txt')  # wyciaganie nazw wszystkich plikow tekstowtych do zmiennej filename
        for i, name in enumerate(filename):  # przekazuje tekst z fumckji tk.Entry
            x = tk.Button(self.leftColumn, bg="orange", text=name,command=lambda:self.fun(i))
            x.place(relwidth=1, relheight=0.05, relx=0, rely=0 + i * 0.05)

        self.rightColumn = tk.Label(self.root)
        self.rightColumn.place(relwidth=0.5, relheight=1, relx=0.5, rely=0)

        self.buttonLoad = tk.Button(self.rightColumn, text="LOAD", command=self.set_fun,state=tk.DISABLED)
        self.buttonLoad.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.4)

        self.root.attributes('-topmost', True)

    def set_fun(self):
        print("Set")
        self.root.destroy()

    def check_state_fun(self):
        """Update button states based on the program's run state"""
        if self.clicked:
            self.buttonLoad.config(state=tk.NORMAL)
        else:
            self.buttonLoad.config(state=tk.DISABLED)
        self.root.update()

    def fun(self,i):
        print(i)
        self.clicked=1
        self.check_state_fun()