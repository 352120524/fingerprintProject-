from tkinter import *
from tkinter import Image, PhotoImage


class Project:
    def __init__(self):
        PageOne = Tk()
        PageOne.title('Start Attendance Students Page')

        maxWidth = str(PageOne.winfo_screenwidth())  # take the max width
        maxHeight = str(PageOne.winfo_screenheight())  # take the max height

        minWidth = int(PageOne.winfo_screenwidth() / 2)  # take the min width
        minHeight = int(PageOne.winfo_screenheight() / 2)  # take the min height

        psInfo = maxWidth + 'x' + maxHeight

        PageOne.geometry(psInfo)
        PageOne.maxsize((PageOne.winfo_screenwidth()),
                        (PageOne.winfo_screenheight()))  # prepare the max size of the screen
        PageOne.minsize(minWidth, minHeight)  # prepare the min size of the screen

        # background image for the root
        PageOne.config(bg='#ffffff')
        # bg_root_image = PhotoImage(file='./image/BG2.png')
        # bg_label_image = Label(PageOne, image=bg_root_image)
        # bg_label_image.place(relwidth=1, relheight=1)

        # create frame in the root screen
        frame_Container = Frame(PageOne, bg='#024f77', relief=SUNKEN)
        frame_Container.place(relx=0, rely=0, relwidth=1, relheight=0.06)

        frame_lower = Frame(PageOne, bg='#024f77', relief=SUNKEN)
        frame_lower.place(relx=0, rely=0.94, relwidth=1, relheight=0.06)

        button_back = Button(PageOne, text='Back', bg='white', fg='#54a5ac', font=('Arial bold', 9),
                             activebackground='#54a5ac', activeforeground='white')
        button_back.place(relx=0.01, rely=0.013, relwidth=0.065, relheight=0.035)

        label_text = Label(PageOne, text='Attendance Students in Exam', bg='#e2e5e5', font=('Arial bold', 12))
        label_text.place(rely=0.09, relwidth=1, relheight=0.045)

        label_Att = Label(PageOne, text='* To Start Attendance Enter Fingerprint Admin', bg='white',
                          font=('Arial', 14))
        label_Att.place(relx=0.5, rely=0.23, anchor='n')

        frame_scan_fingerprint = Frame(PageOne, bd=4, relief=SUNKEN, bg='white')
        frame_scan_fingerprint.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.34)

        entry_scan_finger = Entry(frame_scan_fingerprint, bg='#cfd4d4')
        entry_scan_finger.place(relx=0.5, rely=0.1, relwidth=0.45, relheight=0.5, anchor='n')

        button_scan_finger = Button(frame_scan_fingerprint, text='Scan Fingerprint', bg='#54a5ac', fg='white',
                                    font=('Arial bold', 12))
        button_scan_finger.place(relx=0.5, rely=0.75, relwidth=0.65, relheight=0.15, anchor='n')

        button_login_username = Button(PageOne, text='or Login by Username', bg='#e5e5e5', fg='#262626',
                                       font=('Arial bold', 10))
        button_login_username.place(relx=0.5, rely=0.66, relwidth=0.15, relheight=0.035, anchor='n')

        PageOne.mainloop()

# bg='#277a81', fg='#262626',
app = Project()
