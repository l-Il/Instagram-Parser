from instaloader import Instaloader, Profile
from tkinter import *


class Parser:
    def __init__(self):
        self.L = Instaloader()
        self.username = ''
        self.my_login = ''
        self.my_password = ''
        self.subscribers = []
        self.subscribed = []
        self.similar = []

        self.root = Tk()
        self.root.title('Instagram Parser')
        self.root.geometry('450x400')
        self.root.resizable(False, True)

        self.registration_frame = LabelFrame(self.root, text='Регистрация')
        self.my_login_entry = Entry(self.registration_frame)
        self.my_password_entry = Entry(self.registration_frame, show='*')
        self.status = Label(self.root, text='Можно посмотреть только открытые профили')
        self.username_entry = Entry(self.root)
        self.count_similar = Label(self.root, text='Взаимные:')
        self.subscribers_label = Label(self.root, text='')
        self.subscribed_label = Label(self.root, text='')
        self.similar_label = Label(self.root, text='')

        Label(self.registration_frame, text='Логин:').place(x=0, y=0)
        Label(self.registration_frame, text='Пароль:').place(x=0, y=20)
        self.my_login_entry.place(x=50, y=0, width=90)
        self.my_password_entry.place(x=50, y=20, width=90)
        self.registration_frame.place(x=0, y=0, width=150, height=65)
        self.status.place(x=150, y=0, width=300)
        Label(self.root, text='Ник:').place(x=150, y=20)
        self.username_entry.place(x=180, y=20, width=100)
        Button(self.root, text='Войти', relief=FLAT, border='0', command=self.press).place(x=150, y=45, height=20)
        Label(self.root, text='Подписчики:').place(x=0, y=65)
        Label(self.root, text='Подписки:').place(x=150, y=65)
        self.count_similar.place(x=300, y=65)
        self.subscribers_label.place(x=0, y=85, width=145, height=310)
        self.subscribed_label.place(x=150, y=85, width=145, height=310)
        self.similar_label.place(x=300, y=85, width=145, height=310)
        self.root.mainloop()

    def press(self):
        try:
            self.status['text'] = 'Загрузка. Подождите'
            self.root.update()
            self.username = self.username_entry.get()
            self.my_login = self.my_login_entry.get()
            self.my_password = self.my_password_entry.get()
            self.L.login(self.my_login, self.my_password)
            profile = Profile.from_username(self.L.context, self.username)

            for i in profile.get_followees():
                self.subscribed.append(i.username)
                self.subscribed_label['text'] = self.subscribed_label['text'] + '\n' + str(i.username)

            for i in profile.get_followers():
                self.subscribers.append(i.username)
                self.subscribers_label['text'] = self.subscribers_label['text'] + '\n' + str(i.username)

            for i in range(len(self.subscribers)):
                if self.subscribers[i] in self.subscribed:
                    self.similar.append(self.subscribers[i])
                    self.similar_label['text'] = self.similar_label['text'] + '\n' + str(self.subscribers[i])
                    self.count_similar['text'] = 'Взаимные: ' + str(len(self.similar))
            self.status['text'] = 'Готово!'
        except Exception as e:
            self.status['text'] = e


_ = Parser()
