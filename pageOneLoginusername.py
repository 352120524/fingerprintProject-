from tkinter import *
from tkinter import Image, PhotoImage


class Project:
    def __init__(self):
        PageOneSecTwo = Tk()
        PageOneSecTwo.title('Start Attendance Students Page')

        maxWidth = str(PageOneSecTwo.winfo_screenwidth())  # take the max width
        maxHeight = str(PageOneSecTwo.winfo_screenheight())  # take the max height

        minWidth = int(PageOneSecTwo.winfo_screenwidth() / 2)  # take the min width
        minHeight = int(PageOneSecTwo.winfo_screenheight() / 2)  # take the min height

        psInfo = maxWidth + 'x' + maxHeight

        PageOneSecTwo.geometry(psInfo)
        PageOneSecTwo.maxsize((PageOneSecTwo.winfo_screenwidth()),
                              (PageOneSecTwo.winfo_screenheight()))  # prepare the max size of the screen
        PageOneSecTwo.minsize(minWidth, minHeight)  # prepare the min size of the screen

        # background image for the root
        PageOneSecTwo.config(bg='#ffffff')
        # bg_root_image = PhotoImage(file='./image/BG2.png')
        # bg_label_image = Label(PageOne, image=bg_root_image)
        # bg_label_image.place(relwidth=1, relheight=1)

        # create frame in the root screen
        frame_Container = Frame(PageOneSecTwo, bg='#024f77', relief=SUNKEN)
        frame_Container.place(relx=0, rely=0, relwidth=1, relheight=0.06)

        frame_lower = Frame(PageOneSecTwo, bg='#024f77', relief=SUNKEN)
        frame_lower.place(relx=0, rely=0.94, relwidth=1, relheight=0.06)

        button_back = Button(PageOneSecTwo, text='Back', bg='white', fg='#54a5ac', font=('Arial bold', 9),
                             activebackground='#54a5ac', activeforeground='white')
        button_back.place(relx=0.01, rely=0.013, relwidth=0.065, relheight=0.035)

        label_text = Label(PageOneSecTwo, text='Attendance Students in Exam', bg='#e2e5e5', font=('Arial bold', 12))
        label_text.place(rely=0.09, relwidth=1, relheight=0.045)

        label_Att = Label(PageOneSecTwo, text='* To Start Attendance Enter Username and Password Admin', bg='white',
                          font=('Arial', 14))
        label_Att.place(relx=0.5, rely=0.23, anchor='n')

        frame_scan_fingerprint = Frame(PageOneSecTwo, bd=4, relief=SUNKEN, bg='white')
        frame_scan_fingerprint.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.34)

        button_scan_finger = Button(frame_scan_fingerprint, text='Login', bg='#277a81', fg='white',
                                    font=('Arial bold', 12))
        button_scan_finger.place(relx=0.5, rely=0.85, relwidth=0.8, relheight=0.12, anchor='n')

        labe_username = Label(frame_scan_fingerprint, text='User Name', bg='white', font=('arial bold', 10))
        labe_username.place(relx=0.5, rely=0.35, anchor='n')

        entry_username = Entry(frame_scan_fingerprint, bd=2, relief=SUNKEN, font=('arial bold', 10), fg='#262626')
        entry_username.place(relx=0.5, rely=0.45, relwidth=0.8, relheight=0.12, anchor='n')

        labe_pass = Label(frame_scan_fingerprint, text='Password', bg='white', font=('arial bold', 12))
        labe_pass.place(relx=0.5, rely=0.58, anchor='n')

        entry_pass = Entry(frame_scan_fingerprint, bd=2, relief=SUNKEN, font=('arial bold', 12), fg='#262626', show='*')
        entry_pass.place(relx=0.5, rely=0.68, relwidth=0.8, relheight=0.12, anchor='n')

        PageOneSecTwo.mainloop()


app = Project()
