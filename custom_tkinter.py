import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


def signup_page():
    #Signup details
    title_label = ctk.CTkLabel(signup_frames, text= 'Register')
    title_label.grid(row = 0, column = 0, pady = 20)

    firstname_label = ctk.CTkLabel(signup_frames, text = 'First Name')
    firstname_label.grid(row = 1, column = 0)

    firstname_entry = ctk.CTkEntry(signup_frames, width = 200, placeholder_text ='Enter your First Name')
    firstname_entry.grid(row=2, column = 0, padx = 50)
    
    lastname_label = ctk.CTkLabel(signup_frames, text = 'Last Name')
    lastname_label.grid(row = 3, column = 0)

    lastname_entry = ctk.CTkEntry(signup_frames, width = 200)
    lastname_entry.grid(row=4, column = 0, padx = 50)
    
    email_label = ctk.CTkLabel(signup_frames, text = 'Email')
    email_label.grid(row = 5, column = 0)

    email_entry = ctk.CTkEntry(signup_frames, width = 200)
    email_entry.grid(row=6, column = 0, padx = 50)
    
    phonenumber_label = ctk.CTkLabel(signup_frames, text = 'Phone Number')
    phonenumber_label.grid(row = 7, column = 0)

    phonenumber_entry = ctk.CTkEntry(signup_frames, width = 200)
    phonenumber_entry.grid(row=8, column = 0, padx = 50)
    
    password_label = ctk.CTkLabel(signup_frames, text = 'Password')
    password_label.grid(row = 9, column = 0)

    password_entry = ctk.CTkEntry(signup_frames, width = 200, show = '*')
    password_entry.grid(row=10, column = 0, padx = 50)

    confirm_password_label = ctk.CTkLabel(signup_frames, text = 'Confirm password')
    confirm_password_label.grid(row = 11, column = 0)

    confirm_password_entry= ctk.CTkEntry(signup_frames, width = 200, show = '*')
    confirm_password_entry.grid(row=12, column = 0, padx = 50)

    register_button = ctk.CTkButton(signup_frames, text ='Register')
    register_button.grid(row = 13, column = 0, pady = (10, 15))
      
    
if __name__ == '__main__':
    window = ctk.CTk()
    window.geometry('700x500')#how to give your window its size
    window.title('Abella Login Page')#how to add title on your title page
    window.iconbitmap('logo.ico')#how to add image to you icon bar/button

    #Section Frames
    button_frames = ctk. CTkFrame(window)
    button_frames.grid(row = 0, column = 0, padx = (30, 100))

    #login_frames = ctk. CTkFrame(window)
    #login_frames.grid(row = 0, column = 1, pady = 50)
    
    signup_frames = ctk. CTkFrame(window)
    signup_frames.grid(row = 0, column = 1, pady = 50)
    
    #Login and Signup section
    login_button = ctk.CTkButton(button_frames, text ='Login')
    login_button.grid(row = 0, column = 0, pady = (15, 30), padx = 20)

    signup_button = ctk.CTkButton(button_frames, text ='Sign up', command=signup_page)
    signup_button.grid(row = 1, column = 0, pady = (0, 15))
    



    window.mainloop()
