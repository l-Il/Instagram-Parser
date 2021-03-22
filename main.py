from instaloader import Instaloader, Profile
from tkinter import *


class Parser:
    def __init__(self):
        self.L = Instaloader()
        self.username = ''
        self.second_username = ''
        self.first_username = ''
        self.my_login = ''
        self.my_password = ''
        self.list1 = []
        self.list2 = []
        self.list3 = []

        self.root = Tk()
        self.root.title('Instagram Parser')
        self.root.iconbitmap('favicon.ico')
        self.root.geometry('450x70')
        self.root.resizable(False, True)
        self.root.config(bg='#202020')

        self.registration_frame = LabelFrame(self.root, text='Регистрация', bg='#202020', fg='#CCCCCC')
        self.my_login_entry = Entry(self.registration_frame, bg='#202020', fg='#FFFFFF')
        self.my_password_entry = Entry(self.registration_frame, bg='#202020', fg='#FFFFFF', show='*')
        self.status = Label(self.root, text='Можно посмотреть только открытые профили', bg='#202020', fg='#CCCCCC')
        self.username_entry = Entry(self.root, bg='#202020', fg='#CCCCCC')
        self.second_username_entry = Entry(self.root, bg='#202020', fg='#CCCCCC')
        self.count_similar = Label(self.root, text='Взаимные:', bg='#202020', fg='#CCCCCC')

        self.subscribers_text = Text(self.root)
        self.subscribed_text = Text(self.root)
        self.similar_text = Text(self.root)

        Label(self.registration_frame, text='Логин:', bg='#202020', fg='#CCCCCC').place(x=0, y=0)
        Label(self.registration_frame, text='Пароль:', bg='#202020', fg='#CCCCCC').place(x=0, y=20)
        self.my_login_entry.place(x=51, y=0, width=90)
        self.my_password_entry.place(x=51, y=20, width=90)
        self.registration_frame.place(x=0, y=0, width=150, height=65)
        self.status.place(x=150, y=0, width=300)
        Label(self.root, text='Ник:', bg='#202020', fg='#CCCCCC').place(x=150, y=20, height=20)
        self.username_entry.place(x=181, y=20, width=100, height=20)
        Label(self.root, text='Ник:', bg='#202020', fg='#CCCCCC').place(x=281, y=20, height=20)
        self.second_username_entry.place(x=315, y=20, width=100, height=20)
        Button(self.root, text='Посмотреть взаимных', bg='#202020', fg='#FF0000', relief=FLAT, border='0', command=self.subs).place(x=150, y=41, height=24)
        Button(self.root, text='Скачать истории', bg='#202020', fg='#FF00FF', relief=FLAT, border='0', command=self.stories).place(x=285, y=41, height=24)
        Button(self.root, text='Общие', bg='#202020', fg='#FFFF00', relief=FLAT, border='0', command=self.find_similar).place(x=390, y=41, height=24)

        self.root.mainloop()

    def subs(self):
        try:
            Label(self.root, text='Подписчики:', bg='#202020', fg='#CCCCCC').place(x=0, y=65, height=20)
            Label(self.root, text='Подписки:', bg='#202020', fg='#CCCCCC').place(x=150, y=65, height=20)
            self.count_similar = Label(self.root, text='Взаимные:', bg='#202020', fg='#CCCCCC')
            self.count_similar.place(x=300, y=65, height=20)
            self.status['text'] = 'Загрузка. Подождите'
            self.root.geometry('450x390')

            self.subscribers_text.place(x=0, y=85, width=149, height=300)
            self.subscribed_text.place(x=150, y=85, width=149, height=300)
            self.similar_text.place(x=300, y=85, width=149, height=300)
            self.root.update()
            self.username = self.username_entry.get()
            self.my_login = self.my_login_entry.get()
            self.my_password = self.my_password_entry.get()
            self.L.login(self.my_login, self.my_password)
            profile = Profile.from_username(self.L.context, self.username)

            for i in profile.get_followers():
                self.list1.append(i.username)
                self.subscribers_text.insert(-1.0, f'@{str(i.username)}\n')

            for i in profile.get_followees():
                self.list2.append(i.username)
                self.subscribed_text.insert(-1.0, f'@{str(i.username)}\n')

            for i in range(len(self.list1)-1):
                if self.list1[i] in self.list2:
                    self.list3.append(self.list1[i])
                    self.similar_text.insert(-1.0, f'@{str(self.list1[i])}\n')

            self.count_similar['text'] = 'Взаимные: ' + str(len(self.list3))
            self.status['text'] = 'Готово!'
        except Exception as e:
            self.status['text'] = e

    def stories(self):
        try:
            self.status['text'] = 'Загрузка. Подождите'
            self.root.update()
            self.username = self.username_entry.get()
            self.my_login = self.my_login_entry.get()
            self.my_password = self.my_password_entry.get()
            self.L.login(self.my_login, self.my_password)
            profile = Profile.from_username(self.L.context, self.username)
            print(profile.userid)
            self.L.download_stories(userids=[profile.userid])
            self.status['text'] = 'Готово!'
        except Exception as e:
            self.status['text'] = e

    def find_similar(self):
        try:
            self.status['text'] = 'Загрузка. Подождите'
            self.root.geometry('450x390')
            self.subscribed_text.insert(1.0, '')
            self.subscribed_text.place(x=150, y=85, width=149, height=300)
            self.root.update()
            self.first_username = self.username_entry.get()
            self.second_username = self.second_username_entry.get()
            self.my_login = self.my_login_entry.get()
            self.my_password = self.my_password_entry.get()

            self.L.login(self.my_login, self.my_password)
            profile1 = Profile.from_username(self.L.context, self.first_username)
            profile2 = Profile.from_username(self.L.context, self.second_username)

            for i in profile1.get_followees():
                self.list1.append(i.username)
            for i in profile2.get_followees():
                self.list2.append(i.username)

            for i in range(len(self.list1)):
                if self.list1[i] in self.list2:
                    self.list3.append(self.list1[i])
                    self.subscribed_text.insert(-1.0, f'@{str(self.list1[i])}\n')

            self.status['text'] = 'Готово!'
        except Exception as e:
            self.status['text'] = e


_ = Parser()
