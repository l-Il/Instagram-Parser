import instaloader
from tkinter import *


class Parser:
    def __init__(self):
        self.root = Tk()
        self.root.title('Instagram Parser')
        self.root.geometry('400x400')
        self.root.resizable(False, True)

        self.registration_frame = LabelFrame(self.root, text='Регистрация')
        Label(self.registration_frame, text='Логин:').place(x=0, y=0)
        Label(self.registration_frame, text='Пароль:').place(x=0, y=20)
        self.registration_frame.place(x=0, y=0, width=120, height=70)
        self.root.mainloop()


_ = Parser()
