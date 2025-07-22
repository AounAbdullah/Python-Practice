from tkinter import *
from tkinter import messagebox
import json


# --------------------------------------Search-------------------------------------------------------
def searching():
    name = E_web.get()
    try:
        with open("data.json", 'r') as file:
            # Reading old data
            data = json.load(file)


    except:
        messagebox.showinfo(message="No file found")

    else:

        for names, keys in data.items():
            if names == name:
                webs = keys['email']
                passw = keys['password']
                messagebox.showinfo(title=f"Info on {name}", message=f"Email: {webs}\nPassword: {passw}\n")
            else:
                messagebox.showinfo(message="No email and password associated with this site")


# --------------------------------------Generate Password---------------------------------------------
import random
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    password_sym = [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]

    password_numbers = [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]


    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    E_pass.insert(0, password)
# -------------------------------------- SAVE PASSWORD -----------------------------------------------
def add():
    email = E_email.get()
    website = E_web.get()
    password = E_pass.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered : \n{email} '
                                                      f'\nPassword: {password} \nIs ok to save?')

        if is_ok:
            try:
                with open("data.json", 'r') as file:
                    # Reading old data
                    data = json.load(file)

            except:

                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)

            E_email.delete(0, 'end')
            E_pass.delete(0, 'end')
            E_web.delete(0, 'end')


window = Tk()
window.config(padx=50, pady=50, bg='#f7f7f7', highlightthickness=0)
window.title('Password Generator')



# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0, bd=0, bg=window['bg'])
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=0, row=0, columnspan=3, pady=(0, 20))

# Fonts
default_font = ("Segoe UI", 10)
heading_font = ("Segoe UI", 16, "bold")

# Labels
Label(text="Website:", bg='#f7f7f7', font=default_font).grid(column=0, row=1 )
Label(text="Email/Username:", bg='#f7f7f7', font=default_font).grid(column=0, row=2)
Label(text="Password:", bg='#f7f7f7', font=default_font).grid(column=0, row=3)

# Entry fields (all in column 1)
E_web = Entry(width=26, bg='white')
E_web.grid(column=1, row=1, sticky='W', pady=2)
E_web.focus() # For starting the cursor in this entry

E_email = Entry(width=47, bg='white')
E_email.grid(column=1, row=2, columnspan=2, sticky='W', pady=2)
E_email.insert(END, 'aoun84521@gmail.com')

E_pass = Entry(width=26, bg='white')
E_pass.grid(column=1, row=3, sticky='W', pady=2, ipady=1)
E_pass.get()

# Generate password button (next to password field)
Gen_pass = Button(text="Generate Pass", bg='#0077b6', fg='white',
                  activebackground='#023e8a', font=default_font, width=14, command=generate_pass)
Gen_pass.grid(column=2, row=3, sticky='W', padx=18)

Search = Button(text="Search", bg='#0077b6', fg='white',
                  activebackground='#023e8a', font=default_font, width=14, command=searching)
Search.grid(column=2, row=1, sticky='W', padx=18)


# Add button (directly below password field)
add_button = Button(text='Add', width=20, bg='#38b000', fg='white',
                    activebackground='#2d6a4f', relief='flat', font=default_font, command=add)
add_button.grid(column=1, row=4, columnspan=2, pady=10, sticky='W')

window.mainloop()
