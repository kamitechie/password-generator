from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letters = [choice(letters) for _ in range(randint(8, 10))]
    rand_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    rand_num = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = rand_letters + rand_symbols + rand_num
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = str(web_input.get())
    email = str(email_input.get())
    password = str(password_input.get())
    new_data = {
        web: {
            "email": email,
            "password": password,
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title='Ups', message="Please, don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, 'end')
            password_input.delete(0, 'end')

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    web = str(web_input.get())
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Ups", message="No Data File Found")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Ups", message=f"No details for the {web} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Generator')
window.config(padx=20, pady=60)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

web_label = Label(text='Website:')
web_label.grid(row=1, column=0)

web_input = Entry(width=33)
web_input.focus()
web_input.grid(row=1, column=1)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

email_input = Entry(width=52)
#email_input.insert(0, 'default email adress')
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0, sticky='nsew')

password_input = Entry(width=33)
password_input.grid(row=3, column=1)

generate_button = Button(text='Generate Password', width=14, command=generate_password)
generate_button.grid(row=3, column=2, sticky='nsew')

add_button = Button(text='Add', width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(row=1, column=2)

window.mainloop()
