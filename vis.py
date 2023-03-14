import sys
import shutil
import os
import time
import turtle
import random
from datetime import datetime
import imageio.v2 as iio

# set up turtle window
window = turtle.Screen()
window.title("PI Day 2023")
window.screensize(1000,1000)

# create turtle to make pi estimate 
monte = turtle.Turtle()

# create and setup turtle for writing text
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, 150)

# create directory to store images imageio will use to make the video
try:
    os.mkdir('data')
except FileExistsError:
    pass

def draw_circle():
    # function to draw circle

    monte.penup()
    monte.goto(0, -100)
    monte.pendown()
    monte.circle(100)

def draw_bounding_square():
    # function to draw square

    monte.penup()
    monte.goto(-100, -100)
    monte.pendown()
    for _ in range(4):
        monte.forward(200)
        monte.left(90)

def save_image(writer):
    # Save the current frame as an image
    
    date = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = './data/posta-' + date
    monte.getscreen().getcanvas().postscript(file= fileName+'.eps')
    writer.append_data(iio.imread(fileName + '.eps'))

def save_animation(num_samples):
    # create writer to make animations
    writer = iio.get_writer("monte_carlo_pi.mp4", format='FFMPEG', mode = "I", fps=10)

    # variable that stores number of samples in circle
    num_points_in_circle = 0
    
    monte.speed(0)
    draw_bounding_square()
    draw_circle()

    for i in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        monte.penup()
        monte.goto(x*100, y*100)
        monte.pendown()

        if x**2 + y**2 <= 1:
            monte.dot(3, "green")
            num_points_in_circle += 1
        else:
            monte.dot(3, "red")

        pi_estimate = 4 * num_points_in_circle / (i + 1)
        text.clear()
        text.write("Pi Estimate: {:.6f}\nSamples: {}\nPoints in Circle: {}".format(pi_estimate, i+1, num_points_in_circle),
                align="center", font=("Arial", 16, "bold"))

        # Save the current frame as an image
        save_image(writer)


    pi_estimate = 4 * num_points_in_circle / num_samples
    print("Number of points in the circle:", num_points_in_circle)
    print("Number of samples:", num_samples)
    print("Estimated value of pi:", pi_estimate)
    
    # close writer
    writer.close()
    # delete folder that stores images
    shutil.rmtree('data')


if __name__ == "__main__":
    num_samples = int(sys.argv[1])
    save_animation(num_samples)
