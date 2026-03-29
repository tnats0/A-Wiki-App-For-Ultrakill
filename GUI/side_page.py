from customtkinter import *
from Data.SystemData.guiConfig import *

from Data.ExtraData.dataProcess import *


class PageWindow(CTkToplevel):

    def __init__(self,parent,title:str,size:tuple[int],pages:list,font,resizable:bool=False):
        super().__init__(parent)

        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(resizable,resizable)

        self.font = font

        self.pages = pages
        self.totalPage = len(pages)

        self.topFrame = PageTextFrame(self,self.pages[0],self.font)
        self.bottomFrame = PageButtonFrame(self,self.totalPage,self.change_page,self.font)

        self.topFrame.place(relwidth=1,relheight=0.8,rely=0)
        self.bottomFrame.place(relwidth=1,relheight=0.2,rely=0.8)

    def change_page(self,newPageNum:int):

        self.topFrame.update_text(self.pages[newPageNum])
        
        
class PageTextFrame(CTkFrame):

    def __init__(self,root,text,font):
        super().__init__(root)

        self.text = text

        self.textFrameFont = font


        self.create_widgets()


    def create_widgets(self):

        self.textLabel = CTkLabel(self,text=self.text,font=self.textFrameFont)
        self.textLabel.pack(expand=True,fill=BOTH)

    def update_text(self,newText:str):

        self.textLabel.configure(text=newText)
        

class PageButtonFrame(CTkFrame):
    def  __init__(self,parent:CTk,totalPageCount:int,ChangePageEvent:callable,font):
        super().__init__(parent)

        self.ChangePageEvent = ChangePageEvent
       
        self.totalPageCount = totalPageCount
        self.pageNum = 0

        self.buttonFrameFont = font

        self.configure(fg_color="#2e2e2e")

        self.create_widgets()
        self.place_widgets()


    def create_widgets(self):

        self.pageLabel =CTkLabel(self,text=f"{self.pageNum+1}/{self.totalPageCount}",font=self.buttonFrameFont)

        self.nextButton = CTkButton(self,text="-->",width=50,height=50,command=lambda:self.send_new_page_num(1))
        self.preButton = CTkButton(self,text="<--",width=50,height=50,command=lambda:self.send_new_page_num(0))
    

    def create_layout(self,w,h):

        self.rowconfigure([*range(w)],weight=1)
        self.columnconfigure([*range(h)],weight=1)


    def place_widgets(self):

        self.create_layout(1,5)

        self.pack(expand=True,fill=BOTH)
        
        self.pageLabel.grid(row=0,column=2,sticky=NSEW)
        self.nextButton.grid(row=0,column=4)
        self.preButton.grid(row=0,column=0)


    def send_new_page_num(self,direction:bool):

        self.change_page_num(direction)

        self.pageLabel.configure(text=f"{self.pageNum+1}/{self.totalPageCount}")

        self.ChangePageEvent(self.pageNum)

        
    def change_page_num(self,direction:bool):

        self.pageNum = self.pageNum + 1 if direction else self.pageNum - 1

        self.pageNum %= self.totalPageCount

