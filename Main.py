from FunctionsMODULE import *

# creating app window
app = CTk()
app.geometry('800x600')
app.resizable(False, False)
app.title('')
# creating the main frame
main_frame = CTkFrame(
    app,
    fg_color='white',
    width=800,
    height=580,
)
main_frame.place(x=0, y=0)
# image file
image = Image.open('8fdc3b8300604ed2af0e86142dc47443.png')
# creating the image object
background_image = CTkImage(
    image,
    size=(800, 580)
)
# creating the label
image_label = CTkLabel(
    main_frame,
    text='',
    image=background_image
)
image_label.pack()

# creating the first frame
frame1 = create_frame1(main_frame)

# creating the second frame
frame2 = create_frame2(main_frame)


# Initially, place frame1
frame1.place(x=405, y=0)
# frame one header and footer
frame1_widgets(frame1, frame2, main_frame)

app.mainloop()
