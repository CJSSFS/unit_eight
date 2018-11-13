import tkinter


def f_to_c():
    fahrenheit = int(f_value.get())
    celsius = 5 / 9 * (fahrenheit - 32)
    c_value.set(str(celsius))


root = tkinter.Tk()
f_value = tkinter.StringVar()
c_value = tkinter.StringVar()

f_value.set("0")

root.title("Temperature Converter")
F_Label = tkinter.Label(root, text="degrees F: ")
F_Label.grid(row=1, column=1)

F_Label_entry = tkinter.Entry(root, textvariable=f_value)
F_Label_entry.grid(row=1, column=2)

C_Label = tkinter.Label(root, text="degrees C:")
C_Label.grid(row=2, column=1)

C_Temp_Label = tkinter.Label(root, textvariable=c_value)
C_Temp_Label.grid(row=2, column=2, sticky="W")

convert_button = tkinter.Button(root, text="Convert", command=f_to_c)
convert_button.grid(row=3, column=1, columnspan=2)

root.mainloop()