import turtle
turtle.color("Blue")
x1 = -150
y1 = -150
turtle.pensize(1)
turtle.color('gray')
turtle.fillcolor('gray')
turtle.begin_fill()
turtle.penup()
turtle.goto(x= x1 , y = y1)
turtle.pendown()
turtle.speed(0)
turtle.shape("turtle")
turtle.pensize(3)
b = 0        
a = 0
coory = [150,50,-50]
coorx = [-150,-50,50]
coor_all = [[-150,150],[-50,150],[50,150],[-150,50],[-50,50],[50,50],[-150,-50],[-50,-50],[50,-50]]
list_zanyato = [0,0,0,0,0,0,0,0,0]
turn = 1
list_of_victories = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
game_over = False
def square() -> None:
    i = 0
    while i < 4:
        turtle.forward(100)
        turtle.left(90)
        i += 1
                        
screen = turtle.Screen()            
def krestik(x : float, y : float) -> None:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+100,y-100)
    turtle.penup()
    turtle.goto(x+100,y)
    turtle.pendown()
    turtle.goto(x,y-100)
    
def circle1(x : float,y : float)-> None    : 
    
    
    turtle.penup()
    turtle.goto(x+50,y - 100)
    turtle.pendown()    
    turtle.circle(49)
# цикл чтоб нарисовать поле    
while b < 3:
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    y1 += 100
    b += 1
    a = 0
    while a < 3 :
        square()
        turtle.forward(100)
        a +=1
# функция для ничьи 
def draw_line(start_index,end_index)   :
    
    
    turtle.color("Red")
    if end_index - start_index == 2:
        start_x = coor_all[start_index][0]
        start_y = coor_all[start_index][1] - 50
        end_x = coor_all[end_index][0] + 100
        end_y = coor_all[end_index][1] - 50
    elif end_index - start_index == 6:
        start_x = coor_all[start_index][0] +50
        start_y = coor_all[start_index][1] 
        end_x = coor_all[end_index][0] + 50
        end_y = coor_all[end_index][1] - 100
    elif end_index - start_index == 8:
        start_x = coor_all[start_index][0]
        start_y = coor_all[start_index][1] 
        end_x = coor_all[end_index][0] + 100
        end_y = coor_all[end_index][1] - 100
    elif end_index - start_index == 4:
        start_x = coor_all[start_index][0] + 100
        start_y = coor_all[start_index][1] 
        end_x = coor_all[end_index][0] 
        end_y = coor_all[end_index][1] - 100  
    turtle.pensize(5) 
    turtle.penup()
    turtle.goto(start_x,start_y)
    turtle.pendown()
    
    turtle.goto(end_x,end_y)   
def check_draw()    :
    global game_over
    draw = True
    for status in list_zanyato:
        if status == 0:
            draw = False 
    if draw == True:
        turtle.penup()
        turtle.goto(0,250)
        turtle.pendown()
        turtle.color("Yellow")
        turtle.hideturtle()
        turtle.write(arg = "Нічия",align = "center",font = ["Arial",30,"normal"])
        game_over = True
# функция для победы
def check_victory():
    global game_over
    global victory
    
    for victory in list_of_victories:
        if list_zanyato[victory[0]] == list_zanyato[victory[1]] == list_zanyato[victory[2]]:
            if list_zanyato[victory[0]] != 0:
            
                game_over = True
                draw_line(start_index = victory[0],end_index= victory[2])
                turtle.penup()
                turtle.goto(0,250)
                turtle.pendown()
                turtle.color("Green")
                turtle.hideturtle()
                turtle.write(arg = f"Переміг гравець №{turn}",align = "center",font = ["Arial",30,"normal"])
    if game_over == False:
        check_draw()    


def game(x: float ,y : float):
    global turn
    if game_over == False:
        count = 0
        for coory1 in coory :
            if coory1 > y > coory1 - 100 :
                for coorx1 in coorx :
                    if coorx1 < x < coorx1 + 100:
                        for elements in coor_all:
                            if elements[0] ==coorx1:
                                if elements[1] == coory1:
                                    if list_zanyato[count] == 0:
                                        if turn == 1:
                                            krestik(x = coorx1, y = coory1)
                                            list_zanyato[count] = 1
                                            check_victory()
                                            turn = 2
                                        elif turn == 2:
                                            circle1(x = coorx1, y = coory1)
                                            list_zanyato[count] = 2
                                            check_victory()
                                            turn = 1
                            
                            count +=1 
                                          
screen.onscreenclick(fun = game)         

screen.mainloop()




    
