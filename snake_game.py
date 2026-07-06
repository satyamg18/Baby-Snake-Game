"""
Baby Snake Game
Built during Stanford Code in Place - CS106A Final Project
Author: Satyam Gupta

Controls: Arrow Keys
Goal: Eat the red goal, avoid walls.
"""

from graphics import Canvas
import time
import random

DELAY = 0.01
VELOCITY = 2

def main():
    Canvas_width = 400
    Canvas_height = 400
    Snake_size = 20
    Goal_size = 20

    canvas = Canvas(Canvas_width, Canvas_height)
    
    # Initial position of the snake
    x1 = 0
    y1 = 0
    
    # Random initial position of the goal
    x2, y2 = random_position(Canvas_width, Canvas_height, Goal_size)

    Snake = canvas.create_rectangle(x1, y1, x1 + Snake_size, y1 + Snake_size, "Brown")
    Goal = canvas.create_rectangle(x2, y2, x2 + Goal_size, y2 + Goal_size, "Red")

    while True:
        key = canvas.get_last_key_press()
        
        if key == 'ArrowLeft':
            if x1 > 0:
                x1 -= VELOCITY
        if key == 'ArrowRight':
            if x1 < Canvas_width - Snake_size:
                x1 += VELOCITY
        if key == 'ArrowUp':
            if y1 > 0:
                y1 -= VELOCITY
        if key == 'ArrowDown':
            if y1 < Canvas_height - Snake_size:
                y1 += VELOCITY            

        canvas.moveto(Snake, x1, y1)

        # Check if snake reaches the goal
        if (x1 < x2 + Goal_size and x1 + Snake_size > x2 and
            y1 < y2 + Goal_size and y1 + Snake_size > y2):
            x2, y2 = random_position(Canvas_width, Canvas_height, Goal_size)
            canvas.moveto(Goal, x2, y2)
        
        time.sleep(DELAY)

def random_position(canvas_width, canvas_height, size):
    x = random.randint(0, canvas_width - size)
    y = random.randint(0, canvas_height - size)
    return x, y

if __name__ == '__main__':
    main()
