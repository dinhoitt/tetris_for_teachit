"""
Life is what you make of it 

Written by Dinho_itt (this is my instagram id)
"""


import turtle as t
import random as r
import copy as cp



g_score = 0

Blks_shape_info= {
    "LL" :
        { 0 :((-1,1), (-1, 0), (-1, -1), (0, -1)),
          90 :((-1, 1), (0, 1), (1, 1), (-1, 0)),
          180 :((0, 1), (1, 1), (1, 0), (1, -1)),
          270 :((1, 0), (-1, -1), (0, -1), (1, -1))
          },

    "LR" :
        { 0 :((1, 1), (1, 0), (0, -1), (1, -1)),
          90 :((-1, 0), (-1, -1), (0, -1), (1, -1)),
          180 :((-1, 1), (0, 1), (-1, 0), (-1, -1)),
          270 :((-1, 1), (0, 1), (1, 1), (1, 0))
          },

    "SL" :
        { 0 :((0, 1), (1, 1), (-1, 0), (0, 0)),
          90 :((0, 1), (0, 0), (1, 0), (1, -1)),
          180 :((0, 1), (1, 1), (-1, 0), (0, 0)),
          270 :((0, 1), (0, 0), (1, 0), (1, -1))
          },

    "SR":
        {0: ((-1, 1), (0, 1), (0, 0), (1, 0)),
         90: ((1, 1), (1, 0), (0, 0), (0, -1)),
         180: ((-1, 1), (0, 1), (0, 0), (1, 0)),
         270: ((1, 1), (1, 0), (0, 0), (0, -1))
         },

    "T":
        {0: ((0, 1), (-1, 0), (0, 0), (1, 0)),
         90: ((0, 1), (0, 0), (1, 0), (0, -1)),
         180: ((-1, 0), (0, 0), (1, 0), (0, -1)),
         270: ((0, 1), (0, 0), (-1, 0), (0, -1))
         },

    "Q":
        {0: ((-1, 1), (0, 1), (-1, 0), (0, 0)),
         90: ((-1, 1), (0, 1), (-1, 0), (0, 0)),
         180: ((-1, 1), (0, 1), (-1, 0), (0, 0)),
         270: ((-1, 1), (0, 1), (-1, 0), (0, 0))
         },

    "I":
        {0: ((0, 1), (0, 0), (0, -1), (0, -2)),
         90: ((-1, 0), (0, 0), (1, 0), (2, 0)),
         180: ((0, 1), (0, 0), (0, -1), (0, -2)),
         270: ((-1, 0), (0, 0), (1, 0), (2, 0))

         }
}

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x , self.y + other.y)


class Block:
    def __init__(self, block_type):
        self.block_type = block_type
        self.angles = list(Blks_shape_info[block_type].keys())
        self.angle_idx = 0
        self.points = [Point(*p) for p in Blks_shape_info[block_type][self.angles[self.angle_idx]]]
        self.center_point = Point()

    def rotate(self):
        self.angle_idx = (self.angle_idx + 1) % len(self.angles)
        self.points = [Point(*p) for p in Blks_shape_info[self.block_type][self.angles[self.angle_idx]]]

    def move(self, dx, dy):
        self.center_point.x += dx
        self.center_point.y += dy
        # for p in self.points:
        #     p.x += dx
        #     p.y += dy
        #     print('move', p.x , p.y)

    def draw_unit_blk(self, pt):
        t.goto(pt.x, pt.y)
        t.stamp()

    def draw(self, what):
        if what == 'float':
            t.fillcolor(ttrs.fillcolor_float)
            t.pencolor(ttrs.pencolor_float)
        elif what == 'fixed':
            t.fillcolor(ttrs.fillcolor_fixed)
            t.pencolor(ttrs.pencolor_fixed)
        elif what == 'erase':
            t.color(ttrs.bgcolor)

        cp = ttrs.current_block.center_point

        for p in self.points:
            self.draw_unit_blk(Point((p.x+cp.x) * 22 - 132 , (p.y+cp.y) * 22 - 294))

        del cp




