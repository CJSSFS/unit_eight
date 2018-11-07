import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")
F_Label = tkinter.Label(root, text="degrees F: ")
F_Label.grid(row=1, column=1)

F_Label_entry = tkinter.Entry(root)
F_Label_entry.grid(row=1, column=2)

C_Label = tkinter.Label(root, text="degrees C:")
C_Label.grid(row=2, column=1)

C_Temp_Label = tkinter.Label(root)
C_Temp_Label.grid(row=2, column=2)
root.mainloop()