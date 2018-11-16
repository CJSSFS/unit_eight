import tkinter
import random

root = tkinter.Tk()
root.title("Wheel Of Fortune")

answer = []
word = "basketball"
for x in range(len(word)):
    answer.append("_")

entry = tkinter.StringVar()
showword = tkinter.StringVar()
showword.set(answer)
WordLabel = tkinter.Label(root, textvariable=showword)
WordLabel.grid(row=2, column=2)


def check_a():
    print(answer)
    if "a" in word:
        for x in range(len(answer)):
            if "a" == word[x]:
                answer[x] = "a"
    showword.set(answer)


def check_b():
    print(answer)
    if "b" in word:
        for x in range(len(answer)):
            if "b" == word[x]:
                answer[x] = "b"
    showword.set(answer)


def check_c():
    print(answer)
    if "c" in word:
        for x in range(len(answer)):
            if "c" == word[x]:
                answer[x] = "c"
    showword.set(answer)


def check_d():
    print(answer)
    if "d" in word:
        for x in range(len(answer)):
            if "d" == word[x]:
                answer[x] = "d"
    showword.set(answer)


def check_e():
    print(answer)
    if "e" in word:
        for x in range(len(answer)):
            if "e" == word[x]:
                answer[x] = "e"
    showword.set(answer)


def check_f():
    print(answer)
    if "f" in word:
        for x in range(len(answer)):
            if "f" == word[x]:
                answer[x] = "f"
    showword.set(answer)


def check_g():
    print(answer)
    if "g" in word:
        for x in range(len(answer)):
            if "g" == word[x]:
                answer[x] = "g"
    showword.set(answer)


def check_h():
    print(answer)
    if "h" in word:
        for x in range(len(answer)):
            if "h" == word[x]:
                answer[x] = "h"
    showword.set(answer)


def check_i():
    print(answer)
    if "i" in word:
        for x in range(len(answer)):
            if "i" == word[x]:
                answer[x] = "i"
    showword.set(answer)


def check_j():
    print(answer)
    if "j" in word:
        for x in range(len(answer)):
            if "j" == word[x]:
                answer[x] = "j"
    showword.set(answer)


def check_k():
    print(answer)
    if "k" in word:
        for x in range(len(answer)):
            if "k" == word[x]:
                answer[x] = "k"
    showword.set(answer)


def check_l():
    print(answer)
    if "l" in word:
        for x in range(len(answer)):
            if "l" == word[x]:
                answer[x] = "l"
    showword.set(answer)


def check_m():
    print(answer)
    if "m" in word:
        for x in range(len(answer)):
            if "m" == word[x]:
                answer[x] = "m"
    showword.set(answer)


def check_n():
    print(answer)
    if "n" in word:
        for x in range(len(answer)):
            if "n" == word[x]:
                answer[x] = "n"
    showword.set(answer)


def check_o():
    print(answer)
    if "o" in word:
        for x in range(len(answer)):
            if "o" == word[x]:
                answer[x] = "o"
    showword.set(answer)


def check_p():
    print(answer)
    if "p" in word:
        for x in range(len(answer)):
            if "p" == word[x]:
                answer[x] = "p"
    showword.set(answer)


def check_q():
    print(answer)
    if "q" in word:
        for x in range(len(answer)):
            if "q" == word[x]:
                answer[x] = "q"
    showword.set(answer)


def check_r():
    print(answer)
    if "r" in word:
        for x in range(len(answer)):
            if "r" == word[x]:
                answer[x] = "r"
    showword.set(answer)


def check_s():
    print(answer)
    if "s" in word:
        for x in range(len(answer)):
            if "s" == word[x]:
                answer[x] = "s"
    showword.set(answer)


def check_t():
    print(answer)
    if "t" in word:
        for x in range(len(answer)):
            if "t" == word[x]:
                answer[x] = "t"
    showword.set(answer)


def check_u():
    print(answer)
    if "u" in word:
        for x in range(len(answer)):
            if "u" == word[x]:
                answer[x] = "u"
    showword.set(answer)


def check_v():
    print(answer)
    if "v" in word:
        for x in range(len(answer)):
            if "v" == word[x]:
                answer[x] = "v"
    showword.set(answer)


def check_w():
    print(answer)
    if "w" in word:
        for x in range(len(answer)):
            if "w" == word[x]:
                answer[x] = "w"
    showword.set(answer)


def check_x():
    print(answer)
    if "x" in word:
        for x in range(len(answer)):
            if "x" == word[x]:
                answer[x] = "x"
    showword.set(answer)


def check_y():
    print(answer)
    if "y" in word:
        for x in range(len(answer)):
            if "y" == word[x]:
                answer[x] = "y"
    showword.set(answer)


def check_z():
    print(answer)
    if "z" in word:
        for x in range(len(answer)):
            if "z" == word[x]:
                answer[x] = "z"
    showword.set(answer)


title = tkinter.Label(root, text="Wheel of Fortune")
title.grid(row=1, column=4)

GuessTheWord = tkinter.Label(root, text="Guess the Word:")
GuessTheWord.grid(row=2, column=1)

A = tkinter.Button(root, text="A", command=check_a)
A.grid(row=4, column=1)

B = tkinter.Button(root, text="B",command=check_b)
B.grid(row=4, column=2)

C = tkinter.Button(root, text="C",command=check_c)
C.grid(row=4, column=3)

D = tkinter.Button(root, text="D",command=check_d)
D.grid(row=4, column=4)

E = tkinter.Button(root, text="E", command=check_e)
E.grid(row=4, column=5)

F = tkinter.Button(root, text="F", command=check_f)
F.grid(row=4, column=6)

G = tkinter.Button(root, text="G", command=check_g)
G.grid(row=5, column=1)

H = tkinter.Button(root, text="H", command=check_h)
H.grid(row=5, column=2)

I = tkinter.Button(root, text="I", command=check_i)
I.grid(row=5, column=3)

J = tkinter.Button(root, text="J", command=check_j)
J.grid(row=5, column=4)

K = tkinter.Button(root, text="K", command=check_k)
K.grid(row=5, column=5)

L = tkinter.Button(root, text="L", command=check_l)
L.grid(row=5, column=6)

M = tkinter.Button(root, text="M", command=check_m)
M.grid(row=6, column=1)

N = tkinter.Button(root, text="N", command=check_n)
N.grid(row=6, column=2)

O = tkinter.Button(root, text="O", command=check_o)
O.grid(row=6, column=3)

P = tkinter.Button(root, text="P", command=check_p)
P.grid(row=6, column=4)

Q = tkinter.Button(root, text="Q", command=check_q)
Q.grid(row=6, column=5)

R = tkinter.Button(root, text="R", command=check_r)
R.grid(row=6, column=6)

S = tkinter.Button(root, text="S", command=check_s)
S.grid(row=7, column=1)

T = tkinter.Button(root, text="T", command=check_t)
T.grid(row=7, column=2)

U = tkinter.Button(root, text="U", command=check_u)
U.grid(row=7, column=3)

V = tkinter.Button(root, text="V", command=check_v)
V.grid(row=7, column=4)

W = tkinter.Button(root, text="W", command=check_w)
W.grid(row=7, column=5)

X = tkinter.Button(root, text="X", command=check_x)
X.grid(row=7, column=6)

Y = tkinter.Button(root, text="Y", command=check_y)
Y.grid(row=8, column=1)

Z = tkinter.Button(root, text="Z", command=check_z)
Z.grid(row=8, column=2)


root.mainloop()