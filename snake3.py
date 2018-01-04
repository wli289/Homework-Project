# -*- coding: utf-8 -*-

from Tkinter import *
from random import randint
import tkMessageBox
import datetime

class SnakeGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid = Grid(master)
        self.snake = Snake(self.grid)
        self.food = Food(self.grid)
        self.gameover = False
        self.score = 0
        self.status = ['run', 'stop']
        self.speed = [300, 100]
        self.grid.canvas.bind_all("<KeyRelease>", self.key_release)
        self.display_food()
        # Used to set color changing food
        self.color_c = ("#FFB6C1","#6A5ACD","#0000FF","#F0FFF0","#FFFFE0","#F0F8FF","#EE82EE","#000000","#5FA8D9","#32CD32")
        self.i = 0
        # The left side of the screen shows the score
        self.score_frame = Frame(master)
        self.score_frame.pack()
        self.str_score = StringVar()
        self.ft1 = ('Fixdsys', 40, "bold")
        self.ft_record = ('Fixdsys', 20, "bold")

        self.operation_tip = Label(self.score_frame, text = "press P to stop\npress S to change mode(speed／slow mode)\n\n", 
                                   font = ('Fixdsys', 15, "bold"))
        self.operation_tip.grid(row = 1, column = 1)        
        
        self.m1 = Message(self.score_frame, textvariable=self.str_score, aspect=5000, font=self.ft1, bg="#696969")
        self.m1.pack(side=LEFT, fill=Y)
        self.m1.grid(row = 2, column = 1)
        self.str_score.set("Score:"+str(self.score))
        
        self.messagebox_record = Label(self.score_frame, 
                                       text = self.loadrecord(), 
                                       font = self.ft_record)
        self.messagebox_record.grid(row = 3, column = 1)
        


    
    def loadrecord(self):
        s = 'Record\n'
        f = open('snakerecord.dat', 'r')
        try:
            l = f.readlines()
            temp = []
            for a in l:
                temp.append(a.split())
            temp = sorted(temp, key = lambda x : int(x[0]), reverse = True)
            
            for a in temp[:10]:  # first 10 lines
                s = s + a[0] + ' ' + a[1] + ' ' + a[2] + '\n'
            return s
        except:
            print('open the record file fail')
        finally:
            f.close()
      
        return s
   
    def saverecord(self, score):
        f = open('snakerecord.dat', 'a')
        s = str(score) + ' ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n';
        f.write(s)
        f.close()
        
    # initialize the game when it restarts
    def initial(self):
        self.gameover = False
        self.score = 0
        self.str_score.set("Score:"+str(self.score))
        self.snake.initial()

    #type1:normal food  type2:length-2  type3:initial length  type4:change color
    def display_food(self):
        self.food.color = "#23D978"
        self.food.type = 1
        if randint(0, 40) == 5:
            self.food.color = "#FFD700"
            self.food.type = 3
            while (self.food.pos in self.snake.body):
                self.food.set_pos()
            self.food.display()
        elif randint(0, 4) == 2:
            self.food.color = "#EE82EE"
            self.food.type = 4
            while (self.food.pos in self.snake.body):
                self.food.set_pos()
            self.food.display()
        elif len(self.snake.body) > 10 and randint(0, 16) == 5:
            self.food.color = "#BC8F8F"
            self.food.type = 2
            while (self.food.pos in self.snake.body):
                self.food.set_pos()
            self.food.display()
        else:
            while (self.food.pos in self.snake.body):
                self.food.set_pos()
            self.food.display()

    def key_release(self, event):
        key = event.keysym
        key_dict = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        # Snake can not go in the opposite direction
        if key_dict.has_key(key) and not key == key_dict[self.snake.direction]:
            self.snake.direction = key
            self.move()
        elif key == 'p':
            self.status.reverse()
        elif key == 's':
            self.speed.reverse()

    def run(self):
        # determine if the game is paused
        if not self.status[0] == 'stop':
            # Judge whether the game is over
            if self.gameover == True:
                message = tkMessageBox.showinfo("Game Over", "your score: %d" % self.score)
                self.saverecord(self.score)
                if message == 'ok':
                    self.initial()
            if self.food.type == 4:
                color = self.color_c[self.i]
                self.i = (self.i+1)%10
                self.food.color = color
                self.food.display()
                self.move(color)
            else:
                self.move()
        self.after(self.speed[0], self.run)

    def move(self, color="#EE82EE"):
        # Calculate the next point the snake moves
        head = self.snake.body[0]
        if self.snake.direction == 'Up':
            if head[1] - 1 < 0:
                new = (head[0], 16)
            else:
                new = (head[0], head[1] - 1)
        elif self.snake.direction == 'Down':
            new = (head[0], (head[1] + 1) % 16)
        elif self.snake.direction == 'Left':
            if head[0] - 1 < 0:
                new = (24, head[1])
            else:
                new = (head[0] - 1, head[1])
        else:
            new = ((head[0] + 1) % 24, head[1])
            # Hit itself, set the game end flag, waiting for the next cycle
        if new in self.snake.body:
            self.gameover=True
        # eat the food
        elif new == self.food.pos:
            if self.food.type == 1:
                self.snake.add(new)
            elif self.food.type == 2:
                self.snake.cut_down(new)
            elif self.food.type == 4:
                self.snake.change(new, color)
            else:
                self.snake.init(new)
            self.display_food()
            self.score = self.score+1
            self.str_score.set("Score:" + str(self.score))
        # nothing happens
        else:
            self.snake.move(new)

