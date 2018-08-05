import turtle
turtle.speed(0)
num_pts = 5000#number sides to your drawing!
for i in range(num_pts):
   turtle.left(360/num_pts)
   turtle.forward(1)
   
turtle.mainloop()
