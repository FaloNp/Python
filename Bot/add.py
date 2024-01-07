import tkinter as tk
import function
import variable

class Add:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Add button to list")
        self.root.geometry("500x200")

        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack(fill=tk.BOTH, expand=True)

        self.idLabel = tk.Label(self.mainFrame, text="Button ID")
        self.idLabel.place(relwidth=1, relheight=0.1, rely=0.1)

        self.idEntry = tk.Entry(self.mainFrame)
        self.idEntry.place(relwidth=0.5, relheight=0.1, rely=0.2, relx=0.1)

        self.timeLabel = tk.Label(self.mainFrame, text="Time press [s]")
        self.timeLabel.place(relwidth=1, relheight=0.1, rely=0.5)

        self.timeEntry = tk.Entry(self.mainFrame)
        self.timeEntry.place(relwidth=0.5, relheight=0.1, relx=0.1, rely=0.7)

        #uzywam lambdy poniewaz funkcja dataIntegrator wymaga podania argumentow
        self.setconfiguration = tk.Button(self.mainFrame, text="Set", command=lambda:self.data_integrator_fun(self.idEntry.get(), self.timeEntry.get()))
        self.setconfiguration.place(relwidth=0.2, relheight=0.1, relx=0.7, rely=0.75)
        self.root.attributes('-topmost', True)
    def data_integrator_fun(self,id,time):
        if not id or not time:
            #sprawdzanie czy zmienne nie sa puste
            function.error_fun(variable.listError[2])
            return
        else:
            if len(id) != 1:
                #sprawdzanie czy zmienna id sklada sie z jednego przycisku
                function.error_fun(variable.listError[3])
                return
            else:
                #sprawdzanie czy zmienna time zawiera znaki nie bedace liczbami
                for item in time:
                    if item.isalpha():
                        function.error_fun(variable.listError[4])
                        return
                print("Correct!")
