from customtkinter import *
from Data.SystemData.guiConfig import *

from Data.ExtraData.dataProcess import testaments,books

from GUI.side_page import *




class App(CTk):

    def __init__(self,title:str,size:tuple[int],font,resizable:bool=False):
        super().__init__()

        set_default_color_theme("C:\\Users\\TARIK ATASOY\\projects\\helloworld\\Projects\\Terminal\\Data\\customTheme.json")

        self.title(title)
        
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(resizable,resizable)

        self.font = font

        mainButtonFrame = ButtonFrame(self,self.create_books_page,self.create_testaments_page,self.quit,self.font)
        mainButtonFrame.place(relwidth=0.4,relheight=0.95,relx=0)

        statusBar = StatusBar(self)
        statusBar.place(relwidth=1,relheight=0.05,rely=0.95)

        self.mainloop()

    def create_testaments_page(self):

        self.pageTestament = PageWindow(self,f"{self.title()} - Testaments",(640,480),testaments,self.font,True)

    def create_books_page(self):

        self.pageBook = PageWindow(self,f"{self.title()} - Books",(640,480),books,self.font,True)


    def quit(self):
        self.destroy()


class ButtonFrame(CTkFrame):
    
    def __init__(self,parent:CTk,bookEvent:callable,testamentEvent:callable,quitEvent:callable,font,size:tuple=(250,50)): 
        super().__init__(parent)

        self.quitEvent = quitEvent
        self.testamentEvent = testamentEvent
        self.bookEvent = bookEvent
        
        self.w = size[0]
        self.h = size[1]

        self.font = font


        self.configure(fg_color="#2e2e2e")

        self.create_widgets()
        self.create_layout()
        self.place_widgets()



    def create_widgets(self):

        self.miniFrame = CTkFrame(self,fg_color="transparent")

        self.enemiesButton = CTkButton(self.miniFrame,text="Enemies",width=self.w,height=self.h,fg_color=colors["darker_grey"],font=self.font)
        self.booksButton = CTkButton(self.miniFrame,text="Books",command=self.bookEvent,width=self.w,height=self.h,fg_color=colors["darker_grey"],font=self.font)
        self.testamentsButton = CTkButton(self.miniFrame,text="Testaments",command=self.testamentEvent,width=self.w,height=self.h,fg_color=colors["darker_grey"],font=self.font)
        self.quitButton = CTkButton(self.miniFrame,text="Quit",command=self.quitEvent,width=self.w,height=self.h,fg_color=colors["darker_grey"],font=self.font)


    def create_layout(self):

        self.rowconfigure([*range(3)],weight=1)
        self.columnconfigure([*range(3)],weight=1)

    def place_widgets(self):

        self.miniFrame.grid(row=1,column=1)
        self.miniFrame.grid_propagate(False)

        self.enemiesButton.pack(pady=2)
        self.booksButton.pack(pady=2)
        self.testamentsButton.pack(pady=2)
        self.quitButton.pack(pady=2)


class StatusBar(CTkFrame):
    
    def __init__(self,parent:CTk):
        super().__init__(parent)

        self.create_widgets()
        self.place_widgets()



    def create_widgets(self):

        self.statusFrame = CTkFrame(self, fg_color=colors["titlebar_border"],corner_radius=0, height=1)
        self.statusLabel = CTkLabel(self.statusFrame,text="SYSTEM READY")

    def place_widgets(self):
        
        self.statusLabel.pack()


        


