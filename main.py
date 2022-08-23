from tkinter import *
from tkmacosx import Button
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

# Buttons

generate_btn = Button(window, text="Generate Password")
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
