from customtkinter import *
from config import *

class App(CTk):

    def __init__(self,title:str,size:tuple[int],resizable:bool=False):
        super().__init__()

        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(resizable,resizable)

        bFrame = ButtonFrame(self,self.quit)
        bFrame.place(relwidth=0.4,relheight=1,relx=0)


        self.mainloop()


    def quit(self):
        self.destroy()


class ButtonFrame(CTkFrame):
    
    def __init__(self,parent,quitEvent:callable): # * quitEvent must be a function
        super().__init__(parent)

        self.quitEvent = quitEvent

        self.configure(fg_color="#2e2e2e")

        self.create_widgets()
        self.create_layout()
        self.place_widgets()



    def create_widgets(self):

        self.miniFrame = CTkFrame(self,fg_color="transparent")

        self.enemiesButton = CTkButton(self.miniFrame,text="Enemies",width=200,height=45,fg_color=colors["darker_grey"])
        self.booksButton = CTkButton(self.miniFrame,text="Books",width=200,height=45,fg_color=colors["darker_grey"])
        self.testamentsButton = CTkButton(self.miniFrame,text="Testaments",width=200,height=45,fg_color=colors["darker_grey"])
        self.quitButton = CTkButton(self.miniFrame,text="Quit",command=self.quitEvent,width=200,height=45,fg_color=colors["darker_grey"])


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


    



App("SmileOS 2.0",(640,480),True)