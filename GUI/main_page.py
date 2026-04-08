from customtkinter import *
from rich.text import *

from Data.SystemData.guiConfig import *
from Data.SystemData.system_info import sys_info_minimized

from Data.ExtraData.dataProcess import testaments,books

from GUI.side_page import *




class App(CTk):

    def __init__(self,title:str,size:tuple[int],font,resizable:bool=False):
        super().__init__()

        self.title(title)
        
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(resizable,resizable)

        self.font = font

        self.configure(fg_color=colors["window_bg"])

        topBar = TopBar(self)
        topBar.place(relwidth=1,relheight=0.1,rely=0)

        mainButtonFrame = ButtonFrame(self,self.create_books_page,self.create_testaments_page,self.quit,self.font)
        mainButtonFrame.place(relwidth=0.4,relheight=0.85,rely=0.1)

        logoFrame = LogoFrame(mainButtonFrame)
        logoFrame.grid(row=0,column=1)

        mainTipFrame = TipFrame(self)
        mainTipFrame.place(relwidth=0.6,relheight=0.85,relx=0.4,rely=0.1)

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
    
    def __init__(self,parent:App,bookEvent:callable,testamentEvent:callable,quitEvent:callable,font,size:tuple=(250,50)): 
        super().__init__(parent)

        self.parent = parent

        self.quitEvent = quitEvent
        self.testamentEvent = testamentEvent
        self.bookEvent = bookEvent
        
        self.w = size[0]
        self.h = size[1]

        self.font = font


        self.configure(fg_color="#2e2e2e",corner_radius=1)

        self.create_widgets()
        self.create_layout()
        self.place_widgets()



    def create_widgets(self):

        self.miniFrame = CTkFrame(self,fg_color="transparent")

        self.enemiesButton = CTkButton(self.miniFrame,text="Enemies",width=self.w,height=self.h,fg_color=colors["darker_grey"],font=self.parent.font)
        self.booksButton = CTkButton(self.miniFrame,text="Books",command=self.bookEvent,width=self.w,height=self.h,fg_color=colors["darker_grey"],font=self.parent.font)
        self.testamentsButton = CTkButton(self.miniFrame,text="Testaments",command=self.testamentEvent,width=self.w,height=self.h,fg_color=colors["darker_grey"],font=self.parent.font)
        self.quitButton = CTkButton(self.miniFrame,text="Quit",command=self.quitEvent,width=self.w,height=self.h,fg_color=colors["darker_grey"],font=self.parent.font)


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


class LogoFrame(CTkFrame): 

    def __init__(self,parent):
        super().__init__(parent)

        self.update_idletasks()

        self.create_widgets()
        self.place_widgets()



    def create_widgets(self):

        self.textRowFrame = CTkFrame(self,fg_color="transparent",bg_color="transparent")

        self.logoText = CTkLabel(self.textRowFrame,text = "Smile",font=CTkFont("Arial",40,"bold"))
        self.logoText2 = CTkLabel(self.textRowFrame,text = "OS 2.0",font=CTkFont("Arial",25,"bold"))

        self.rainbowBar = self.create_rainbow_gradient_bar(200,5)
  

    def place_widgets(self):

        self.textRowFrame.pack()

        self.logoText.pack(side=LEFT,anchor=S) 
        self.logoText2.pack(side=LEFT,anchor=S)
        self.rainbowBar.pack()

    def create_rainbow_gradient_bar(self,width:int=120,height:int=3):

        self.bar = CTkCanvas(self,width=width,height=height,highlightthickness=0)

        colors = ["#e74c3c","#e67e22","#f1c40f","#2ecc71","#3498db","#9b59b6"]

        subLineLenght = width / len(colors)

        for idx,color in enumerate(colors):

            self.bar.create_rectangle(idx*subLineLenght,0,(idx+1)*subLineLenght,height,fill=color,outline="")

        return self.bar


class TipFrame(CTkFrame):

    def __init__(self,parent:App):
        super().__init__(parent)

        self.configure(corner_radius=1)

        self.create_widgets()
        self.place_widgets()


    def create_widgets(self):

        self.inFrame = CTkFrame(self,fg_color=colors["tip_body"],corner_radius=1)
        self.inFrameTopBar = CTkFrame(self.inFrame,fg_color=colors["titlebar_top"])
        self.inFrameTitle = CTkLabel(self.inFrameTopBar,text=" Tip Of The Day ",font=CTkFont("Arial",16,"bold"))

    def place_widgets(self):

        self.inFrame.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05)
        self.inFrameTopBar.place(relwidth=1,relheight=0.1)
        self.inFrameTitle.pack(side=LEFT)



class TopBar(CTkFrame):

    def __init__(self,parent:App):
        super().__init__(parent)

        self.parent = parent

        self.configure(fg_color=colors["titlebar_top"],corner_radius=5, height=1)

        
        self.create_widgets()
        self.place_widgets()


    def create_widgets(self):

        self.iconLabel = CTkLabel(self,text="LOGO") 
        self.titleLabel = CTkLabel(self,text=" SmileOS 2.0 ",font=CTkFont("Arial",14,"bold"))


    def place_widgets(self):

        self.iconLabel.pack(side=LEFT,padx=10)
        self.titleLabel.pack(side=LEFT)

    
class StatusBar(CTkFrame):
    
    def __init__(self,parent:CTk):
        super().__init__(parent)

        self.configure(fg_color=colors["status_bar"],corner_radius=0, height=1)

        self.create_widgets()
        self.place_widgets()



    def create_widgets(self):

        self.dot = CTkFrame(self,width=6,height=6,corner_radius=3,fg_color=colors["status_dot"])
        self.text = CTkLabel(self,text="SYSTEM READY ",text_color=colors["status_text"],font=("Courier",10))

        self.stats = CTkLabel(self,text=sys_info_minimized,text_color=colors["status_text"],font=("Courier",10))

       
    def place_widgets(self):

        self.dot.pack(side=LEFT,padx=(12,6),pady=8)
        self.text.pack(side=LEFT)

        self.stats.pack(side=LEFT)
        


        