class Tetris:
    def __init__(self):
        self.border_color = 'black'
        self.bgcolor = 'light yellow'
        self.fillcolor_float = 'yellow'
        self.fillcolor_fixed = 'green'
        self.pencolor_float = 'red'
        self.pencolor_fixed = 'black'
        self.blocks = ['LL', 'LR', 'SL', 'SR', 'T', 'Q', 'I']
        self.game_board = [[0] * 12 for _ in range(22)]  #''' 아래의 [주석 1번]'''
        self.current_block = None

    '''
    [주석 1번]
    self.game_board = [[0] * 12 for _ in range(22)]는 22개의 0으로 이루어진 1차원 리스트를
    12번 반복하여 2차원 리스트를 생성하는 구문입니다. 이 구문은 리스트 컴프리헨션을 사용하여 간결하게
    표현한 것으로, 내부적으로는 22개의 독립된 1차원 리스트가 생성되어 각 행마다 별도의 참조가 이루어
    집니다. 따라서, self.game_board.append() 메서드를 사용하지 않고도 2차원 리스트를 초기화하고 
    사용할 수 있습니다. 이후에는 각 행에 대해 별도의 참조가 이루어졌으므로, 각 행을 독립적으로 변경
    하거나 접근할 수 있습니다.
    '''


    def draw_borderline(self):
        t.up()
        t.pencolor(ttrs.border_color)
        t.goto(-146, 300)
        t.down()
        t.goto(-146, -306)
        t.goto(124, -306)
        t.goto(124, 300)
        t.up()


    def init_turtle(self):
        t.bgcolor(ttrs.bgcolor)
        t.ht()
        t.up()

    def new_block(self):
        del self.current_block
        self.current_block = Block(r.choice(ttrs.blocks))
        self.current_block.fillcolor = 'yellow'
        self.current_block.pencolor = 'red'
        self.current_block.center_point = Point(5, 20)


    def init_game(self):
        global g_score
        g_score = 0


        for y in range(22):
            for x in range(12):
                self.game_board[y][x] = 0

        t.clear()

        self.new_block()
        self.draw_borderline()

        write_informations('score :\n' + repr(g_score), 'black')

        bt_prcss= button_process(ttrs)
        bt_prcss.draw_button('clicked')
        del bt_prcss

        event_init()

    def run(self):
        self.init_turtle()
        self.init_game()
        self.current_block.draw('float')


        t.mainloop()



    def is_collision(self, block, dx, dy):
        for p in block.points:
            x = p.x + dx
            y = p.y + dy
            # print(x,y,'gb : ',self.game_board[y][x])
            if x < 0 or x >= 12 or y < 0 or y >= 22 or self.game_board[y][x] == 1:
                # print('game_board[y][x]', self.game_board[y][x])
                del x, y
                return True
        del x, y
        return False

    def add_to_board(self, block):
        for p in block.points:
            self.game_board[p.y + block.center_point.y][p.x + block.center_point.x] = 1


    def check_board(self):
        global g_score

        Ln_for_rm = []
        Pull_num = []
        y_len = 21
        for y in range(y_len):
            sum = 0
            for x in range(12):
                sum += self.game_board[y][x]

            if sum == 12 :
                Ln_for_rm.append(y)
                t.color(ttrs.bgcolor)
                for xx in range(12):
                    self.game_board[y][xx] = 0
                    self.current_block.draw_unit_blk(Point(xx * 22 - 132, y * 22 - 294))


        if  len(Ln_for_rm):
            g_score += (100 * len(Ln_for_rm))
            Ln_for_rm.append(y_len-1)
            Pull_num.append(1)
            i=0
            while Pull_num[i] < len(Ln_for_rm):
                while Ln_for_rm[i+1] == Ln_for_rm[i]+1:
                    del Ln_for_rm[i+1]
                    Pull_num[i] += 1

                Pull_num.append(1+Pull_num[i])
                i+=1

            if Pull_num[i] < len(Ln_for_rm)+1 :
                Pull_num.append(0)
            else :
                Pull_num[i] = 0


            i=0
            for i in range(len(Ln_for_rm)-1):
                for y in range(Ln_for_rm[i]-Pull_num[i-1], Ln_for_rm[i+1]-Pull_num[i]):
                    for x in range(12):
                        ttrs.game_board[y][x] = ttrs.game_board[y+Pull_num[i]][x]

            t.clear()
            ttrs.draw_borderline()

            t.fillcolor(ttrs.fillcolor_fixed)
            t.pencolor(ttrs.pencolor_fixed)
            for x in range(12):
                for y in range(22):
                    if ttrs.game_board[y][x]:
                        self.current_block.draw_unit_blk(Point(x * 22 - 132, y * 22 - 294))

            write_informations('score :\n' + repr(g_score), 'black')



    def move_sequence(self, x, y, what):
        self.current_block.draw('erase')
        self.current_block.move(x, y)
        self.current_block.draw(what)



    def calc_ydistance(self):
        ydistance = 50
        for p in self.current_block.points:
            temp_pt =Point(p.x, p.y) + self.current_block.center_point
            # print("ydis pt:", temp_pt.x, temp_pt.y)
            i=0
            temp_ydistance = 0

            for y in range(temp_pt.y-1, -1, -1):
                if  self.game_board[y][temp_pt.x] :
                    # print("ydst if")
                    temp_ydistance = i
                else :
                    # print("ydst else")
                    i+=1

            if temp_ydistance < i :
                temp_ydistance = i

            if temp_ydistance < ydistance :
                ydistance = temp_ydistance

        del temp_ydistance, temp_pt, i

        return ydistance

    def block_piling(self):
        self.add_to_board(self.current_block)
        self.check_board()
        # for y in range(21, -1, -1):
        #     for x in range(12):
        #         print(self.game_board[y][x], end= ' ')
        #     print("",end = '\n')
        self.new_block()
        if self.is_collision(self.current_block, self.current_block.center_point.x, self.current_block.center_point.y) :
            self.game_over()
        else :
            self.current_block.draw('float')


    def game_over(self):
        set_bit(g_game_over)
        event_disable()






