import random
from tkinter import Label , Tk , Text , Canvas , Button
from tkinter.messagebox import showinfo , showwarning
from tkinter import *
from random import randint

root = Tk()
root.title('Magic Squares')
root.geometry('600x500')
root.resizable(False, False)
canvas = Canvas(root , width = 600 , height=500)
canvas.pack()

Lab = Label(text= "Магический квадрат", font=("Times 30", 20))
canvas.create_window(300, 100, window=Lab)

playBut = Button(root , text="Играть", font=("Times 30", 16), width=8)
canvas.create_window(300, 200, window=playBut)

x1 = Text(root, width=4, height=2)
x2 = Text(root, width=4, height=2)
x3 = Text(root, width=4, height=2)
x4 = Text(root, width=4, height=2)
x5 = Text(root, width=4, height=2)
x6 = Text(root, width=4, height=2)
x7 = Text(root, width=4, height=2)
x8 = Text(root, width=4, height=2)
x9 = Text(root, width=4, height=2)

def ui():
    canvas.delete('all')
    canvas.create_window(300, 100, window=Label(text=Numb, font=('Times 30', 20)))
    canvas.create_window(250, 180, window=x1)
    canvas.create_window(300, 180, window=x2)
    canvas.create_window(350, 180, window=x3)
    canvas.create_window(250, 230, window=x4)
    canvas.create_window(300, 230, window=x5)
    canvas.create_window(350, 230, window=x6)
    canvas.create_window(250, 280, window=x7)
    canvas.create_window(300, 280, window=x8)
    canvas.create_window(350, 280, window=x9)
    canvas.create_window(300, 350, window= get)

def rand():
    global Numb
    list = ['15', '21', '22', '24', '27', '30', '33', '36', '42']
    Numb = random.choice(list)
    ui()

def game():
    n1 = x1.get(0.0, 6.0)
    n2 = x2.get(0.0, 3.0)
    n3 = x3.get(0.0, 3.0)
    n4 = x4.get(0.0, 3.0)
    n5 = x5.get(0.0, 3.0)
    n6 = x6.get(0.0, 3.0)
    n7 = x7.get(0.0, 3.0)
    n8 = x8.get(0.0, 3.0)
    n9 = x9.get(0.0, 3.0)
    if n1 == '\n' or n2 == '\n' or n3 == '\n' or n4 == '\n' or n5 == '\n' or n6 == '\n' or n7 == '\n' or n8 == '\n' or n9 == '\n':
        showwarning('Error!', 'Пожалуйста, заполните пустые ячейки числами')
    else:
            s1 = int(n1) + int(n2) + int(n3)
            s2 = int(n4) + int(n5) + int(n6)
            s3 = int(n7) + int(n8) + int(n9)
            s4 = int(n1) + int(n4) + int(n7)
            s5 = int(n2) + int(n5) + int(n8)
            s6 = int(n3) + int(n6) + int(n9)
            s7 = int(n1) + int(n5) + int(n9)
            if int(s1) and int(s2) and int(s3) and int(s4) and int(s5) and int(s6) and int(s7) == int(Numb):
                showinfo('Congratulations!', 'Вы успешно решили магический квадрат!')
            else:
                if (int(n1) == int(n2) or int(n1) == int(n3) or int(n1) == int(n4) or int(n5) == int(n6) or int(n7) == int(n8) or int(n1) == int(n9)
                        or int(n2) == int(n3) or int(n2) == int(n4) or int(n2) == int(n5) or int(n2) == int(n6) or int(n2) == int(n7) or int(n2) == int(n8) or int(n2) == int(n9)
                        or int(n3) == int(n4) or int(n3) == int(n5) or int(n3) == int(n6) or int(n3) == int(n7) or int(n3) == int(n8) or int(n3) == int(n9)
                        or int(n4) == int(n5) or int(n4) == int(n6) or int(n4) == int(n7) or int(n4) == int(n8) or int(n4) == int(n9)
                        or int(n5) == int(n6) or int(n5) == int(n7) or int(n5) == int(n8) or int(n5) == int(n9)
                        or int(n6) == int(n7) or int(n6) == int(n8) or int(n6) == int(n9)
                        or int(n7) == int(n8) or int(n7) == int(n9) or int(n8) == int(n9)):
                    showwarning("Error", "Пожалуйста, не вводите одно и тоже число в разные ячайки")
                else:
                    showwarning('Error!','Пожалуйста, убедитесь, что сумма строк и столбцов совпадает с указанным выше числом.')

get=Button(root , text='Вполнить' , font=('Times 30' , 16), width=8 , command=game)

#Правила игры-----------------------------------------------------------------------------------------------------------
ruleBut = Button(root , text="Правила", font=("Times 30", 16), width=8)
canvas.create_window(300, 260, window = ruleBut)

def rules():
    canvas.delete("all")
    Lab2 = Label(text="Правила игры", font=("Times 30", 20))
    canvas.create_window(300, 100, window=Lab2)
    canvas.create_window(300, 150, window=Label(root, text='Целью игры являетя заполнить ', font=('Times 30', 16)))
    canvas.create_window(300, 180, window=Label(root, text='пустые ячейик числами так, чтобы', font=('Times 30', 16)))
    canvas.create_window(300, 210, window=Label(root, text='сумма по горизонтали, вертикали и,', font=('Times 30', 16)))
    canvas.create_window(300, 240, window=Label(root, text='по диагонали были равны. При каждом ', font=('Times 30', 16)))
    canvas.create_window(300, 270, window=Label(root, text='новом запуске игры необхадимая сумма ', font=('Times 30', 16)))
    canvas.create_window(300, 300, window=Label(root, text='будет рандомна меняться.', font=('Times 30', 16)))

    playBut = Button(root, text="Играть", font=("Times 30", 16), width=8)
    canvas.create_window(150, 400, window=playBut)
    playBut.configure(command = rand)


#Выход из игры----------------------------------------------------------------------------------------------------------
exitBut = Button(root , text="Выйти", font=("Times 30", 16), width=8)
canvas.create_window(300, 320, window = exitBut)



playBut.configure(command = rand)
ruleBut.configure(command = rules)
exitBut.configure(command = root.quit)


root.mainloop()
