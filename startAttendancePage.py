from tkinter import *
from tkinter import Image, PhotoImage


class Project:
    def __init__(self):
        StartAttendPage = Tk()
        StartAttendPage.title('Start Attendance Students Page')

        maxWidth = str(StartAttendPage.winfo_screenwidth())  # take the max width
        maxHeight = str(StartAttendPage.winfo_screenheight())  # take the max height

        minWidth = int(StartAttendPage.winfo_screenwidth() / 2)  # take the min width
        minHeight = int(StartAttendPage.winfo_screenheight() / 2)  # take the min height

        psInfo = maxWidth + 'x' + maxHeight

        StartAttendPage.geometry(psInfo)
        StartAttendPage.maxsize((StartAttendPage.winfo_screenwidth()),
                                (StartAttendPage.winfo_screenheight()))  # prepare the max size of the screen
        StartAttendPage.minsize(minWidth, minHeight)  # prepare the min size of the screen

        # background image for the root
        StartAttendPage.config(bg='#ffffff')
        # bg_root_image = PhotoImage(file='./image/BG2.png')
        # bg_label_image = Label(PageOne, image=bg_root_image)
        # bg_label_image.place(relwidth=1, relheight=1)

        # create frame in the root screen
        frame_Container = Frame(StartAttendPage, bg='#024f77', relief=SUNKEN)
        frame_Container.place(relx=0, rely=0, relwidth=1, relheight=0.06)

        frame_lower = Frame(StartAttendPage, bg='#024f77', relief=SUNKEN)
        frame_lower.place(relx=0, rely=0.94, relwidth=1, relheight=0.06)

        frame_titel = Frame(StartAttendPage, bg='#e5e5e5')
        frame_titel.place(rely=0.08, relwidth=1, relheight=0.045)

        button_back = Button(StartAttendPage, text='Back', bg='white', fg='#54a5ac', font=('Arial bold', 9),
                             activebackground='#54a5ac', activeforeground='white')
        button_back.place(relx=0.01, rely=0.013, relwidth=0.065, relheight=0.035)

        lab_titel = Label(frame_titel, text='Attendance Student in Exam', font=('arial', 13), padx=55, bg='#e5e5e5')
        lab_titel.place(relx=0.5, rely=0.2, anchor='n')

        button_logout = Button(frame_titel, text='Log Out', bg='white')
        button_logout.place(relx=0.92, rely=0.15, relwidth=0.07, relheight=0.7)

        frame_fill_admin = Frame(StartAttendPage, bg='#e5e5e5')
        frame_fill_admin.place(relx=0.02, rely=0.18, relwidth=0.5, relheight=0.08)



        StartAttendPage.mainloop()


app = Project()
