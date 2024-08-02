import customtkinter
from tkinter import *
from PIL import Image, ImageTk

import cards
from cards import *

deck = get_deck()
shuffle_deck(deck)

app = customtkinter.CTk()
app.geometry('1500x800')
app.title('My Fortune')
app.resizable(width=False, height=True)

my_font = customtkinter.CTkFont(family="Blackadder ITC", size=30, weight='bold')
text_font = customtkinter.CTkFont(family="Blackadder ITC", size=22, weight='bold')
my_img = customtkinter.CTkImage(Image.open('images/Black_00.png'), size=(400, 300))

def shuffle():
    global my_img
    my_img = customtkinter.CTkImage(Image.open('images/Black_00.png'), size=(400, 300))
    frame2label.configure(image=my_img)
    frame3label.configure(image=my_img)
    frame4label.configure(image=my_img)

    frame2_text.configure(text_color='black')
    frame3_text.configure(text_color='black')
    frame4_text.configure(text_color='black')
    shuffle_deck(deck)

def dealPast():
    my_card = get_card(deck)
    cardname = my_card[0].get('name')
    carddesc = my_card[0].get('desc')
    cardadd = my_card[0].get('image')
    string1 = f'The {cardname}\n Symbolizes:\n {carddesc}'
    frame2_text.configure(text_color='darkgoldenrod3', text=string1)
    past_img = customtkinter.CTkImage(Image.open(cardadd), size=(400, 300))
    frame2label.configure(image=past_img)


def dealPresent():
    my_card = get_card(deck)
    cardname = my_card[0].get('name')
    carddesc = my_card[0].get('desc')
    cardadd = my_card[0].get('image')
    string1 = f'The {cardname}\n Symbolizes:\n {carddesc}'
    frame3_text.configure(text_color='darkgoldenrod3', text=string1)
    pres_img = customtkinter.CTkImage(Image.open(cardadd), size=(400, 300))
    frame3label.configure(image=pres_img)

def dealFuture():
    my_card = get_card(deck)
    cardname = my_card[0].get('name')
    carddesc = my_card[0].get('desc')
    cardadd = my_card[0].get('image')
    string1 = f'The {cardname}\n Symbolizes:\n {carddesc}'
    frame4_text.configure(text_color='darkGoldenrod3', text=string1)
    fut_img = customtkinter.CTkImage(Image.open(cardadd), size=(400, 300))
    frame4label.configure(image=fut_img)


frame1 = customtkinter.CTkFrame(master=app, fg_color='black')
frame2 = customtkinter.CTkFrame(master=frame1, fg_color='black')
frame2label = customtkinter.CTkLabel(master=frame2, text="", image=my_img)
frame2_text = customtkinter.CTkLabel(master=frame2, text="Past", font=text_font, text_color='darkGoldenrod3', wraplength=300)
frame2label.pack(pady=10)
frame2_text.pack(pady=10)
frame3 = customtkinter.CTkFrame(master=frame1, fg_color='black')
frame3label = customtkinter.CTkLabel(master=frame3, text="", image=my_img)
frame3_text = customtkinter.CTkLabel(master=frame3, text="Present", font=text_font, text_color='darkGoldenrod3', wraplength=300)
frame3label.pack(pady=10)
frame3_text.pack(pady=10)
frame4 = customtkinter.CTkFrame(master=frame1, fg_color='black')
frame4label = customtkinter.CTkLabel(master=frame4, text="", image=my_img)
frame4_text = customtkinter.CTkLabel(master=frame4, text='Future', font=text_font, text_color='darkGoldenrod3', wraplength=300)
frame4label.pack(pady=10)
frame4_text.pack(pady=10)
frame1.pack(side='top', fill='both', expand=True, padx=10)
frame2.grid(row=0, column=0, sticky="", padx=10, pady=10)
frame3.grid(row=0, column=1, sticky="", padx=10, pady=10)
frame4.grid(row=0, column=2, sticky="", padx=10, pady=10)


button1 = customtkinter.CTkButton(master=frame1, text="Shuffle Deck", fg_color='darkGoldenrod3', font=my_font, command=shuffle)
button2 = customtkinter.CTkButton(master=frame1, text="Show Past", fg_color='darkGoldenrod3', font=my_font, command=dealPast)
button3 = customtkinter.CTkButton(master=frame1, text="Show Present", fg_color='darkGoldenrod3', font=my_font, command=dealPresent)
button4 = customtkinter.CTkButton(master=frame1, text="Show future", fg_color='darkGoldenrod3', font=my_font, command=dealFuture)
button1.grid(column=1, row=3, pady=10)
button2.grid(column=0, row=2, pady=10)
button3.grid(column=1, row=2, pady=10)
button4.grid(column=2, row=2, pady=10)

app.mainloop()
