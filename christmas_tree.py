# source https://gist.github.com/jurandysoares/4380835

import turtle

def christmastree():
    # Setup drawing screen
    screen = turtle.Screen()
    screen.setup(900,870)

    # Create circle object
    circle = turtle.Turtle()
    circle.shape('circle')
    circle.color('red')
    circle.speed('fastest')
    circle.up()

    # Create square object
    square = turtle.Turtle()
    square.shape('square')
    square.color('green')
    square.speed('fastest')
    square.up()

    # Start at the top and draw first red circle
    circle.goto(0,280)
    circle.stamp()

    k = 0
    # Iterate to create rows 1 - 16
    for i in range(1, 17):
        # Every iteration, go 30 pixels down
        y = 30*i
        
        # Draw green squares, width is iteration minus k-variable
        for j in range(i-k):
            x = 30*j
            square.goto(x,-y+280)
            square.stamp()
            square.goto(-x,-y+280)
            square.stamp()

        # Draw red circles once every 4 rows, starting at 0
        if i % 4 == 0:
            x =  30*(j+1)
            circle.color('red')
            circle.goto(-x,-y+280)
            circle.stamp()
            circle.goto(x,-y+280)
            circle.stamp()        
            # After every row with a red circle, decrease tree width with two
            k += 2

        # Draw yellow circles once every 4 rows, starting at 3
        if i % 4 == 3:
            x =  30*(j+1)
            circle.color('yellow')
            circle.goto(-x,-y+280)
            circle.stamp()
            circle.goto(x,-y+280)
            circle.stamp() 
    
    # Create trunk in rows 17 - 19
    square.color('brown')
    for i in range(17,20):
        y = 30*i
        for j in range(3):    
            x = 30*j
            square.goto(x,-y+280)
            square.stamp()
            square.goto(-x,-y+280)
            square.stamp()