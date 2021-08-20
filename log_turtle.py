Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 144+28
172
>>> 172/52
3.3076923076923075
>>> clear
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.fd(90)
>>> tao.shape('turtle')
>>> tao.distance(50)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tao.distance(50)
  File "C:\Python39\lib\turtle.py", line 1859, in distance
    return abs(pos - self._position)
UnboundLocalError: local variable 'pos' referenced before assignment
>>> tao.forward(100)
>>> tao.left(90)
>>> for i in range(1,50):
	for j in range(4):
		tao.forward(100)
		tao.left(90)

		
Traceback (most recent call last):
  File "<pyshell#14>", line 4, in <module>
    tao.left(90)
  File "C:\Python39\lib\turtle.py", line 1700, in left
    self._rotate(angle)
  File "C:\Python39\lib\turtle.py", line 3277, in _rotate
    self._update()
  File "C:\Python39\lib\turtle.py", line 2663, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Python39\lib\turtle.py", line 561, in _update
    self.cv.update()
  File "C:\Python39\lib\tkinter\__init__.py", line 1314, in update
    self.tk.call('update')
KeyboardInterrupt

>>> for i in range(1,50):
	for j in range(4):
		tao.forward(100+2*i)
		tao.left(90)

		
Traceback (most recent call last):
  File "<pyshell#16>", line 3, in <module>
    tao.forward(100+2*i)
  File "C:\Python39\lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Python39\lib\turtle.py", line 3182, in _goto
    screen._drawline(self.drawingLineItem, ((0, 0), (0, 0)),
  File "C:\Python39\lib\turtle.py", line 544, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Python39\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> tao = turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tao = turtle.Turtle()
  File "C:\Python39\lib\turtle.py", line 3814, in __init__
    RawTurtle.__init__(self, Turtle._screen,
  File "C:\Python39\lib\turtle.py", line 2558, in __init__
    self._update()
  File "C:\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> for i in range(1,50):
	for j in range(4):
		tao.forward(100+2*i+j)
		tao.left(90)

		
Traceback (most recent call last):
  File "<pyshell#19>", line 3, in <module>
    tao.forward(100+2*i+j)
  File "C:\Python39\lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Python39\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Python39\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Python39\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> import turtle
>>> tao = turtle.Turtle()
>>> for i in range(1,50):
	for j in range(4):
		tao.forward(100+2*i+j)
		tao.left(90)

		
Traceback (most recent call last):
  File "<pyshell#23>", line 4, in <module>
    tao.left(90)
  File "C:\Python39\lib\turtle.py", line 1700, in left
    self._rotate(angle)
  File "C:\Python39\lib\turtle.py", line 3277, in _rotate
    self._update()
  File "C:\Python39\lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Python39\lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Python39\lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
>>> for i in range(1,50):
	for j in range(4):
		tao.forward(100+2*(i+j))
		tao.left(90)

		
Traceback (most recent call last):
  File "<pyshell#25>", line 3, in <module>
    tao.forward(100+2*(i+j))
  File "C:\Python39\lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Python39\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Python39\lib\turtle.py", line 754, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Python39\lib\tkinter\__init__.py", line 2766, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> tao = turtle.Turtle()
>>> for i in range(1,50):
	for j in range(4):
		tao.forward(100+2*(i+j))
		tao.left(90)

		
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(50):
	tao.forward(100+(i*20))
	tao.left(90)

	
>>> tao.reset()
>>> tao.shape('turtle')
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
>>> for i in range(8):
	tao.forward(100)
	tao.left(360/8)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> def ShapeSpin(n=4):
	tao.reset()
	for i in range(100)
	
SyntaxError: invalid syntax
>>> def ShapeSpin(n=4):
	tao.reset()
	for i in range(n):
		tao.forward(100)
		tao.left(360/n)

		
>>> ShapeSpin(20)
>>> ShapeSpin(3)
>>> def ShapeSpin(n=4):
	tao.reset()
	for i in range(n):
		tao.forward(100/n)
		tao.left(360/n)

		
>>> ShapeSpin(20)
>>> ShapeSpin(40)
>>> ShapeSpin(100000)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    ShapeSpin(100000)
  File "<pyshell#51>", line 4, in ShapeSpin
    tao.forward(100/n)
  File "C:\Python39\lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Python39\lib\turtle.py", line 3196, in _goto
    self._update() #count=True)
  File "C:\Python39\lib\turtle.py", line 2663, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Python39\lib\turtle.py", line 561, in _update
    self.cv.update()
  File "C:\Python39\lib\tkinter\__init__.py", line 1314, in update
    self.tk.call('update')
KeyboardInterrupt
>>> ShapeSpin(10)
>>> ShapeSpin(5)
>>> ShapeSpin(6)
>>> ShapeSpin(7)
>>> def ShapeSpin(n=4):
	#tao.reset()
	for i in range(n):
		tao.forward(100/n)
		tao.left(360/n)

		
>>> fot i in range(3,11):
	
SyntaxError: invalid syntax
>>> for i in range(3,11):
	ShapeSpin(i)

	
>>> 
	tao.reset()
	
SyntaxError: unexpected indent
>>> tao.reset()
>>> def ShapeSpin(n=4):
	#tao.reset()
	for i in range(n):
		tao.forward(100)
		tao.left(360/n)

		
>>> for i in range(3,11):
	ShapeSpin(i)

	
>>> for i in range(3,20):
	ShapeSpin(i)

	
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	tao.left(45)

	
>>> tap.reset()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    tap.reset()
NameError: name 'tap' is not defined
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	tao.left(90)

	
>>> def ShapeSim(n=4,l=4)
SyntaxError: invalid syntax
>>> def ShapeSim(n=4,l=4):
	for i in range(l):
		for j in range(n)
		
SyntaxError: invalid syntax
>>> def ShapeSim(n=4,l=4):
	tao.reset()
	for i in range(l):
		for j in range(n):
			tao.forward(100)
			tao.left(360,n)

			
>>> def ShapeSim(n=4,l=4):
	tao.reset()
	for i in range(l):
		for j in range(n):
			tao.forward(100)
			tao.left(360,n)
		tao.left(360/l)

		
>>> ShapeSim(8,4)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    ShapeSim(8,4)
  File "<pyshell#93>", line 6, in ShapeSim
    tao.left(360,n)
TypeError: left() takes 2 positional arguments but 3 were given
>>> def ShapeSim(n=4,l=4):
	tao.reset()
	for i in range(l):
		for j in range(n):
			tao.forward(100)
			tao.left(360/n)
		tao.left(360/l)

		
>>> ShapeSim(8,4)
>>> ShapeSim(1,10)
>>> ShapeSim(8,10)
>>> ShapeSim(4,36)
>>> tao.color('green')
>>> ShapeSim(4,36)
>>> 