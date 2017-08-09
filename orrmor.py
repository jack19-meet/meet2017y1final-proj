import turtle
import random

unitsize = 20
turtle.tracer(1,0)
turtle.penup()
turtle.hideturtle()

#the size of the screen
WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 600
turtle.setup(WINDOW_SIZE_X , WINDOW_SIZE_Y)

foodpos_list = []

#the edges of the screen

UP_EDGE = WINDOW_SIZE_Y/2
DOWN_EDGE = -(WINDOW_SIZE_Y/2) 
RIGHT_EDGE = WINDOW_SIZE_X/2
LEFT_EDGE = -(WINDOW_SIZE_X/2)

#making the catcher
n=0
m=0
catcher = turtle.clone()
##turtle.register_shape('boat.gif')
##catcher.shape("boat.gif")
catcher.shape("square")


turtle_score=turtle.clone()
turtle_score.hideturtle()
turtle_score.goto(-WINDOW_SIZE_X/2+10,-WINDOW_SIZE_Y/2+40)
turtle_score.write('score:'+str(n),font=("Arial",30,("bold","italic")))
turtle_drops = turtle.clone()
turtle_drops.hideturtle()
turtle_drops.goto(-WINDOW_SIZE_X/2+10,-WINDOW_SIZE_Y/2+10)
turtle_drops.write('drops: '+str(m), font=('Arial',30,('bold','italic')))


SQUARE_SIZE = 20
catcher.goto(-(WINDOW_SIZE_X/2)+150,-(WINDOW_SIZE_Y/2)+90)
catcher.showturtle()

##for i in range (START_LENGTH):
##    x_pos=catcher.pos()[0]
##    y_pos=catcher.pos()[1]
##
##    x_pos=x_pos+SQUARE_SIZE
##
##    my_pos= (x_pos, y_pos)
##    catcher.goto(x_pos, y_pos)
##
##    pos_list.append(my_pos)
##    new_stamp = catcher.stamp()
##    stamp_list.append(new_stamp)


RIGHT_ARROW = 'Right'
LEFT_ARROW = 'Left'
TIME_STEP = 100

RIGHT=0
LEFT=1

def right():
    global direction
    direction= RIGHT
    move_catcher()
    print('you moved right!')
    

def left():
    global direction

    direction = LEFT
    move_catcher()
    print('you moved left!')

turtle.onkeypress(right , RIGHT_ARROW)
turtle.onkeypress(left , LEFT_ARROW)
turtle.listen()
##
def move_catcher():
    global direction
    my_pos = catcher.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        catcher.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    
    elif direction==LEFT:
        catcher.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

##    my_pos=catcher.pos()
##    pos_list.append(my_pos)
##    new_stamp = catcher.stamp()
##    stamp_list.append(new_stamp)
##
##    old_stamp = stamp_list.pop(0)
##    catcher.clearstamp(old_stamp)
##    pos_list.pop(0)
##

food_list = []
step = 25
bottom = -WINDOW_SIZE_Y/2 + 100
turtle.register_shape('food-chicken.gif')
def create_food():
    y_pos = WINDOW_SIZE_Y/2 - 50
    min_x = -int(WINDOW_SIZE_X/2/unitsize)+1
    max_x = int(WINDOW_SIZE_X/2/unitsize)-1
    x_pos = random.randint(min_x,max_x)*unitsize
    food = turtle.clone()
    food.shape('food-chicken.gif')
    food.goto(x_pos,y_pos)
    food.showturtle()
    food_list.append(food)
food_delay = 0
delay_num = 7
def falling_food():
    global food_delay, m, n
    food_destroy = []
    eaten_food = []
    for food in food_list:
        x_pos = food.pos()[0]
        y_pos = food.pos()[1]
        if y_pos >= bottom:
            y_pos = y_pos - step
            food.goto(x_pos,y_pos)
            boat_x = catcher.pos()[0]
            boat_y = catcher.pos()[1]
            if (x_pos >=  boat_x - 50 ) and (x_pos <=  boat_x + 50 ) and (y_pos >=  boat_y - 50 ) and (y_pos <=  boat_y + 50 ):
                ind = food_list.index(food)
                eaten_food.append(ind)
        else:
            ind = food_list.index(food)
            food_destroy.append(ind)

    for ind in food_destroy:
        old_food = food_list.pop(ind)
        old_food.hideturtle()
        del old_food
        m=m+1
        turtle_drops.clear()
        turtle_drops.write('drops: '+str(m), font=('Arial',30,('bold','italic')))

    for ind in eaten_food:
        old_food = food_list.pop(ind)
        old_food.hideturtle()
        del old_food
        n=n+1
        turtle_score.clear()
        turtle_score.write("score:"+str(n),font=("Arial",30,("bold","italic")) )

    if food_delay <= delay_num:
        food_delay += 1
    else:
        food_delay = 0
        create_food()

    if m == 5:
        print('game over!')
        print ('you droped 5!')
        quit()
        
    turtle.ontimer(falling_food,100)

falling_food()


