# generate random numbers for sudoku
from random import sample
from tkinter import *
import copy

base = 3
side = base * base
# pattern for a baseline valid solution
def pattern(r, c): return (base * (r % base) + r // base + c) % side
# randomize rows, columns and numbers (of valid base pattern)
def shuffle1(s): return sample(s, len(s))

rBase = range(base)
rows = [g * base + r for g in shuffle1(rBase) for r in shuffle1(rBase)]
cols = [g * base + c for g in shuffle1(rBase) for c in shuffle1(rBase)]
nums = shuffle1(range(1, base * base + 1))

# produce board using randomized baseline pattern
soln_board = [[nums[pattern(r, c)] for c in cols] for r in rows]
board = copy.deepcopy(soln_board)

# for line in board: print(line)
squares = side * side
empties = squares * 3 // 4
for p in sample(range(squares), empties):
    board[p // side][p % side] = 0
'''
for k in range(9):
    for m in range(9):
        print(soln_board[k][m],end =" ")

    print() '''

def show_solution():
    l4 = Label(my_window,text="",font=("Arial Bold",12))
    for i in range(9):
        for j in range(9):
            l4["text"]= l4["text"]+ str(soln_board[i][j]) + "  "
        l4["text"] =l4["text"] + "\n"
    l4.pack()


def check_solution():
    result = True
    temp=0
    for i,j in index:
        try:
            temp = int(l[i][j].get())
        except ValueError:
            l3["text"]="Enter valid integer values"

        if temp != soln_board[i][j]:
            result = False
            break
    if not result:
            l3["text"]="The solution is invalid Check again"
    else:
        l3["text"]="correct solution\n"
    b2 =Button(my_window,text="Show Solution",command=show_solution)
    b2.pack()


index=[]
l = [[0 for x in range(9)] for y in range(9)]
my_window = Tk()
my_window.title("Sudoku")
frame1 = Frame(my_window)
frame1.pack()
for i in range(9):

    for j in range(9):

        if board[i][j] != 0:
            l[i][j] = Label(frame1, text=board[i][j], font=("Arial Bold", 12))
            l[i][j].grid(row=i, column=j)
        else:
            l[i][j] = Entry(frame1,width=2)
            l[i][j].grid(row=i, column=j)
            index.append([i,j])

b1 = Button(my_window, text="Check Solution",command=check_solution)
b1.pack()
l3 =Label(my_window,text="",font=("Arial Bold",12))
l3.pack()
# my_window.geometry(300,300)
my_window.mainloop()