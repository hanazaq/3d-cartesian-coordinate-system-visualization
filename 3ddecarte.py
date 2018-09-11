import turtle
turtle.speed(0)
turtle.screensize()
turtle.setup(width = 1.0, height = 1.0)
turtle.penup()
turtle.goto(-469.846310393,0)
turtle.pendown()
angle=[40,140,40]
turtle.right(20)
for s in (angle):
	turtle.fd(500)
	turtle.left(s)
turtle.fd(500)

turtle.penup()
turtle.goto(-469.846310393,0)
turtle.pendown()
turtle.left(140)
for i in range(5):
	
	turtle.fd(500)
	turtle.left(40)
	turtle.fd(50)
	turtle.left(140)
	turtle.fd(500)
	turtle.right(140)
	turtle.fd(50)
	turtle.right(40)
turtle.right(140)

for i in range(5):	
	turtle.fd(500)
	turtle.left(140)
	turtle.fd(50)
	turtle.left(40)
	turtle.fd(500)
	turtle.right(40)
	turtle.fd(50)
	turtle.right(140)
print ((469.846310393**2)+(171.010071663**2))**0.5
x=turtle.Turtle('triangle')
xx=turtle.Turtle('triangle')
y=turtle.Turtle('triangle')
yy=turtle.Turtle('triangle')
z=turtle.Turtle('triangle')
zz=turtle.Turtle('triangle')

x.shapesize(.5)
xx.shapesize(.5)
y.shapesize(.5)
yy.shapesize(.5)
z.shapesize(.5)
zz.shapesize(.5)

x.speed(0)
xx.speed(0)
y.speed(0)
yy.speed(0)
z.speed(0)
zz.speed(0)
x.color("red")
xx.color("red")
y.color("blue")
yy.color("blue")
z.color("green")
zz.color("light green")
x.width(2)
xx.width(2)
y.width(2)
yy.width(2)
z.width(2)
zz.width(2)
z.setheading(90)
for i in range(1,5):
	z.fd(50)
	z.dot()
	z.write(i)
z.fd(50)
zz.setheading(-90)
for i in range(1,5):
	zz.fd(50)
	zz.dot()
	zz.write(-i)
zz.fd(50)
xx.setheading(20)
for i in range(1,5):
	xx.fd(50)
	xx.dot()
	xx.write(-i)
xx.fd(50)
x.setheading(200)
for i in range(1,5):
	x.fd(50)
	x.dot()
	x.write(i)
x.fd(50)
y.setheading(-20)
for i in range(1,5):
	y.fd(50)
	y.dot()
	y.write(i)
y.fd(50)
yy.setheading(160)
for i in range(1,5):
	yy.fd(50)
	yy.dot()
	yy.write(-i)
yy.fd(50)


a=-3
b=-4
c=5
point=turtle.Turtle('circle')
point.color("orange")
point.penup()
if a>0:
	point.setheading(200)
	point.fd(a*50)
elif a<0:
	point.setheading(20)
	point.fd(a*50*-1)

if b>0:
	point.setheading(-20)
	point.fd(b*50)
elif b<0:
	point.setheading(160)
	point.fd(b*50*-1)
if c>0:
	point.setheading(90)
	point.fd(c*50)
elif c<0:
	point.setheading(-90)
	point.fd(c*50*-1)



turtle.done()