from tkinter import *
from tkinter import Image, PhotoImage


# def raise_frame(frame):
#     frame.tkraise()


class prject:
    def __init__(self):
        root = Tk()
        root.title('Student Attendance System')

        #  screen format
        #  take the resolution of the computer screen

        # Home = Frame(root)
        # PageOne = Frame(root)

        # Home.grid(row=0, column=0)
        # PageOne.grid(row=0, column=0)

        maxWidth = str(root.winfo_screenwidth())  # take the max width
        maxHeight = str(root.winfo_screenheight())  # take the max height

        minWidth = int(root.winfo_screenwidth() / 2)  # take the min width
        minHeight = int(root.winfo_screenheight() / 2)  # take the min height

        psInfo = maxWidth + 'x' + maxHeight

        root.geometry(psInfo)
        root.maxsize((root.winfo_screenwidth()), (root.winfo_screenheight()))  # prepare the max size of the screen
        root.minsize(minWidth, minHeight)  # prepare the min size of the screen

        # background image for the root
        root.config(bg='#ffffff')
        bg_root_image = PhotoImage(file='./image/BG1.png')
        bg_label_image = Label(root, image=bg_root_image)
        bg_label_image.place(relwidth=1, relheight=1)

        # create frame in the root screen
        frame_Container = Frame(root, bg='#f3f3f3', relief=SUNKEN)
        frame_Container.place(relx=0.04, rely=0.25, relwidth=0.2, relheight=0.45)

        # label in the frame
        label_title = Label(frame_Container, text='Student Attendance System', bg='white', fg='#54a5ac',
                            font=('impact', 15), padx=10, pady=17)
        label_title.place(relx=0, rely=0.01, relwidth=1)

        # buttons in the frame container
        button_StartAttend = Button(frame_Container, text='Start Attendance Students\n in Exam',
                                    font=('arial bold', 12),
                                    pady=20, activebackground='#54a5ac', activeforeground='white')
        button_StartAttend.place(rely=0.22, relwidth=1)

        button_Display_StdInfo = Button(frame_Container, text='Display Student Schedule', font=('arial bold', 12),
                                        pady=20,
                                        activebackground='#54a5ac', activeforeground='white')
        button_Display_StdInfo.place(rely=0.5, relwidth=1)

        button_Login_Admin = Button(frame_Container, text='Login Admin', font=('times new roman bold', 15), pady=20,
                                    bg='#54a5ac', fg='white', command=root.quit)
        button_Login_Admin.place(rely=0.75, relwidth=1)

        root.mainloop()


app = prject()
