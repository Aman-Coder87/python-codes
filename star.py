import turtle

# windows setup
wn =turtle.Screen()
wn.title('Spyder')
wn.bgcolor('black')
wn.setup( width = 800 , height = 600)

# Heart ,,
heart = turtle.Turtle()
heart.speed(0)
heart.shape('circle')
heart.color('red')
heart.penup()
heart.goto(-350 , 0)


# angel,star_animation
angel = turtle.Turtle()
angel.getscreen().bgcolor( 'black')

angel.color('yellow', 'yellow')
angel.speed(100)

def star(turtle, size):
	if size <= 10 :
		return
	else :
		turtle.begin_fill()
		for i in range(5) :
			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)
		turtle.end_fill()


star(angel, 300)






turtle.done()