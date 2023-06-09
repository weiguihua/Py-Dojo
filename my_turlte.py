import turtle as tu

def cube(my_turtle, x, y, w, h, hand):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.setheading(0)

    my_turtle.down()

    if hand == 'right':
        my_turtle.forward(w)
        my_turtle.left(90)

        my_turtle.forward(h)
        my_turtle.left(90)

        my_turtle.forward(w)
        my_turtle.left(90)

        my_turtle.forward(h)
        my_turtle.left(90)
    elif hand == 'left':
        my_turtle.forward(w)
        my_turtle.right(90)

        my_turtle.forward(h)
        my_turtle.right(90)

        my_turtle.forward(w)
        my_turtle.right(90)

        my_turtle.forward(h)
        my_turtle.right(90)
    else:
        print(f'手性错误: {hand}')

    my_turtle.up()


tu.setup(900, 600)

t = tu.Turtle()   # 创建海龟对象
t.speed(10)   # 将速度设为1，即降慢海龟的速度

cube(t, 10, 10, 300, 180, 'right')
cube(t, -300-10, 10, 300, 180, 'right')
cube(t, 10, -200-10, 300, 180, 'right')
cube(t, -300-10, -200-10, 300, 180, 'right')

for i in range(5):
    cube(t, i*10, i*10, 300, 180, 'right')

tu.done()
tu.mainloop()   # 保证窗口持续显示直到关闭
