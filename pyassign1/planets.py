import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")

Sun = turtle.Turtle()
Sun.pensize(50)
Sun.color("yellow")
Sun.goto(0,0)
Sun.stamp()

Plants = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn"]
Colors = ["white","orange","lightblue","purple","pink","lightgreen"]
PlantsRadius = [1,1,2,2,3,3]
Radius_a = [2,4.5,8,10,13,20]
Radius_b = [3,4,7,12,15,19]
Speed = [7,5.5,4,3,1.5,1]


for x in range(6):
    Plants[x] = turtle.Turtle()
    Plants[x].color(Colors[x])
    Plants[x].shape("circle")
    Plants[x].speed(0)
    Plants[x].shapesize(PlantsRadius[x])
    Plants[x].penup()
    Plants[x].goto(Radius_a[x] * 15,0)
    Plants[x].pendown()
for i in range(3600):
    for x in range(6):
        Plants[x].goto(15 * Radius_a[x] * math.cos(Speed[x] * i / (360)), 15 * Radius_b[x] * math.sin(Speed[x] * i / (360)))
