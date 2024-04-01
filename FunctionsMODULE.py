from customtkinter import *
from PIL import Image
from savingdata import _get_infor_from_database, _save_to_dataBase


# function to place the frames to be switchable
def switch_frames(frame1, frame2):
    if frame1.winfo_viewable():
        frame1.place_forget()
        frame2.place(x=405, y=0)
        frame2_widgets(frame2, frame1)
    else:
        frame2.place_forget()
        frame1.place(x=405, y=0)


# function to create the first frame
def create_frame1(app):
    frame = CTkFrame(
        app,
        width=390,
        height=585,
        border_width=30,
        border_color='#FFFFF7',
        corner_radius=8,
        fg_color='#FFFFF7',
    )
    return frame


# function to widgets for the first frame
def frame1_widgets(frame, frame2, mainframe):
    header = CTkLabel(
        master=frame,
        text='Welcome Back!',
        text_color='purple',
        font=('Comic Sans MS', 30, 'bold'),
    )
    header.place(x=25, y=24)
    footer = CTkLabel(
        master=frame,
        text='sign in to your account',
        text_color='#808080',
        font=('Comic Sans MS', 15, 'bold')
    )
    footer.place(x=26, y=69)
    # creating email label
    email_image = Image.open('postcard.png')
    image_email = CTkImage(
        email_image,
        size=(20, 20)
    )
    email = CTkLabel(
        master=frame,
        text='',
        image=image_email,
        width=5,
        height=5,
    )
    email.place(x=25, y=150)
    email_label = CTkLabel(
        master=frame,
        text='Email:',
        text_color='purple',
        font=('Comic Sans MS', 15, 'bold')
    )
    email_label.place(x=50, y=148)
    # placing an entr to receive input
    entry_email = CTkEntry(
        master=frame,
        width=300,
        height=35,
        corner_radius=5,
        fg_color='#F2F3F5',
        border_width=2,
        border_color='purple',
        text_color='purple',
        font=('Comic Sans MS', 14)
    )
    entry_email.place(x=25, y=178)
    # creating password section
    pas_image = Image.open('4585570.png')
    pass_image = CTkImage(
        pas_image,
        size=(20, 20)
    )
    password = CTkLabel(
        master=frame,
        text='',
        image=pass_image
    )
    password.place(x=25, y=240)
    password_label = CTkLabel(
        master=frame,
        text='Password:',
        text_color='purple',
        font=('Comic Sans MS', 15, 'bold')
    )
    password_label.place(x=50, y=244)
    entry_password = CTkEntry(
        master=frame,
        width=300,
        height=35,
        corner_radius=5,
        fg_color='#F2F3F5',
        border_width=2,
        border_color='purple',
        text_color='purple',
        font=('Comic Sans MS', 14),
        show="*"
    )
    entry_password.place(x=25, y=275)

    # function to get  the text typed password and username
    def Information():
        username = entry_email.get().strip()
        password__ = entry_password.get().strip()
        _get_infor_from_database(username, password__, frame, mainframe)

    Login = CTkButton(
        master=frame,
        text='Login',
        text_color='white',
        fg_color='purple',
        width=300,
        height=35,
        font=('Comic Sans MS', 15, 'bold'),
        command=Information
    )
    Login.place(x=25, y=350)

    # functionality to switch frames
    def switch():
        switch_frames(frame, frame2)
    google = CTkButton(
        master=frame,
        text='To sign up. Click here',
        text_color='white',
        fg_color='purple',
        width=300,
        height=35,
        font=('Comic Sans MS', 13, 'bold'),
        hover_color='#C0C0C0',
        command=switch
    )
    google.place(x=25, y=420)


# function to create the second frame
def create_frame2(app):
    frame = CTkFrame(
        app,
        width=390,
        height=585,
        border_width=30,
        border_color='#FFFFF7',
        corner_radius=8,
        fg_color='#FFFFF7',
    )
    return frame


# function to set widgets for the second frame
def frame2_widgets(frame2, frame1):
    welcome = CTkLabel(
        master=frame2,
        text='Welcome!',
        text_color='purple',
        font=('Comic Sans MS', 30, 'bold'),
    )
    welcome.place(x=25, y=24)
    footer2 = CTkLabel(
        master=frame2,
        text='sign up a new account',
        text_color='#808080',
        font=('Comic Sans MS', 15, 'bold')
    )
    footer2.place(x=26, y=69)
    # creating email label
    email_image2 = Image.open('postcard.png')
    image_email2 = CTkImage(
        email_image2,
        size=(20, 20)
    )
    email2 = CTkLabel(
        master=frame2,
        text='',
        image=image_email2,
        width=5,
        height=5,
    )
    email2.place(x=25, y=150)
    email_label2 = CTkLabel(
        master=frame2,
        text='Email:',
        text_color='purple',
        font=('Comic Sans MS', 15, 'bold')
    )
    email_label2.place(x=50, y=148)
    # placing an entr to receive input
    entry_email2 = CTkEntry(
        master=frame2,
        width=300,
        height=35,
        corner_radius=5,
        fg_color='#F2F3F5',
        border_width=2,
        border_color='purple',
        text_color='purple',
        font=('Comic Sans MS', 14)
    )
    entry_email2.place(x=25, y=178)
    # creating password section
    pas_image2 = Image.open('4585570.png')
    pass_image2 = CTkImage(
        pas_image2,
        size=(20, 20)
    )
    password2 = CTkLabel(
        master=frame2,
        text='',
        image=pass_image2
    )
    password2.place(x=25, y=240)
    password_label2 = CTkLabel(
        master=frame2,
        text='Password:',
        text_color='purple',
        font=('Comic Sans MS', 15, 'bold')
    )
    password_label2.place(x=50, y=244)
    entry_password2 = CTkEntry(
        master=frame2,
        width=300,
        height=35,
        corner_radius=5,
        fg_color='#F2F3F5',
        border_width=2,
        border_color='purple',
        text_color='purple',
        font=('Comic Sans MS', 14),
    )
    entry_password2.place(x=25, y=275)
    # creating the login button

    # function to get  the text typed password and username
    def save_information():
        username = entry_email2.get().strip()
        password__ = entry_password2.get().strip()
        _save_to_dataBase(username, password__)

    Login2 = CTkButton(
        master=frame2,
        text='Sign-up',
        text_color='white',
        fg_color='purple',
        width=300,
        height=35,
        font=('Comic Sans MS', 15, 'bold'),
        command=save_information
    )
    Login2.place(x=25, y=350)

    # functionality to switch frames
    def switch():
        switch_frames(frame1, frame2)
    google2 = CTkButton(
        master=frame2,
        text='Click here to go to login page',
        text_color='white',
        fg_color='purple',
        width=300,
        height=35,
        font=('Comic Sans MS', 13, 'bold'),
        hover_color='#C0C0C0',
        command=switch
    )
    google2.place(x=25, y=420)
