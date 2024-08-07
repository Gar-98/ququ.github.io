from turtle import*


t1 = Turtle()


t1.color('green')
t1.shape('turtle')
t1.speed(1)


def tiknuli(x,y): #как реагировать
    t1.color('red')
    t1.forward(5)
    t1.color('green')


t1.onclick(tiknuli) #на что реагировать


while True:
    t1.circle(50)