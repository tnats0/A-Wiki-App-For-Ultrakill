from customtkinter import *
from config import *

from testamentData import *


class App:

    def __init__(self):
        
        self.mainWindow = CTk()

        # * Main Window

        self.w,self.h = 640,480

        self.mainWindow.title("SmileOS 2.0")

        self.mainWindow.maxsize(self.w,self.h)
        self.mainWindow.minsize(self.w,self.h)

        # * Frames

        self.leftFrame = CTkFrame(self.mainWindow,bg_color=colors["dark_grey"],fg_color=colors["dark_grey"],width=240,height=480)
        self.buttonFrame = CTkFrame(self.leftFrame,bg_color="transparent",fg_color="transparent")

        self.rightFrameOut = CTkFrame(self.mainWindow,bg_color=colors["dark_grey"],fg_color=colors["dark_grey"],width=400,height=480,border_color=colors["dark_grey"],border_width=30)
        self.rightFrameIn = CTkFrame(self.rightFrameOut,bg_color=colors["darkest_grey"],fg_color=colors["darkest_grey"],width=370,height=450)

        # * Frame Placement

        self.leftFrame.pack(side=LEFT,expand=True,fill=BOTH)
        self.leftFrame.pack_propagate(False)

        self.rightFrameOut.pack(side=LEFT,expand=True,fill=BOTH)
        self.rightFrameOut.pack_propagate(False)

        # * Layouts Inside Frames

        self.leftFrame.columnconfigure([*range(3)],weight=1)
        self.leftFrame.rowconfigure([*range(6)],weight=1) # !!

        self.rightFrameOut.columnconfigure([*range(3)],weight=1)
        self.rightFrameOut.rowconfigure([*range(3)],weight=1)

        # * Frame Placement Inside Frames

        self.buttonFrame.grid(row=3,column=2)
        self.buttonFrame.grid_propagate(False)

        self.rightFrameIn.grid(row=1,column=1)
        self.rightFrameIn.grid_propagate(False)


        # * Buttons

        enemiesButton = CTkButton(self.buttonFrame,text="Enemies",command=self.action,width=200,height=45,fg_color=colors["darker_grey"])
        booksButton = CTkButton(self.buttonFrame,text="Books",command=self.action,width=200,height=45,fg_color=colors["darker_grey"])
        testamentsButton = CTkButton(self.buttonFrame,text="Testaments",command=self.create_testaments_page,width=200,height=45,fg_color=colors["darker_grey"])
        quitButton = CTkButton(self.buttonFrame,text="Quit",command=self.quit,width=200,height=45,fg_color=colors["darker_grey"])

        # * Button Placement

        enemiesButton.pack(pady=2,expand=True,fill=BOTH)
        booksButton.pack(pady=2,expand=True,fill=BOTH)
        testamentsButton.pack(pady=2,expand=True,fill=BOTH)
        quitButton.pack(pady=2,expand=True,fill=BOTH)

        # * END

        self.mainWindow.mainloop()


    def action(self):
        print("Activated!")

    def create_testaments_page(self):
        
        self.testamentsPage = CTkToplevel(self.mainWindow)

        self.testamentsPage.title("Testaments")

        self.testamentsPage.minsize(self.w,self.h)
        self.testamentsPage.maxsize(self.w,self.h)

        self.testamentsPage.rowconfigure([*range(3)],weight=1)
        self.testamentsPage.columnconfigure([*range(3)],weight=1)


        self.label1 = CTkLabel(self.testamentsPage,text=testaments["1"])
        self.label1.grid(row=1,column=1)
        

    def quit(self):

        self.mainWindow.destroy()



App()