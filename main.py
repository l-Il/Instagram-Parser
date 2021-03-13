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
        self.root.iconbitmap('favicon.ico')
        self.root.geometry('450x240')
        self.root.resizable(False, True)
        self.root.config(bg='#202020')

        self.registration_frame = LabelFrame(self.root, text='Регистрация', bg='#202020', fg='#CCCCCC')
        self.my_login_entry = Entry(self.registration_frame, bg='#202020', fg='#FFFFFF')
        self.my_password_entry = Entry(self.registration_frame, bg='#202020', fg='#FFFFFF', show='*')
        self.status = Label(self.root, text='Можно посмотреть только открытые профили', bg='#202020', fg='#CCCCCC')
        self.username_entry = Entry(self.root, bg='#202020', fg='#CCCCCC')
        self.count_similar = Label(self.root, text='Взаимные:', bg='#202020', fg='#CCCCCC')
        self.subscribers_label = Label(self.root, text='')
        self.subscribed_label = Label(self.root, text='')
        self.similar_label = Label(self.root, text='')

        Label(self.registration_frame, text='Логин:', bg='#202020', fg='#CCCCCC').place(x=0, y=0)
        Label(self.registration_frame, text='Пароль:', bg='#202020', fg='#CCCCCC').place(x=0, y=20)
        self.my_login_entry.place(x=51, y=0, width=90)
        self.my_password_entry.place(x=51, y=20, width=90)
        self.registration_frame.place(x=0, y=0, width=150, height=65)
        self.status.place(x=150, y=0, width=300)
        Label(self.root, text='Ник:', bg='#202020', fg='#CCCCCC').place(x=150, y=20, height=20)
        self.username_entry.place(x=181, y=20, width=110, height=20)
        Button(self.root, text='Войти', bg='#202020', fg='#FF0000', relief=FLAT, border='0', command=self.subs).place(x=150, y=41, height=24)
        Button(self.root, text='Скачать истории', bg='#202020', fg='#FF00FF', relief=FLAT, border='0', command=self.stories).place(x=190, y=41, height=24)
        Label(self.root, text='Подписчики:', bg='#202020', fg='#CCCCCC').place(x=0, y=65, height=20)
        Label(self.root, text='Подписки:', bg='#202020', fg='#CCCCCC').place(x=150, y=65, height=20)
        self.count_similar.place(x=300, y=65)
        self.subscribers_label.place(x=0, y=85, width=149, height=150)
        self.subscribed_label.place(x=150, y=85, width=149, height=150)
        self.similar_label.place(x=300, y=85, width=149, height=150)
        self.root.mainloop()

    def subs(self):
        try:
            self.status['text'] = 'Загрузка. Подождите'
            self.root.geometry('450x700')
            self.subscribers_label.place_forget()
            self.subscribed_label.place_forget()
            self.similar_label.place_forget()
            self.subscribers_label['text'] = ''
            self.subscribed_label['text'] = ''
            self.similar_label['text'] = ''
            self.subscribers_label.place(x=0, y=85, width=149, height=610)
            self.subscribed_label.place(x=150, y=85, width=149, height=610)
            self.similar_label.place(x=300, y=85, width=149, height=610)
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

    def stories(self):
        try:
            self.status['text'] = 'Загрузка. Подождите'
            self.root.update()
            self.username = self.username_entry.get()
            profile = self.L.check_profile_id(self.username)
            print(profile.userid)
            self.L.download_stories(userids=[profile.userid])
            self.status['text'] = 'Готово!'
        except Exception as e:
            self.status['text'] = e


_ = Parser()
