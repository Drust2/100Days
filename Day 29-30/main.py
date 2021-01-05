from tkinter import *
from tkinter import messagebox
import pandas
import random
import json

BACKGROUND = "#d9ecf2"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_input.delete(0, 'end')
    password_list = []
    nr_letters = 4
    nr_symbols = 4
    nr_numbers = 4
    
    for char in range(1, nr_letters + 1):
      password_list.append(random.choice(letters))
    
    for char in range(1, nr_symbols + 1):
      password_list += random.choice(symbols)
    
    for char in range(1, nr_numbers + 1):
      password_list += random.choice(numbers)
    
    random.shuffle(password_list)
   
    password = ""
    for char in password_list:
      password += char
    password_input.insert(0, password)
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if website != "" and email != "" and password != "":
        entry = {
            "Website": website,
            "Username": email,
            "Password": password,
        }
        try:
            with open("saved_passwords.json") as file:
                saved_passwords = json.load(file)
                
        except FileNotFoundError:
            entry = {
                "Website": [website],
                "Username": [email],
                "Password": [password],
                }
            new_password = pandas.DataFrame(entry)                  
            new_password.to_json("saved_passwords.json")
            password_input.delete(0, 'end')
            messagebox.showinfo(title="Password Manager", message="The information was saved succesfully.")
        else:
            saved_passwords = pandas.read_json("saved_passwords.json")
            check = 0
            for (index, row) in saved_passwords.iterrows():
                if row.Website == website and row.Username == email:
                    check = 1
                    
            if check == 0:
                saved_passwords = saved_passwords.append(entry, ignore_index = True)                
                saved_passwords.to_json("saved_passwords.json")
                # Cleaning the GUI
                password_input.delete(0, 'end')
                messagebox.showinfo(title="Password Manager", message="The information was saved succesfully.")
            else:
                messagebox.showwarning(title="Password Manager", message="There exists already a password for this combination of user and website.")
    else:
        messagebox.showerror(title="Password Manager", message="All fields must be filled to continue.")


# New Window for the existing data inserted in the search_user() function
def existing_data(username=""):    
    if username == "":
        messagebox.showwarning(title="Search username", message="Please input a username")
    else:
       #Listbox usage
       def listbox_used(event):
        # Gets current selection from listbox
        current_website = search_listbox.get(search_listbox.curselection())
        for (index, row) in saved_passwords.iterrows():
            if row.Username == username and row.Website == current_website:
                password = row.Password
                
        web_entry.config(state=NORMAL)   
        web_entry.delete(0, 'end')
        web_entry.insert(0, current_website)
        web_entry.config(state=DISABLED)
        pwd_entry.delete(0, 'end')
        pwd_entry.insert(0, password)
        
        # Check if there is an existing data file
       try:
            with open("saved_passwords.json") as file:
                saved_passwords = json.load(file)
       except FileNotFoundError:
            messagebox.showerror(title= "Search existing username", message="There is no data file in the program directory. You should first store some data.")
       else:
            saved_passwords = pandas.read_json("saved_passwords.json")
            search_window = Toplevel(window)
            search_window.title("Search existing passwords")
            search_window.config(bg=BACKGROUND, padx=20)
            
            #Frame for the labels
            frame = Frame(search_window, bg=BACKGROUND)
            frame.grid(row=0, column = 3, padx=20)
            
            # Label
            user_label = Label(frame, text="Username:", bg=BACKGROUND, font=("Arial", 10))
            user_label.grid(column = 0, row=0, sticky="W")
            web_label = Label(frame, text="Website:", bg=BACKGROUND, font=("Arial", 10))
            web_label.grid(column = 0, row=1, sticky="W")
            pwd_label = Label(frame, text="Password:", bg=BACKGROUND, font=("Arial", 10))
            pwd_label.grid(column = 0, row=2, sticky="W")
            
            username_entry = Entry(frame, width=30)
            username_entry.insert(0, username)
            username_entry.config(state=DISABLED)
            username_entry.grid(row=0, column=1, sticky="W", columnspan=2)
            
            web_entry = Entry(frame, width=30)
            web_entry.config(state=DISABLED)
            web_entry.grid(row=1, column=1, sticky="W", columnspan=2)
            
            pwd_entry = Entry(frame, width=30)
            pwd_entry.grid(row=2, column=1, sticky="W", columnspan=2)        
            
            
            # Loading the list of websites stored for the current username
            search_listbox = Listbox(search_window, height=5, width= 41)    
            existing_websites = []
            for (index, row) in saved_passwords.iterrows():
                if row.Username == username:
                    existing_websites.append(row.Website)
            
            for website in existing_websites: 
                search_listbox.insert(existing_websites.index(website), website)
                search_listbox.bind("<<ListboxSelect>>", listbox_used)
                search_listbox.grid(column=0, row=0, sticky="", pady=10)
        
            #Scrollbar
            search_scrollbar = Scrollbar(search_window, orient="vertical")
            search_scrollbar.config(command=search_listbox.yview)
            search_scrollbar.grid(column=1, row=0, sticky="")
            search_listbox.config(yscrollcommand=search_scrollbar.set)
            
    
def search_user():
    # To close the window and return the search
    def button_press():
        entry = user_input.get()
        existing_data(username=entry)
        new_user.destroy()
    
    new_user = Toplevel(window)
    new_user.title("Input existing username or email")
    new_user.config(bg=BACKGROUND, padx=20, pady= 5)
    
    # Label
    search_user = Label(new_user, text="Email/Username:", bg=BACKGROUND, width=15, font=("Arial", 10))
    search_user.grid(column=0, row=0, pady=10)
    
    # Input
    user_input = Entry(new_user, width=40)
    user_input.grid(column=1, row=0)
    user_input.focus()
    
    # Button
    input_button = Button(new_user, text="Search", width=20, command=button_press)
    input_button.grid(column=0, row=1, columnspan=2, pady=10)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=BACKGROUND, padx=20)
window.title("Password Manager")

canvas = Canvas(width=400, height=200, highlightthickness=0, bg=BACKGROUND)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(200, 94.5, image=bg_image)
canvas.grid(column=0, row=0, columnspan=2, sticky="N")

# Labels
website_label = Label(text="Website:", bg=BACKGROUND, width=15, font=("Arial", 10))
website_label.grid(row=1, column=0, pady=2)
email_label = Label(text="Email/Username:", bg=BACKGROUND, width=15, font=("Arial", 10))
email_label.grid(row=2, column=0, pady=2)
password_label = Label(text="Password:", bg=BACKGROUND, width=15, font=("Arial", 10))
password_label.grid(row=3, column=0, pady=2)

# Inputs
website_input = Entry(width=40, highlightthickness=1)
website_input.grid(row=1, column=1, columnspan=20)
website_input.focus()
email_input = Entry(width=40, highlightthickness=1)
email_input.insert(0, "Drust")
email_input.grid(row=2, column=1, columnspan=20)
password_input = Entry(width=20, highlightthickness=1)
password_input.grid(row=3, column=1, sticky="W", columnspan=20)

# Buttons
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=1, sticky="E", columnspan=40)
add_button = Button(text="Add", width=34, highlightthickness=1, command=save_password)
add_button.grid(row=4, column=1, pady=2, columnspan=40)
search_button = Button(text="Search existing data", width=30, command=search_user)
search_button.grid(row=5, column=0, pady=10, sticky="", columnspan=2)


window.mainloop()