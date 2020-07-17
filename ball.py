import turtle
from time import sleep

# setup Windows
wn = turtle.Screen()
wn.title('Spyder')
wn.bgcolor( 'black')
wn.setup(width = 500 , height = 500)




# base ground
base = turtle.Turtle()
base.color('white')
base.shape('square')
base.speed(0)
base.shapesize(stretch_wid = 0.5 , stretch_len = 60)
base.penup()
base.goto(0 , -290 )

# Ball. 
ball = turtle.Turtle()
ball.color('yellow')
ball.shape('circle')
ball.speed(5)
ball.shapesize(stretch_wid = 2 , stretch_len = 2)
ball.penup()
ball.goto( 0 , -265 )

#Bot_1
bot_1 = turtle.Turtle()
bot_1.color('red')
bot_1.shape('square')
bot_1.speed(5)
bot_1.shapesize(stretch_wid = 5 , stretch_len=2)
bot_1.penup()
bot_1.goto(-465 , -240)

#	bot_2
bot_2 = turtle.Turtle()
bot_2.color('blue')
bot_2.shape('square')
bot_2.speed(5)
bot_2.shapesize(stretch_wid = 5 , stretch_len = 2)
bot_2.penup()
bot_2.goto(+465 , -240)

#illusion star
rs = turtle.Turtle()
rs.color('green', 'yellow')
rs.speed(0)
rs.penup()
rs.goto(-300 , +200)


def round(turtle , size) :
	if size <= 10 :
		return
	else :
		rs.begin_fill()
		for i in range(20) :
			turtle.forward(size)
			round(turtle , size/3)
			turtle.left(210)
	
			
		rs.end_fill()
			
		


# running bot
#def run(bot , size) :
#	for i in range(1) :
#		bot.forward(size)
#		bot.backward(size)


#def run_b(bot , size ) :
#	for i in range(1) :
#		bot.backward(200)
#		bot.forward(200)

#def run_1(ball , size ) :
#	for i in range(1) :
#		ball.forward(size)
#		ball.backward(size)
#		ball.backward(size)
#		ball.forward(size)



#mess
m = turtle.Turtle()

def mass(m) :
	for i in range (100) :
		ball.forward(400)
		bot_2.backward(50) , ball.backward(400)
		
		bot_2.forward(50)
		ball.backward(400)
		bot_1.forward(50) , ball.forward(400)
		bot_1.backward(50)


	
	
	# move ball
#	ball.setx(ball.xcor() )
#	bot_1.setx(ball.xcor())
#	bot_2.setx(ball.xcor())
#	
#	if ball.xcor() > -425 :
#		run_1(ball , 425)
#		
#	if ball.xcor() > 425 :
#		run(bot_1 , 100)
#		

# star
star = turtle.Turtle()
star.color('yellow', 'yellow')
star.speed(0)
star.penup()
star.goto(+50 , +100)
star.penup()

def run_a(turtle , size) :
	if size <= 10 :
		return
	else :
		star.begin_fill()
		for i in range(5) :
			turtle.forward(size)
			run_a(turtle ,size/2.5)
			turtle.left(216)
			
		star.end_fill()


sleep(1)
round(rs , 100)
sleep(1)			
run_a(star , 200) 
sleep(1)
mass(m)


wn.update()
turtle.done()