import tkinter
root = tkinter.Tk()
root.title("Wheel Of Fortune")

title = tkinter.Label(root, text="Wheel of Fortune")
title.grid(row=1, column=4)

A = tkinter.Button(root, text="A")
A.grid(row=2, column=1)

B = tkinter.Button(root, text="B")
B.grid(row=2, column=2)

C = tkinter.Button(root, text="C")
C.grid(row=2, column=3)

D = tkinter.Button(root, text="D")
D.grid(row=2, column=4)

E = tkinter.Button(root, text="E")
E.grid(row=2, column=5)

F = tkinter.Button(root, text="F")
F.grid(row=2, column=6)

G = tkinter.Button(root, text="G")
G.grid(row=3, column=1)


root.mainloop()