import tkinter


root = tkinter.Tk()
root.title("Wheel Of Fortune")


def one():
    answer = entry.get()
    entry.set(answer + "A")


entry = tkinter.StringVar()

title = tkinter.Label(root, text="Wheel of Fortune")
title.grid(row=1, column=4, columnspan=5)

main_entry = tkinter.Entry(root, textvariable=entry)
main_entry.grid(row=2, column=1, columnspan=6)

A = tkinter.Button(root, text="A", command=one)
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

H = tkinter.Button(root, text="H")
H.grid(row=3, column=2)

I = tkinter.Button(root, text="I")
I.grid(row=3, column=3)

J = tkinter.Button(root, text="J")
J.grid(row=3, column=4)

K = tkinter.Button(root, text="K")
K.grid(row=3, column=5)

L = tkinter.Button(root, text="L")
L.grid(row=3, column=6)

M = tkinter.Button(root, text="M")
M.grid(row=4, column=1)

N = tkinter.Button(root, text="N")
N.grid(row=4, column=2)

O = tkinter.Button(root, text="O")
O.grid(row=4, column=3)

P = tkinter.Button(root, text="P")
P.grid(row=4, column=4)

Q = tkinter.Button(root, text="Q")
Q.grid(row=4, column=5)

R = tkinter.Button(root, text="R")
R.grid(row=4, column=6)

S = tkinter.Button(root, text="S")
S.grid(row=5, column=1)

T = tkinter.Button(root, text="T")
T.grid(row=5, column=2)

U = tkinter.Button(root, text="U")
U.grid(row=5, column=3)

V = tkinter.Button(root, text="V")
V.grid(row=5, column=4)

W = tkinter.Button(root, text="W")
W.grid(row=5, column=5)

V = tkinter.Button(root, text="V")
V.grid(row=5, column=6)

Y = tkinter.Button(root, text="Y")
Y.grid(row=6, column=1)

Z = tkinter.Button(root, text="Z")
Z.grid(row=6, column=2)


root.mainloop()