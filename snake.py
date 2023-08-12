from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.out_of_screen_segments = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, pos):
        if self.out_of_screen_segments:  # garbage collection
            segment = self.out_of_screen_segments[-1]
            self.out_of_screen_segments.remove(segment)
        else:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
        segment.goto(pos[0], pos[1])
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

    def reset(self):
        for i in range(3):
            segment = self.segments[i]
            segment.goto(STARTING_POSITIONS[i])
        if len(self.segments) > 3:  # send to garbage
            removed_segments = []
            for segment in self.segments[3:]:
                segment.goto(2000, 2000)
                removed_segments.append(segment)
                self.out_of_screen_segments.append(segment)
            for segment in removed_segments:
                self.segments.remove(segment)
        self.head.setheading(0)
