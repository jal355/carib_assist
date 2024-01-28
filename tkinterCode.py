import tkinter as tk
from tkinter import *
import customtkinter
from Main import *
import sys


def button_click_action():
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit()
# -----------------------------------------------

app = customtkinter.CTk()
app.geometry("1280x720")

customtkinter.set_appearance_mode("dark")
welcome_banner = customtkinter.CTkLabel(app, text="Welcome, I'm Vivian!", anchor="w", font=("Airal", 25))
welcome_banner.place(relx=0.50, rely=0.35, anchor="center")

role_description = customtkinter.CTkLabel(app, text="Your Caribbean personal assistant.", anchor="w", font=("Airal", 20))
role_description.place(relx=0.50, rely=0.40, anchor="center")

button = customtkinter.CTkButton(app, text="Click to Start", command=button_click_action, corner_radius=350, fg_color="#483d8b", hover_color="#69359c", height=50, width=100)
button.place(relx=0.50, rely=0.50, anchor="center")

app.mainloop()