class Grid(object):
    def __init__(self, master=None,height=16, width=24, offset=10, grid_width=40, bg="#808080"):
        self.height = height
        self.width = width
        self.offset = offset
        self.grid_width = grid_width
        self.bg = bg
        self.canvas = Canvas(master, width=self.width*self.grid_width+2*self.offset,
                             height=self.height*self.grid_width+2*self.offset, bg=self.bg)
        self.canvas.pack(side=RIGHT, fill=Y)

    def draw(self, pos, color, ):
        x = pos[0] * self.grid_width + self.offset
        y = pos[1] * self.grid_width + self.offset

        self.canvas.create_rectangle(x, y, x + self.grid_width, y + self.grid_width, fill=color, outline=self.bg)

class Food(object):
    def __init__(self, grid, color = "#23D978"):
        self.grid = grid
        self.color = color
        self.set_pos()
        self.type = 1

    def set_pos(self):
        x = randint(0, self.grid.width - 1)
        y = randint(0, self.grid.height - 1)
        self.pos = (x, y)

    def display(self):
        self.grid.draw(self.pos, self.color)


class Snake(object):
    def __init__(self, grid, color = "#000000"):
        self.grid = grid
        self.color = color
        self.body = [(8, 11), (8, 12), (8, 13)]
        self.direction = "Up"
        for i in self.body:
            self.grid.draw(i, self.color)

    # initialize the snake's position when the game is restarted
    def initial(self):
        while not len(self.body) == 0:
            pop = self.body.pop()
            self.grid.draw(pop, self.grid.bg)
        self.body = [(8, 11), (8, 12), (8, 13)]
        self.direction = "Up"
        self.color = "#000000"
        for i in self.body:
            self.grid.draw(i, self.color)

    # The snake moves to a specified point
    def move(self, new):
        self.body.insert(0, new)
        pop = self.body.pop()
        self.grid.draw(pop, self.grid.bg)
        self.grid.draw(new, self.color)

    # The snake moves to a specified point and increases the length
    def add(self ,new):
        self.body.insert(0, new)
        self.grid.draw(new, self.color)

    # Snake eat a special food 1, cut their length
    def cut_down(self,new):
        self.body.insert(0, new)
        self.grid.draw(new, self.color)
        for i in range(0,3):
            pop = self.body.pop()
            self.grid.draw(pop, self.grid.bg)

    # Snake eat special food 2, back to the original length
    def init(self, new):
        self.body.insert(0, new)
        self.grid.draw(new, self.color)
        while len(self.body) > 3:
            pop = self.body.pop()
            self.grid.draw(pop, self.grid.bg)

     # Snake eat special food 3, changed its own color
    def change(self, new, color):
        self.color = color
        self.body.insert(0, new)
        for item in self.body:
            self.grid.draw(item, self.color)



if __name__ == '__main__':
    root = Tk()
    snakegame = SnakeGame(root)
    snakegame.run()
    snakegame.mainloop()