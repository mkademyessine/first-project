
from tkinter import *
from tkinter import messagebox as mb
import json

root = Tk()
root.geometry("800x500")
root.title("Quiz")
#define the first quiz
with open('politique.json') as f:
    obj = json.load(f)
q = (obj['ques'])
options = (obj['options'])
a = (obj['ans'])

#define the sencond quiz
with open('culture.json') as f:
    obj2 = json.load(f)
q2 = (obj2['ques'])
options2 = (obj2['options'])
a2 = (obj2['ans'])
#define the third quiz
with open('sport.json') as f:
    obj3 = json.load(f)
q3 = (obj3['ques'])
options3 = (obj3['options'])
a3 = (obj3['ans'])
#define the fourth quiz
with open('geographie.json') as f:
    obj4 = json.load(f)
q4 = (obj4['ques'])
options4 = (obj4['options'])
a4 = (obj4['ans'])

class Quiz2:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Quiz in General Culture", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q2[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn


    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q2[qn]
        for op in options2[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="green", fg="white",
                         font=("times", 16, "bold"))
        nbutton.place(x=200, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                            font=("times", 16, "bold"))
        quitbutton.place(x=380, y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a2[qn]:
            return True

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q2):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q2) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q2) - self.correct
        correct = "Number of correct answers: " + str(self.correct)
        wrong = "Number of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

#define the second quiz

class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Quiz in Politics", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn


    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="green", fg="white",
                         font=("times", 16, "bold"))
        nbutton.place(x=200, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                            font=("times", 16, "bold"))
        quitbutton.place(x=380, y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "Number of correct answers: " + str(self.correct)
        wrong = "Number of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

#define the third quiz
class Quiz3:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Quiz in Sport", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q3[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn


    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q3[qn]
        for op in options3[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="green", fg="white",
                         font=("times", 16, "bold"))
        nbutton.place(x=200, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                            font=("times", 16, "bold"))
        quitbutton.place(x=380, y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a3[qn]:
            return True

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q3):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q3) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q3) - self.correct
        correct = "Number of correct answers: " + str(self.correct)
        wrong = "Number of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

#define the fourth quiz
class Quiz4:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Quiz in Geographie", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q4[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn


    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q4[qn]
        for op in options4[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="green", fg="white",
                         font=("times", 16, "bold"))
        nbutton.place(x=200, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                            font=("times", 16, "bold"))
        quitbutton.place(x=380, y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a4[qn]:
            return True

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q4):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q4) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q4) - self.correct
        correct = "Number of correct answers: " + str(self.correct)
        wrong = "Number of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

def sport():
    quiz = Quiz3()

def culture():
    quiz = Quiz2()

def geographie():
    quiz = Quiz4()

def politique():
    quiz = Quiz()

t = Label(root, text="Choose The Domain Of The Quiz", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
t.place(x=0, y=2)
bouts=Button(root,text ='Sport',font=("times", 20, "bold"),width=20,bg='bisque',command=lambda :[bouts.place_forget() ,
     boutc.place_forget(), boutp.place_forget(),boutg.place_forget(),sport()])
bouts.place(x=50,y=100)
boutc=Button(root,text ='General Knowledge',font=("times", 20, "bold"),width=20,bg='bisque',command=lambda :[bouts.place_forget() ,
     boutc.place_forget(), boutp.place_forget(),boutg.place_forget(), culture()])
boutc.place(x=400,y=100)
boutg=Button(root,text ='Geography',font=("times", 20, "bold"),width=20,bg='bisque',command=lambda :[bouts.place_forget() ,
  boutc.place_forget(), boutp.place_forget(),boutg.place_forget() , geographie()])
boutg.place(x=50,y=160)
boutp=Button(root,text ='Politics',font=("times", 20, "bold"),width=20,bg='bisque',command=lambda :[bouts.place_forget() ,
    boutc.place_forget(), boutp.place_forget(),boutg.place_forget() , politique()])
boutp.place(x=400,y=160)


#quiz = Quiz()
root.mainloop()