def set_bit(bit_num):
    global g_key_flag
    g_key_flag |= 1<<bit_num

def clear_bit(bit_num):
    global g_key_flag
    g_key_flag &= ~(1<<bit_num)

def get_bit(bit_num):
    global g_key_flag
    if g_key_flag & (1<<bit_num) :
        return True
    else:
        return False

def event_init():
    t.onkeypress(fun_onkey_up, 'space')
    t.onkeypress(fun_onkey_down, 'Down')
    t.onkeypress(fun_onkey_left, 'Left')
    t.onkeypress(fun_onkey_right, 'Right')
    t.onkeypress(fun_onkey_space, 'up')

    if get_bit(g_game_over):
        t.ontimer(fun_otmr,1000)
        clear_bit(g_game_over)

    t.listen()

    t.onscreenclick(fun_osclk)

def event_disable():
    t.onkeypress(None, 'spce')
    t.onkeypress(None, 'Down')
    t.onkeypress(None, 'Left')
    t.onkeypress(None, 'Right')
    t.onkeypress(None, 'Up')



def fun_button_released():
    bt_prcss = button_process(ttrs)
    bt_prcss.draw_button('released')
    ttrs.init_game()
    del bt_prcss

def fun_osclk(x, y):
    if (x < -253) and (x > -323) and (y < 99) and (y > 68) :
       if get_bit(g_game_over):
           bt_prcss = button_process(ttrs)
           bt_prcss.draw_button('clicked')
           # t.ontimer(fun_button_released, bt_prcss.release_time)
           del bt_prcss
           ttrs.init_game()





def fun_otmr():

    if get_bit(g_game_over) :
        bt_prcss = button_process(ttrs)
        bt_prcss.draw_button('released')
        del bt_prcss

        return
    # print(ttrs.current_block.center_point.x, ttrs.current_block.center_point.y)
    temp_block = cp.copy(ttrs.current_block)
    pt_t = temp_block.center_point
    # print('func otmr')
    if  ttrs.is_collision(ttrs.current_block,pt_t.x,pt_t.y-1) :
        # print('otmr - collision')
        ttrs.current_block.draw('fixed')
        ttrs.block_piling()
        # return
    else :
        ttrs.move_sequence(0,-1, 'float')
        # print('ydistance :', ttrs.calc_ydistance())
        # print(3)

    del temp_block, pt_t
    t.ontimer(fun_otmr,1000)

def fun_onkey_up():

    # print('func key up')
    temp_block = cp.copy(ttrs.current_block)
    temp_block.rotate()
    if  ttrs.is_collision(temp_block,temp_block.center_point.x, temp_block.center_point.y) :
        # print('key up collision')
        del temp_block
        return
    else :
        ttrs.current_block.draw('erase')
        ttrs.current_block.rotate()
        ttrs.current_block.draw('float')
    del temp_block

def fun_onkey_down():
    # print(' func key down')
    temp_block = cp.copy(ttrs.current_block)
    pt_t = temp_block.center_point

    if  ttrs.is_collision(ttrs.current_block,pt_t.x,pt_t.y-1) :
        # print('onkey down - collision')
        ttrs.current_block.draw('fixed')
        ttrs.block_piling()
        del temp_block, pt_t
        return
    else :
        ttrs.move_sequence(0,-1, 'float')

    del temp_block, pt_t

