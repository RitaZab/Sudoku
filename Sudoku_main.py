import pygame as pyg, sys,random

pyg.init()
pyg.display.set_caption("Have fun with SUDOKU game made by Rita Zet!")

#global variables
width=650
height=650
bg_color=(230, 179, 117)
window=pyg.display.set_mode((width, height))
lines_col=(38, 24, 7)
nr_font=pyg.font.SysFont("comicsansms", 45)

from random import sample
base=3
side=base*base
def pattern(row,col):
    return (base*(row%base)+row//base+col)%side
def shuffle(s):
    return sample(s,len(s))
rowBase=range(base)
rows=[g*base + row for g in shuffle(rowBase) for row in shuffle(rowBase)]
cols=[g*base +col for g in shuffle(rowBase) for col in shuffle (rowBase)]
numbers=shuffle(range(1,base*base+1))
board=[[numbers[pattern(row,col)] for col in cols]for row in rows]



squares=side*side
empty_places=squares*3//4
for place in sample(range(squares),empty_places):
    board[place//side][place%side]=0

numSize = len(str(side))
for line in board:
    print(*(f"{n or ' ':{numSize}} " for n in line))









#functions
def display_window():
    window.fill(bg_color)
    pyg.draw.rect(window, lines_col, pyg.Rect(10,10,630,630),8)
    li=1
    while(li*70)<630:
        line_width=3 if li %3 >0 else 6
        pyg.draw.line(window,lines_col, pyg.Vector2((li*70)+10,10),pyg.Vector2((li*70)+10,635),line_width)
        pyg.draw.line(window, lines_col, pyg.Vector2(10,(li*70)+10), pyg.Vector2(635,(li*70)+10),line_width)
        li+=1

def display_numbers():

    row=0
    while row < 9:
        col=0
        while col <9:
            if board[row][col] != 0:
                visible_numbers=board[row][col]
                nr_text=nr_font.render(str(visible_numbers), True, lines_col)
                window.blit(nr_text, pyg.Vector2((col*70)+33,(row*70)+15))
            col+=1
        row+=1

def draw_criss_cross():
    pass

def main_game():
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
    display_window()
    display_numbers()
    pyg.display.flip()

while True:
    main_game()
