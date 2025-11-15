from customtkinter import *

class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()

        self.name = ""
        self.host = ""
        self.port = ""

        self.name_entry = CTkEntry(self, placeholder_text="Введіть ім'я: ")
        self.name_entry.pack(padx=20, anchor='w', fill="x")

        self.host_entry = CTkEntry(self, placeholder_text="Введіть хост: ")
        self.host_entry.pack(padx=20, pady=15, anchor='w', fill="x")

        self.port_entry = CTkEntry(self, placeholder_text="Введіть порт сервера: ")
        self.port_entry.pack(padx=20, anchor='w', fill="x")

        self.btn = CTkButton(self, command=self.open_game, height=50)
        self.btn.pack(padx=20, pady=15, fill="x")

    def open_game(self):
        self.name = self.name_entry.get()
        self.port = int(self.port_entry.get())
        self.host = self.host_entry.get()
        self.destroy()