def fun_onkey_left():
    # print(' func key left')
    temp_block = cp.copy(ttrs.current_block)
    pt_t = temp_block.center_point

    if  ttrs.is_collision(ttrs.current_block,pt_t.x-1,pt_t.y) :
        # print('onkey left - collision')
        del temp_block, pt_t
        return
    else :
        ttrs.move_sequence(-1,0, 'float')

    del temp_block, pt_t

def fun_onkey_right():
    # print(' func key right')
    temp_block = cp.copy(ttrs.current_block)
    pt_t = temp_block.center_point

    if  ttrs.is_collision(ttrs.current_block,pt_t.x+1,pt_t.y) :
        # print('onkey right - collision')
        del temp_block, pt_t
        return
    else :
        ttrs.move_sequence(1,0,'float')

    del temp_block, pt_t


def fun_onkey_space():
    # print(' func key space')
    ydistance = ttrs.calc_ydistance()

    ttrs.move_sequence(0,-ydistance, 'fixed')
    ttrs.block_piling()

    del ydistance



class write_inform:
    def __init__(self):
        self.pen = t.Turtle()
        self.point = Point(-300, 200)
        self.pen.up()

    def write(self,str):
        self.pen.goto(self.point.x, self.point.y)
        self.pen.color('black')
        self.pen.write(str, align="center", font=("Arial", 16, "normal"))

    def erase(self):
        # self.pen.color(ttrs.bgcolor)
        self.pen.color('red')
        self.pen.goto(self.point.x, self.point.y)
        self.pen.down()
        self.pen.goto(self.point.x-75, self.point.y-75)
        self.pen.begin_fill()
        self.pen.goto(self.point.x-75, self.point.y+75)
        self.pen.goto(self.point.x + 75, self.point.y + 75)
        self.pen.goto(self.point.x + 75, self.point.y - 75)
        self.pen.end_fill()
        self.pen.up()

    def pt(self, x,y):
        self.point = Point(x,y)




def write_informations(str, color):
    write = write_inform()
    write.erase()
    write.pen.color(color)
    write.write(str)
    del write


class button_process:
    def __init__(self, tetris):
        self.pos = Point(-325, 100)
        self.color = 'light gray'
        self.shadow_color = 'gray'
        self.ft_color = 'black'
        self.release_time = 250 # [msec]
        self.ttrs = tetris




    def draw_button(self, state):
        l_width, l_height = 75, 35
        offset = 5
        s_width, s_height = l_width-offset, l_height-offset

        if  state == 'clicked':
            color = self.shadow_color
            shadow_color = self.color
        elif state == 'released':
            color = self.color
            shadow_color = self.shadow_color

        to1 = t.Turtle()
        to1.ht()
        to1.fillcolor(color)
        to1.up()
        to1.goto(self.pos.x, self.pos.y)
        to1.down()
        to1.begin_fill()
        to1.goto(self.pos.x+l_width, self.pos.y)
        to1.goto(self.pos.x+l_width, self.pos.y-l_height)
        to1.goto(self.pos.x+s_width, self.pos.y-s_height)
        to1.goto(self.pos.x+s_width, self.pos.y-offset)
        to1.goto(self.pos.x+offset, self.pos.y-offset)
        to1.goto(self.pos.x, self.pos.y)
        to1.end_fill()

        to1.goto(self.pos.x+offset, self.pos.y-offset)
        to1.begin_fill()
        to1.goto(self.pos.x+s_width, self.pos.y-offset)
        to1.goto(self.pos.x+s_width, self.pos.y-s_height)
        to1.goto(self.pos.x+offset, self.pos.y-s_height)
        to1.goto(self.pos.x+offset, self.pos.y-offset)
        to1.end_fill()

        to1.fillcolor(shadow_color)

        to1.begin_fill()
        to1.goto(self.pos.x, self.pos.y)
        to1.goto(self.pos.x, self.pos.y-l_height)
        to1.goto(self.pos.x+l_width, self.pos.y-l_height)
        to1.goto(self.pos.x+s_width, self.pos.y-s_height)
        to1.goto(self.pos.x+offset, self.pos.y-s_height)
        to1.goto(self.pos.x+offset, self.pos.y-offset)
        to1.goto(self.pos.x, self.pos.y)
        to1.end_fill()

        write = write_inform()
        write.pt(self.pos.x + 35, self.pos.y - 30 )
        write.write('Start')

        del to1
        del write
        del l_width, l_height, offset, s_width, s_height



g_key_flag = 0
g_game_over = 0
g_timer_out = 1

ttrs = Tetris()
t.delay(0)
t.tracer(0,0)
t.shape('square')
set_bit(g_game_over)
ttrs.run()
