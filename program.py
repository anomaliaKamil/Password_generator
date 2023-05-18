from tkinter import *
import tkinter as tk
import random
import secrets
import string


root = Tk()
root.geometry("360x360")
root.resizable(False, False)
root.title("Generator")

def generate(): #funkcja generująca hasło

    password = [] 
    password_len = var_bar.get() #przypisanie wartości z paska 
    characters = []
    if var_ABC.get() == 1: 
        characters.extend(list(string.ascii_uppercase))
    if var_abc.get() == 1:
        characters.extend(list(string.ascii_lowercase))
    if var_123.get() == 1:
        characters.extend(list(string.digits))
    if var_punct.get() == 1:
        characters.extend(list(string.punctuation))
    else: passwordInput.delete(0,tk.END)
#Losowanie znaków
    while len(password) < password_len:
        character = random.choice(characters)
        if character is not password:
            password.append(character)
#Przypisywanie wylosowanych znaków do listy password
    random.shuffle(password) #Przetasowanie jeszcze hasła
    final_password = "".join(password) #Zmiana listy na stringa
    #print(final_password)
    passwordInput.delete(0,tk.END) #usuwanie zawartości
    passwordInput.insert(0,final_password) #dodanie nowej zawartości
    
   

    
    

title = Label(root, text = "Generator haseł")
title.pack()

frame = LabelFrame(root, padx = 30)
frame.pack(padx = 10,pady = 1)


passwordInput = Entry(frame, width= 80, bd = 4)
passwordInput.pack(pady = 10)

tittle_checkbuttons = Label(frame, text = "Użyte znaki:").pack()
frame_choice = LabelFrame(frame)

frame_choice.pack(padx = 5, pady = 10)

var_ABC = IntVar()
var_abc= IntVar()
var_123 = IntVar()
var_punct = IntVar()
var_bar= IntVar()


c1 = Checkbutton(frame_choice, text = "ABC", variable = var_ABC).grid(row = 1, column = 1)
c2 = Checkbutton(frame_choice, text = "abc", variable = var_abc).grid(row = 1, column = 2)
c3 = Checkbutton(frame_choice, text = "123", variable = var_123).grid(row = 1, column = 3)
c4 = Checkbutton(frame_choice, text = "!@#", variable = var_punct).grid(row = 1, column = 4)

tittle_bar = Label(frame, text = "Długość hasła:").pack()
bar = Scale(frame, from_= 5, to = 50, orient = HORIZONTAL, variable = var_bar).pack()

generateButton = Button(frame, text = "Generuj hasło",command = generate, padx = 10,pady = 15)
generateButton.pack(pady = 20)

root.mainloop()