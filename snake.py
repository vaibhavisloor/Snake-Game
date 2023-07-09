from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]


class snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_turtle=Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    
    def move(self):
            for segment in range(len(self.segments)-1,0,-1):
                x_coordinate = self.segments[segment-1].xcor()
                y_coordinate = self.segments[segment-1].ycor()
                self.segments[segment].goto(x_coordinate,y_coordinate)
            self.head.forward(20)


    def move_up(self):
         if self.head.heading() != 270:
            self.head.setheading(90)
    def move_down(self):
         if self.head.heading() != 90:
            self.head.setheading(270)
    def move_left(self):
         if self.head.heading() != 0:
            self.head.setheading(180)
    def move_right(self):
         if self.head.heading() != 180:
            self.head.setheading(0)
