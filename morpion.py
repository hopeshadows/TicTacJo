import tkinter

"""def morpion():"""

fen = tkinter.Tk()
fen.title("Morpion")
fen.geometry("502x602")
fen.resizable(width=False, height=False)

back = tkinter.PhotoImage(file="back.png")
canv = tkinter.Canvas(fen, width=500, height=600,)
canv.create_image(250,300,image=back)
canv.place(x=0,y=0)

N=1
S="O"

score_p1=0
score_p2=0

a=2
b=2
c=2

d=2
e=2
f=2

g=2
h=2
i=2

score = tkinter.Label(text="0  ", fg="#E1C04B", background='#141414', font=("Eras Bold ITC", 20))
score.place(x=420, y=553)
score = tkinter.Label(text="0  ", fg="#E1C04B", background='#141414', font=("Eras Bold ITC", 20))
score.place(x=420, y=513)

pastille = tkinter.Label(text="•", fg="#E1C04B", background='#141414', font=("Eras Bold ITC", 20))
pastille.place(x=100, y=513)

def changement_signe():
    global N
    global S
    if N==1:
        S="O"
        pastille.place(x=100, y=553)
    else:
        S="X "
        pastille.place(x=100, y=513)
    N=N*(-1)

def place():
    print(a,b,c,d,e,f,g,h,i)
    def test():
        if a==b==c!=2:
            fin(N)
        elif d==e==f!=2:
            fin(N)
        elif g==h==i!=2:
            fin(N)

        elif a==d==g!=2:
            fin(N)
        elif b==e==h!=2:
            fin(N)
        elif c==f==i!=2:
            fin(N)

        elif a==e==i!=2:
            fin(N)
        elif c==e==g!=2:
            fin(N)

        elif a+b+c+d+e+f+g+h+i==1 or a+b+c+d+e+f+g+h+i==-1:
            replay()

    def activation_a():
        global N
        global a
        a=N
        changement_signe()
        button_a.destroy()
        Label = tkinter.Label(text=""+S, fg="white", background='#141414', font=("Eras Bold ITC", 40))
        Label.place(x=140, y=128)
        test()

    def activation_b():
        global N
        global b
        b=N
        changement_signe()
        button_b.destroy()
        Label = tkinter.Label(text=""+S, fg="white", background='#141414', font=("Eras Bold ITC", 40))
        Label.place(x=226, y=128)
        test()

    def activation_c():
        global N
        global c
        c=N
        changement_signe()
        button_c.destroy()
        Label = tkinter.Label(text=""+S, fg="white", background='#141414', font=("Eras Bold ITC", 40))
        Label.place(x=311, y=128)
        test()

    def activation_d():
        global N
        global d
        d=N
        changement_signe()
        button_d.destroy()
        Label = tkinter.Label(text=""+S, fg="white", background='#141414', font=("Eras Bold ITC", 40))
        Label.place(x=140, y=214)
        test()

    def activation_e():
        global N
        global e
        e=N
        changement_signe()
        button_e.destroy()
        Label = tkinter.Label(text=""+S, fg="white", background='#141414', font=("Eras Bold ITC", 40))
        Label.place(x=226, y=214)
        test()

    def activation_f():
        global N
        global f
        f=N
        changement_signe()
        button_f.destroy()
        Label = tkinter.Label(text=""+S, fg="white", background='#141414', font=("Eras Bold ITC", 40))
        Label.place(x=311, y=214)
        test()

    def activation_g():
        global N
        global g
        g=N
        changement_signe()
        button_g.destroy()
        Label = tkinter.Label(text=""+S, fg="white", background='#141414', font=("Eras Bold ITC", 40))
        Label.place(x=140, y=300)
        test()

    def activation_h():
        global N
        global h
        h=N
        changement_signe()
        button_h.destroy()
        Label = tkinter.Label(text=""+S, fg="white", background='#141414', font=("Eras Bold ITC", 40))
        Label.place(x=226, y=300)
        test()

    def activation_i():
        global N
        global i
        i=N
        changement_signe()
        button_i.destroy()
        Label = tkinter.Label(text=""+S, fg="white", background='#141414', font=("Eras Bold ITC", 40))
        Label.place(x=311, y=300)
        test()

    def reset():
        global score_p1, score_p2, N
        score_p1=0
        score_p2=0
        score = tkinter.Label(text="0  ", fg="#E1C04B", background='#141414', font=("Eras Bold ITC", 20))
        score.place(x=420, y=553)
        score = tkinter.Label(text="0  ", fg="#E1C04B", background='#141414', font=("Eras Bold ITC", 20))
        score.place(x=420, y=513)
        replay()

    button_a = tkinter.Button(text="", background="#141414", command=activation_a,  height = 4, width = 9)
    button_a.place(x=130, y=128)

    button_b = tkinter.Button(text="", background="#141414", command=activation_b,  height = 4, width = 9)
    button_b.place(x=216, y=128)

    button_c = tkinter.Button(text="", background="#141414", command=activation_c,  height = 4, width = 9)
    button_c.place(x=301, y=128)

    #2eme ligne
    button_d = tkinter.Button(text="", background="#141414", command=activation_d,  height = 4, width = 9)
    button_d.place(x=130, y=214)

    button_e = tkinter.Button(text="", background="#141414", command=activation_e,  height = 4, width = 9)
    button_e.place(x=216, y=214)

    button_f = tkinter.Button(text="", background="#141414", command=activation_f,  height = 4, width = 9)
    button_f.place(x=301, y=214)

    #3eme ligne
    button_g = tkinter.Button(text="", background="#141414", command=activation_g,  height = 4, width = 9)
    button_g.place(x=130, y=300)

    button_h = tkinter.Button(text="", background="#141414", command=activation_h,  height = 4, width = 9)
    button_h.place(x=216, y=300)

    button_i = tkinter.Button(text="", background="#141414", command=activation_i,  height = 4, width = 9)
    button_i.place(x=301, y=300)

    def replay():
        global a,b,c,d,e,f,g,h,i

        button_a.destroy()
        button_b.destroy()
        button_c.destroy()
        button_d.destroy()
        button_e.destroy()
        button_f.destroy()
        button_g.destroy()
        button_h.destroy()
        button_i.destroy()

        a=2
        b=2
        c=2

        d=2
        e=2
        f=2

        g=2
        h=2
        i=2

        place()

    def fin(n):
        global score_p1
        global score_p2
        if n==1:
            score_p2=score_p2+1
            score = tkinter.Label(text=""+str(score_p2), fg="#E1C04B", background='#141414', font=("Eras Bold ITC", 20))
            score.place(x=420, y=553)
            replay()
        else:
            score_p1=score_p1+1
            score = tkinter.Label(text=""+str(score_p1), fg="#E1C04B", background='#141414', font=("Eras Bold ITC", 20))
            score.place(x=420, y=513)
            replay()


    button = tkinter.Button(text="reset", fg="white", background='#141414', font=("Eras Bold ITC", 11), command=reset, height = 3, width = 6)
    button.place(x=20, y=520)


place()
fen.mainloop()
