import tkinter

root = tkinter.Tk()
f_value = tkinter.StringVar()
c_value = tkinter.StringVar()
root.title("Temperature Converter")
F_Label = tkinter.Label(root, text="degrees F: ")
F_Label.grid(row=1, column=1)

F_Label_entry = tkinter.Entry(root, textvariable=f_value)
F_Label_entry.grid(row=1, column=2)

C_Label = tkinter.Label(root, text="degrees C:")
C_Label.grid(row=2, column=1)

C_Temp_Label = tkinter.Label(root, textvariable=c_value)
C_Temp_Label.grid(row=2, column=2)
root.mainloop()