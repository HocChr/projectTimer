import tkinter as tk
from tkinter import messagebox
from tkinter import *
import time


def deleteme(currProj):
    result = messagebox.askquestion("Projektwechsel?", "Arbeitest Du noch am Projekt: " + currProj + " ?", icon='warning')
    if result == 'yes':
        return True
    else:
        return False


root = tk.Tk()  #to avoid second window shown
root.withdraw() #to avoid second window shown


class ProjSelectorUi():
    def __init__(self, currProj, projList):
        self._choosenProj = currProj
        self._projList = projList

        self.callbackOkay = lambda: None

    def getSelectedProj(self):
        return self._choosenProj

    def getProjList(self):
        return self._projList

    def _setupUi(self):
        self._variable = StringVar(root)
        self._variable.set(self._choosenProj)  # default value

        root.Label1 = Label(text="Aktuelles Projekt und Projektauswahl:")
        root.Label1.pack()

        self._w = OptionMenu(root, self._variable, *self._projList, command=self._setChoosenProj)
        self._w.pack()

        root.Label2 = Label(text="------------------------------------")
        root.Label2.pack()

        root.button1 = Button(text="Aktuelles Projekt löschen", command=self._onItemDeleted)
        root.button1.pack()

        root.Label3 = Label(text="------------------------------------")
        root.Label3.pack()

        self._entry = Entry(root)
        self._entry.pack()
        root.button2 = Button(text="Neues Projekt anlegen", command=self._onNewProject)
        root.button2.pack()

        root.Label4 = Label(text="------------------------------------")
        root.Label4.pack()

        root.button3 = Button(text="Speichern und schließen", command=self._onQkayClicked)
        root.button3.pack()

    def _onNewProject(self):
        if not self._entry.get():
            return
        if self._entry.get() in self._projList:
            self._entry.delete(0, END)
            self._entry.insert(0, "SCHON VORHANDEN!")
            root.update()
            time.sleep(3)
            self._entry.delete(0, END)
            return
        self._projList = [self._entry.get()] + self._projList
        self._choosenProj = self._entry.get()
        menu = self._w["menu"]
        menu.delete(0, "end")
        for string in self._projList:
            menu.add_command(label=string,
                             command=lambda value=string: self._variable.set(value))
        self._variable.set(self._choosenProj)
        self._entry.delete(0, END)

    def _setChoosenProj(self, value):
        self._choosenProj = value

    def _onItemDeleted(self):
        if len(self._projList) == 0:
            return
        menu = self._w["menu"]
        menu.delete(0, "end")
        self._projList.remove(self._choosenProj)
        for string in self._projList:
            menu.add_command(label=string,
                             command=lambda value=string: self._variable.set(value))
        if not len(self._projList) == 0:
            self._variable.set(self._projList[0])
        else:
            self._variable.set('')
        self._choosenProj = self._variable.get()

    def _onQkayClicked(self):
        root.destroy()
        self.callbackOkay()

    def run(self):
        root.deiconify()
        self._setupUi()
        root.mainloop()




