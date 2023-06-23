from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def random_password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    password_Label.delete(0,END)
    print(f"Your password is: {password}")
    password_Label.insert(0, password)
    pyperclip.copy(password)

# -------------------save entryy---------------------
entry_website = ""
email_Label = ""
password_Label = ""

def enter_To_text_File():
    if len(entry_website.get()) == 0 or len(password_Label.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please have no field empty")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(), message=f"There are the details entered: \nEmail: {email_Label.get()}\nPassword: {password_Label.get()}\nis it ok to save?")


        if is_ok:
            with open('input.txt', 'a') as f:
                f.write(f"{entry_website.get()} | {email_Label.get()} | {password_Label.get()} \n")
            entry_website.delete(0, END)
            password_Label.delete(0, END)





window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width = 200, height = 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column = 1, row = 0)

website_Label = Label(text="Website")
website_Label.grid(column = 0, row = 1)

email_Label = Label(text="Email/Username:")
email_Label.grid(column = 0, row = 2)

password_Label = Label(text="password")
password_Label.grid(column = 0, row = 3)

entry_website = Entry(width=35)
entry_website.grid(column = 1, row = 1, columnspan=2)
entry_website.focus()
email_Label = Entry(width=35)
email_Label.grid(column = 1, row = 2, columnspan=2)
email_Label.insert(0, "angela@gmail.com")
password_Label = Entry(width=21)
password_Label.grid(column = 1, row = 3)

generate_button = Button(text="Generate Password", width=15, command=random_password_generator)
generate_button.grid(column = 2, row = 3)


add_button = Button(text="Add", width=36, command=enter_To_text_File)
add_button.grid(column = 1, row = 4, columnspan=2)


window.mainloop()