from customtkinter import *

def action():
    print("Activated!")

main = CTk()

main.title("SmileOS 2.0")
main.geometry("640x480")
main.minsize(640,480)

buttonFrame = CTkFrame(main,bg_color="#2e2e2e",fg_color="#2e2e2e",width=240,height=480)
tipFrame = CTkFrame(main,bg_color="blue",fg_color="blue",width=400,height=480)

miniFrame = CTkFrame(buttonFrame,bg_color="transparent",fg_color="transparent")


buttonFrame.pack(side=LEFT,expand=True,fill=BOTH)

tipFrame.pack(side=LEFT,expand=True,fill=BOTH)
tipFrame.pack_propagate(False)


buttonFrame.rowconfigure((0,1,2,3,4,5,6),weight=2)
buttonFrame.columnconfigure((1,2,3),weight=1)

miniFrame.grid(row=3,column=2)

label1 = CTkLabel(buttonFrame,text= "Smile OS 2.0")

button1 = CTkButton(miniFrame,text="Click Me!",command=action,width=200,height=45,fg_color="#252525")
button2 = CTkButton(miniFrame,text="Click Me!",command=action,width=200,height=45,fg_color="#252525")
button3 = CTkButton(miniFrame,text="Click Me!",command=action,width=200,height=45,fg_color="#252525")
button4 = CTkButton(miniFrame,text="Click Me!",command=action,width=200,height=45,fg_color="#252525")

label1.grid(row=1,column=2,sticky=NSEW)


button1.pack(pady=2,expand=True,fill=BOTH)
button2.pack(pady=2,expand=True,fill=BOTH)
button3.pack(pady=2,expand=True,fill=BOTH)
button4.pack(pady=2,expand=True,fill=BOTH)


label = CTkLabel(tipFrame,text="H a v e   F u n")
label.pack()


main.mainloop()
