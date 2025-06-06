Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import turtle
tao = turtle.pen()
tao = turtle.Pen()
type(tao)
<class 'turtle.Turtle'>
tao.shape('turtle')
tao.color('red')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.reset()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.color('red')
for i in range(8):
    tao.forward(100)
    tao.left(45)

    
for i in range(4):
    print(i)
    tao.forward(100)
    tao.left(90)

    
0
1
2
3
list(range(4))
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
list(range(1,4))
[1, 2, 3]
list(range(1,5))
[1, 2, 3, 4]
lilst(range(0,10,2))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    lilst(range(0,10,2))
NameError: name 'lilst' is not defined. Did you mean: 'list'?
list(range(0,10,2))
[0, 2, 4, 6, 8]
list(range(0,11,2))
[0, 2, 4, 6, 8, 10]
# สร้างเต่าขึ้นมาอีกตัว
[0, 2, 4, 6, 8, 10]# สร้างเต่าขึ้นมาอีกตัว
[0, 2, 4, 6, 8, 10]

tao.up
<bound method TPen.penup of <turtle.Turtle object at 0x0000024272F896D0>>
tao.up()
taolist = []
tao.reset()
for i in range(8):
    tao.forward(100)
    tao.left(45)

    
tao.up()
tao.goto(30,30)
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.down()
for i in range(4):
    tao.forward(50)
    tao.left(90)

    
taolist = []
tao1 = turtle.Pen()
tao2 = turtle.pen()
taolist.append(tao)
taolist.append(tao1)
taolist.append(tao2)
print(taolist)
[<turtle.Turtle object at 0x0000024272F896D0>, <turtle.Turtle object at 0x0000024272F89E50>, {'shown': True, 'pendown': True, 'pencolor': 'black', 'fillcolor': 'black', 'pensize': 1, 'speed': 3, 'resizemode': 'noresize', 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1, 'tilt': 0.0}]
taolist[0].forward(200)
taolist[1].backward(200)
taolist[2].color('red')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    taolist[2].color('red')
AttributeError: 'dict' object has no attribute 'color'
taolist[2].left(90)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    taolist[2].left(90)
AttributeError: 'dict' object has no attribute 'left'
aolist = []
tao1 = turtle.Pen()
tao2 = turtle.Pen()
taolist.append(tao)
taolist.append(tao1)
taolist.append(tao2)
SyntaxError: multiple statements found while compiling a single statement
taolist = []
tao1 = turtle.Pen()
tao2 = turtle.Pen()
... taolist.append(tao)
... taolist.append(tao1)
... taolist.append(tao2)
... print(taolist)
SyntaxError: multiple statements found while compiling a single statement
>>> tao.reset()
>>> taolist = []
... tao1 = turtle.Pen()
... tao2 = turtle.Pen()
... taolist.append(tao)
... taolist.append(tao1)
... taolist.append(tao2)
SyntaxError: multiple statements found while compiling a single statement
>>> tao.reset()
>>> 
>>> tao.reset()
>>> 
>>> taolist = []
>>> tao1 = turtle.Pen()
>>> tao2 = turtle.Pen()
>>> taolist.append(tao)
>>> taolist.append(tao1)
>>> taolist.append(tao2)
\
>>> print(taolist)
[<turtle.Turtle object at 0x0000024272F896D0>, <turtle.Turtle object at 0x0000024272F8A0D0>, <turtle.Turtle object at 0x0000024272F8A210>]
>>> taolist[0].forward(200)
>>> taolist[1].backward(200)
>>> taolist[2].color('red')
>>> taolist[2].left(90)
>>> taolist[2].forward(100)
>>> for t in taolist:
...     for i in range(4):
...         t.forward(50)
...         t.left(90)
... 
...         
