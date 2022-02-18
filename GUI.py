import tkinter

root = tkinter.Tk()
root.geometry("500x500")

def exit_app():
    print("thanks for using our program")
    exit()
    
frame = tkinter.Frame(root)
frame.pack()

button = tkinter.Button(frame, text="QUIT", fg="black",command=exit_app)
button.pack(side=tkinter.TOP)

root.mainloop()
    