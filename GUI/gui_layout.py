from customtkinter import *
from config import *

def action():
    print("Activated!")

main = CTk()

w,h = 640,480

main.title("SmileOS 2.0")
main.geometry(f"{w}x{h}")
main.maxsize(w,h)
main.minsize(w,h)

buttonFrame = CTkFrame(main,bg_color=colors["dark_grey"],fg_color=colors["dark_grey"],width=240,height=480)
miniFrame = CTkFrame(buttonFrame,bg_color="transparent",fg_color="transparent")


tipOutFrame = CTkFrame(main,bg_color=colors["dark_grey"],fg_color=colors["dark_grey"],width=400,height=480,border_color=colors["dark_grey"],border_width=30)
tipInFrame = CTkFrame(tipOutFrame,bg_color=colors["darkest_grey"],fg_color=colors["darkest_grey"],width=370,height=450)

buttonFrame.pack(side=LEFT,expand=True,fill=BOTH)

tipOutFrame.pack(side=LEFT,expand=True,fill=BOTH)
tipOutFrame.pack_propagate(False)

tipOutFrame.columnconfigure((0,1,2),weight=1)
tipOutFrame.rowconfigure((0,1,2),weight=1)


tipInFrame.grid(row=1,column=1)
tipInFrame.grid_propagate(False)


buttonFrame.rowconfigure((0,1,2,3,4,5,6),weight=2)
buttonFrame.columnconfigure((1,2,3),weight=1)

miniFrame.grid(row=3,column=2)

label1 = CTkLabel(buttonFrame,text= "Smile OS 2.0")

button1 = CTkButton(miniFrame,text="Enemies",command=action,width=200,height=45,fg_color=colors["darker_grey"])
button2 = CTkButton(miniFrame,text="Books",command=action,width=200,height=45,fg_color=colors["darker_grey"])
button3 = CTkButton(miniFrame,text="Testaments",command=action,width=200,height=45,fg_color=colors["darker_grey"])
button4 = CTkButton(miniFrame,text="Prime Data",command=action,width=200,height=45,fg_color=colors["darker_grey"])



button1.pack(pady=2,expand=True,fill=BOTH)
button2.pack(pady=2,expand=True,fill=BOTH)
button3.pack(pady=2,expand=True,fill=BOTH)
button4.pack(pady=2,expand=True,fill=BOTH)



main.mainloop()
