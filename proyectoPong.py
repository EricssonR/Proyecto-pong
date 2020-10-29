import turtle
import winsound


#ventana
wn =  turtle.Screen()
wn.title("pong by Ericsson Reyes")
wn.bgcolor("black")
wn.setup(width =800, height=600)
wn.tracer(0)
turtle.bgpic("fondo6.png" )

MarcadorA=0
MarcadorB=0

#JugadorA
JugadorA = turtle.Turtle()
JugadorA.speed(0)
JugadorA.shape("square")
JugadorA.color("Blue")
JugadorA.penup()
JugadorA.goto(-360,0)
JugadorA.shapesize(stretch_wid=5, stretch_len=1)


#JugadorB
JugadorB = turtle.Turtle()
JugadorB.speed(0)
JugadorB.shape("square")
JugadorB.color("yellow")
JugadorB.penup()
JugadorB.goto(350,0)
JugadorB.shapesize(stretch_wid=5, stretch_len=1)

#Pelota
Pelota = turtle.Turtle()
Pelota.speed(0)
Pelota.shape("circle")
Pelota.color("red")
Pelota.penup()
Pelota.goto(0,0)
Pelota.dx = 1.5
Pelota.dy = 1.5

#Marcador
Marcador = turtle.Turtle ()
Marcador.speed(0)
Marcador.color("White")
Marcador.penup()
Marcador.hideturtle()
Marcador.goto(0,240)
Marcador.write("Jugador A: 0     Jugador B: 0", align="Center", font=("Courier",24,"normal"))

mensaje_marcador = turtle.Turtle()
mensaje_marcador.speed(0)
mensaje_marcador.color("white")
mensaje_marcador.penup()
mensaje_marcador.hideturtle()
mensaje_marcador.goto(0,-260)
mensaje_marcador.write("Gana quien obtenga los primeros 15 puntos", align="center",font=("Courier", 16,"normal") )

#Linea Division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#funcion
def JugadorA_up():
    y = JugadorA.ycor()
    y += 20
    JugadorA.sety(y)

def JugadorA_down():
    y = JugadorA.ycor()
    y -= 20
    JugadorA.sety(y)

def JugadorB_up():
    y = JugadorB.ycor()
    y += 20
    JugadorB.sety(y)

def JugadorB_down():
    y = JugadorB.ycor()
    y -= 20
    JugadorB.sety(y)

def winner_message():
    mensaje=turtle.Turtle()
    mensaje.speed(0)
    mensaje.color("white")
    mensaje.penup()
    mensaje.hideturtle()
    mensaje.goto(0,-220)
    mensaje.write("WE HAVE A WINNER \n CONGRATULATION!", align="center", font=("Courier", 24,"bold"))

#Teclado
wn.listen()
wn.onkeypress(JugadorA_up, "W")
wn.onkeypress(JugadorA_up, "w")
wn.onkeypress(JugadorA_down, "S ")
wn.onkeypress(JugadorA_down, "s ")
wn.onkeypress(JugadorB_up, "Up")
wn.onkeypress(JugadorB_down, "Down")

while True:
    wn.update()

    Pelota.setx(Pelota.xcor() + Pelota.dx)
    Pelota.sety(Pelota.ycor() + Pelota.dy)

    #Bordes
    if Pelota.ycor() > 290:
        Pelota.dy *= -1
    if Pelota.ycor()<-290:
        Pelota.dy *= -1
       

    #Bordes derecha/izquierda
    if Pelota.xcor()> 350:
        Pelota.goto(0,0)
        Pelota.dx *= -1
        MarcadorA += 1
        winsound.PlaySound("over.wav", winsound.SND_ASYNC)
        Marcador.clear()
        Marcador.write("Jugador A: {}  Jugador B: {}".format (MarcadorA, MarcadorB),
        align="Center", font=("courier" ,24, "normal"))


    if Pelota.xcor()<- 350:
        Pelota.goto(0,0)
        Pelota.dx *= -1
        MarcadorB += 1
        winsound.PlaySound("over.wav", winsound.SND_ASYNC)
        Marcador.clear()
        Marcador.write("Jugador A: {}  Jugador B: {}".format (MarcadorA, MarcadorB),
        align="Center", font=("courier" ,24, "normal"))

        

    if ((Pelota.xcor() >340 and Pelota.xcor() <350)
        and(Pelota.ycor() < JugadorB.ycor() + 50 
        and Pelota.ycor()> JugadorB.ycor() -50)):
        Pelota.dx *= -1
       
        
        

    
    if ((Pelota.xcor() <-340 and Pelota.xcor() > -350)
        and(Pelota.ycor() < JugadorA.ycor() +50 
        and Pelota.ycor()> JugadorA.ycor() -50)):
        Pelota.dx *= -1
        
        
    if MarcadorA == 15 or MarcadorB == 15:
        winner_message()
        break

exit()
turtle.getscreen()._root.mainloop()
