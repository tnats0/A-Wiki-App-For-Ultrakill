from customtkinter import *
from config import *

from dataProcess import *


class App:

    def __init__(self):

        self.testamentNum = 1 # TODO: Relocate the variable

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
        self.leftFrame.rowconfigure([*range(6)],weight=1) 

        self.rightFrameOut.columnconfigure([*range(3)],weight=1)
        self.rightFrameOut.rowconfigure([*range(3)],weight=1)

        # * Frame Placement Inside Frames

        self.buttonFrame.grid(row=3,column=2)
        self.buttonFrame.grid_propagate(False)

        self.rightFrameIn.grid(row=1,column=1)
        self.rightFrameIn.grid_propagate(False)


        # * Buttons

        enemiesButton = CTkButton(self.buttonFrame,text="Enemies",command=self.action,width=200,height=45,fg_color=colors["darker_grey"])
        booksButton = CTkButton(self.buttonFrame,text="Books",command=self.create_book_page,width=200,height=45,fg_color=colors["darker_grey"])
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

        # * Testaments Page
        
        self.testamentsPage = CTkToplevel(self.mainWindow)

        self.testamentsPage.title("Testaments")

        self.testamentsPage.minsize(self.w,self.h)
        self.testamentsPage.maxsize(self.w,self.h)

        # * Layout

        self.testamentsPage.rowconfigure([*range(3)],weight=1)
        self.testamentsPage.columnconfigure([*range(3)],weight=1)

        # * Buttons

        self.preButton = CTkButton(self.testamentsPage,text=" <-- ",command=self.previous_page,fg_color=colors["darker_grey"],width=40,height=40)
        self.nextButton = CTkButton(self.testamentsPage,text=" --> ",command=self.next_page,fg_color=colors["darker_grey"],width=40,height=40)

        # * Button Placement

        self.preButton.grid(row=2,column=0,sticky=SW)        
        self.nextButton.grid(row=2,column=2,sticky=SE)        

        # * Label and Label Placement

        self.testamentLabel = CTkLabel(self.testamentsPage,text=testaments[f"{self.testamentNum}"])
        self.testamentLabel.grid(row=1,column=1)
        

    def create_book_page(self):

        self.bookPage = CTkToplevel(self.mainWindow)

        self.bookPage.title("Books")

        self.bookPage.minsize(self.w,self.h)
        self.bookPage.maxsize(self.w,self.h)


        self.bookPage.rowconfigure([*range(3)],weight=1)
        self.bookPage.columnconfigure([*range(3)],weight=1)


        self.bookLabel = CTkLabel(self.bookPage,text=bookData_1_4)
        self.bookLabel.grid(row=1,column=1)





    def next_page(self):

        self.testamentNum += 1

        if self.testamentNum > 5:

            self.testamentNum = 1

        self.testamentLabel.destroy()
        self.testamentLabel = CTkLabel(self.testamentsPage,text=testaments[f"{self.testamentNum}"])
        self.testamentLabel.grid(row=1,column=1)


    def previous_page(self):

        self.testamentNum -= 1

        if self.testamentNum < 1:

            self.testamentNum = 5

        self.testamentLabel.destroy()
        self.testamentLabel = CTkLabel(self.testamentsPage,text=testaments[f"{self.testamentNum}"])
        self.testamentLabel.grid(row=1,column=1)


    def quit(self):

        self.mainWindow.destroy()



App()