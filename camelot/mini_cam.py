import time
from tkinter import *

import numpy as np


class MiniCamelot(object):

    def __init__(self):
        #rows for the game board
        self.row1 = [-1] + [0] * 6 + [-1]
        self.row2 = [-1] * 2 + [0] * 4 + [-1] * 2
        self.row3 = [-1] * 3 + [0] * 2 + [-1] * 3
        self.dead = []
        self.saved_x = 0
        self.saved_y = 0
        self.prev_play = None

    #terminal test for alpha-beta and for checking for winners
    def end(self, grid):
        victor = None
        use, com = self.num(grid, 0, 0)
        if grid[1][3] == 2 and grid[1][4] == 2:
            #the computer is victorious by occupying the castle
            victor = 2
        elif grid[-1][3] == 1 and grid[-1][4] == 1:
            #the player is victorious by occupying castle
            victor = 1
        elif use < 2 and com > 1:
            #user does not have enough pieces and loses
            victor = 2
        elif use < 2 and com < 2:
            #Draw
            victor = 3
        elif com < 2 and use > 1:
            #computer does not have enough pieces
            victor = 1
        return victor

    #The evaluation function to calculate the utility of a state
    def evaluation(self, state):
        val = 0
        for i in range(14):
            for j in range(8):
                if state[i][j] == 2:
                    val += 140 - 15 * i
                elif state[i][j] == 1:
                    val -= i * 3
        val += 100 * (self.num(state, 0, 0)[1]) - 100 * (self.num(state, 0, 0)[0])

        if state[0][3] == 2 and state[0][4] == 2:
            val = 1000
        if state[13][3] == 1 and state[13][4] == 1:
            val = -1000
        return val
    #calculate number of pieces
    def num(self, game_board, u, c):
        for piece in game_board:
            u += piece.count(1)
            c += piece.count(2)
        return u, c

    #result of the board after a certain movement
    def board_result(self, state, move, player):
        k = move[0][0]
        j = move[0][1]
        nk = move[1][0]
        nj = move[1][1]
        nstate = self.transfer(state)
        enemy = 0
        if player == 1:
            enemy = 2
        elif player == 2:
            enemy = 1
        self.enem_check(k, nk, j, nj, nstate, enemy)
        nstate[k][j] = 0
        nstate[nk][nj] = player
        return nstate

    #returns a list of all possible moves
    def moves(self, grid, player):
        enemy = 0
        if player == 1:
            enemy = 2
        elif player == 2:
            enemy = 1
        location_list = self.nlist(grid, player)
        moves = []
        eaten = False
        for l in location_list:
            if l[0] == 0:
                continue
            x = l[0]
            y = l[1]
            # adds possible capture moves
            if self.compare(x + 2, x + 1, x + 2, y, y, 14, enemy):
                moves.append(((x, y), (x + 2, y)))
                eaten = True
            if self.comparer(x - 2, x - 1, x - 2, y, y, enemy):
                moves.append(((x, y), (x - 2, y)))
                eaten = True
            if self.compare(y + 2, x, x, y + 1, y + 2, 8, enemy):
                moves.append(((x, y), (x, y + 2)))
                eaten = True
            if self.comparer(y - 2, x, x, y - 1, y - 2, enemy):
                moves.append(((x, y), (x, y - 2)))
                eaten = True
        #if there is no capture move available
        if not eaten:
            for l in location_list:
                if l[0] == 0:
                    continue
                x, y = l
                #add all simple moves
                self.common_m(x, y, moves)
                # add catering moves
                self.cater_m(x, y, moves, player)
        return moves
    #function for comparison
    def simplify(self, x1, x3, y2, num):
        if x1 < num and self.grid[x3][y2] == 0:
            return True
        return False
    def simplifier(self, x1, x3, y2):
        if x1 >= 0 and self.grid[x3][y2] == 0:
            return True
        return False
    #update player info of a position of a new state
    def enem_check(self, k, nk, j, nj, nstate, enemy):
        if nstate[int((k + nk) / 2)][int((j + nj) / 2)] == enemy:
            nstate[int((k + nk) / 2)][int((j + nj) / 2)] = 0
        return nstate
    #function for simple moves
    def common_m(self, x, y, moves):
        if self.simplifier(y-1,x,y-1):
            moves.append(((x, y), (x, y - 1)))
        if self.simplify(y+1,x,y+1,8):
            moves.append(((x, y), (x, y + 1)))
        if self.simplifier(x - 1, x-1, y):
            moves.append(((x, y), (x - 1, y)))
        if self.simplify(x + 1, x + 1, y, 8):
            moves.append(((x, y), (x + 1, y)))
        return moves
    #simplfy comparison and approval
    def compare(self, x1, x2, x3, y1, y2, num, player):
        if x1 < num and self.grid[x2][y1] == player and self.grid[x3][y2] == 0:
            return True
        return False
    def comparer(self, x1, x2, x3, y1, y2, player):
        if x1 >= 0 and self.grid[x2][y1] == player and self.grid[x3][y2] == 0:
            return True
        return False
    def transfer(self, list):
        return [i[:] for i in list]
    #function for catering moves
    def cater_m(self, x, y, moves, user):
        if self.comparer(x-2, x-1, x-2, y, y, user):
            moves.append(((x, y), (x - 2, y)))
        if self.compare(x + 2, x+1, x+2, y, y, 14, user):
            moves.append(((x, y), (x + 2, y)))
        if self.comparer(y - 2, x, x, y-1, y-2, user):
            moves.append(((x, y), (x, y - 2)))
        if self.compare(y+2, x, x, y+1, y+2, 8, user):
            moves.append(((x, y), (x, y + 2)))
        return moves

    def nlist(self, grid, player):
        ngrid = np.array(grid)
        return np.asarray(np.where(ngrid == player)).T
    #start the game
    def start_game(self):
        self.game_finish = False
        self.winner = None
        self.grid = [self.row3, self.row2, self.row1, [0] * 8, [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0], [0] * 8, [0] * 8, [0, 0, 0, 2, 2, 0, 0, 0],
                     [0, 0, 2, 2, 2, 2, 0, 0], [0] * 8, self.row1, self.row2, self.row3]
        print(self.grid)
#Gameboard dimensions
Width = 400
Height = 640
Border = 40
#Create the UI for the game using Tkinter
class MiniCamelotBoard(Frame):
    Width = 400
    Height = 640
    Border = 40

    def __init__(self, parent, board):
        self.board = board
        self.parent = parent
        Frame.__init__(self, parent)
        self.i, self.j = -1, -1
        self.useri()
    def useri(self):
        self.parent.title("Mini Camelot 2017")
        self.canvas = Canvas(self, width=self.Width, height=self.Height)
        self.canvas.configure(background='black')
        self.pack(fill=BOTH, expand=1)
        self.canvas.pack(fill=BOTH, side=TOP)
        self.game_map()
        self.theboard()
        #use mouse click to select boxes
        self.canvas.bind("<Button-1>", self.box_clicked)

    #approximate square location
    def adjust_size(self, x):
        return x // 40 - 1
    #create the board with lines
    def theboard(self):
        k = 80
        r = 4
        Border = self.Border
        self.horizontal(k, r, Border)
        self.vertical(k, r, Border)

    #check if anyone won. If someone did, display winning message on the screen
    def victory_check(self):
        victor = self.board.end(self.board.grid)
        #if there is a winner finish game
        if victor is not None:
            self.board.game_finish = True
        print(self.board.game_finish)
        if self.board.game_finish:
            self.show_win(victor)
        else:
            self.com_move()
    #update player info of a location
    def computer_pos_check(self,i,j):
        if self.board.grid[int((self.i + i) / 2)][int((self.j + j) / 2)] == 2:
            self.board.grid[int((self.i + i) / 2)][int((self.j + j) / 2)] = 0
    # update position and change click position back to none
    def pos_review(self, i, j):
        if self.can_move(i, j):
            self.board.grid[self.i][self.j] = 0
            self.board.grid[i][j] = 1
            self.computer_pos_check(i, j)
            self.i = -1
            self.j = -1
            self.game_map()
            self.victory_check()

    #get position of the box clicked and record position of clicked box
    def box_clicked(self, event):
        x = event.x
        y = event.y
        if self.board.game_finish:
            return
        if (self.size_condition(Border, Height, y) and self.size_condition(Border, Width, x)):
            j = self.adjust_size(x)
            i = self.adjust_size(y)
            self.canvas.focus_set()
            if self.i != -1 and self.j != -1:
                self.pos_review(i, j)
            elif self.board.grid[i][j] == 1:
                self.i, self.j = i, j
            print('gamegrid', self.board.grid, 'grid', self.grid)
            print(i, j, 'ij')

    # Shows winner on the screen if there is one
    def show_win(self, victor):
        x = Border * 6
        y = Border * 10
        victory_txt = ''
        if victor == 1:
            victory_txt = "User"
        elif victor == 2:
            victory_txt = "Computer"
        elif victor == 3:
            victory_txt = "Draw"
        self.canvas.create_text(x, y, text=victory_txt + " wins!", tags="prevgrid", fill="white", font=("Helvetica", 25))

    def size_condition(self, b, h, x):
        return b < x < h - b

    #draws the board pieces, six for each player
    def game_map(self):
        self.canvas.delete("prevgrid")
        for i in range(14):
            for j in range(8):
                cor = self.board.grid[i][j]
                if cor == 1 or cor == 2:
                    f = ((j + 1) * 20) * 2
                    g = ((i + 1) * 20) * 2
                    w = (f + 10)
                    y = (g + 10)
                    x = (f + 30)
                    z = (g + 30)
                    color = "black" if cor == 2 else "white"
                    self.canvas.create_oval(w, y, x, z, outline="white", tag="prevgrid", fill=color, width=2)

    #check if a piece nearby can be eaten(captured)
    def be_eaten(self):
        if self.j + 2 < 8 and self.board.grid[self.i][self.j + 1] == 2 \
                and self.board.grid[self.i][self.j + 2] == 0:
            return True
        elif self.i + 2 < 14 and self.board.grid[self.i + 1][self.j] == 2 \
                and self.board.grid[self.i + 2][self.j] == 0:
            return True
        elif self.i - 2 >= 0 and self.board.grid[self.i - 1][self.j] == 2 \
                and self.board.grid[self.i - 2][self.j] == 0:
            return True
        elif self.j - 2 >= 0 and self.board.grid[self.i][self.j - 2] == 0 \
                and self.board.grid[self.i][self.j - 1] == 2:
            return True
        return False

    #draw lines for board
    def horizontal(self, k, r, Border):
        for i in range(r - 1):
            w = ((i + 1) * 20 + r * 5) * 2
            x = (k * 2 - (i + 1) * 20 + r * 5) * 2
            y = ((i + (r * 3) + 1) * 20) * 2
            z = ((i + (r * 3) + 1) * 20) * 2
            self.canvas.create_line(w, y, x, z, fill="white")

            for j in range(r + 3 - i, i, -1):
                w = j * r * 10 + r * 10
                x = j * r * 10 + r * 10
                y = 2 * k + r * 10 * (r * 2)
                z = ((i + (r * 3) + 1) * r * 5) * 2
                self.canvas.create_line(w, y, x, z, fill="white")
        for i in range(r, (r * 3) + 1):
            w = r * 10
            x = k * r + r * 10
            y = i * r * 10
            z = i * r * 10
            self.canvas.create_line(w, y, x, z, fill="white")

    #makes the computer take a move through alpha-beta search and updates board with result
    def com_move(self):
        state = self.board.transfer(self.board.grid)
        comp_move = self.alpha_beta_search(state)
        self.board.grid = self.board.board_result(self.board.grid, comp_move, 2)
        self.game_map()
        victor = self.board.end(self.board.grid)
        if victor is not None:
            self.board.game_finish = True
            self.victory_check()

    def tidy(self, i, j):
        if self.j - j == 0 and abs(self.i - i) == 1:
            return True
        elif self.i - i == 0 and abs(self.j - j) == 1:
            return True
        else:
            ci = int((i + self.i) / 2)
            cj = int((j + self.j) / 2)
            if self.board.grid[ci][cj] == 1:
                return True
        return False
    def vertical(self, k, r, border):
        for i in range(r):
            w = (r - i) * 40 + r * 10
            x = (k * r) - (r - i) * 40 + r * 10
            y = i * r * 10
            z = i * r * 10
            self.canvas.create_line(w, y, x, z, fill="white")

            for j in range(r - 1 - i, r + 2 + i):
                w = j * 40 + r * 10
                x = j * 40 + r * 10
                y = (i + 1) * r * 10
                z = k * 2
                self.canvas.create_line(w, y, x, z, fill="white")
        for i in range(2 * r + 1):
            w = i * 40 + r * 10
            x = i * 40 + r * 10
            y = k * 2
            z = 160 + r * 10 * 8
            self.canvas.create_line(w, y, x, z, fill="white")

    #check if a move is legal
    def can_move(self, i, j):
        if self.be_eaten():
            print("you must capture")
            if abs(self.j - j) + abs(self.i - i) == 2:
                return True
        elif self.board.grid[i][j] == 0:
            if self.tidy(i, j):
                return True
        return False

    #alpha-beta search
    def alpha_beta_search(self, state, d=4, cutoff_test=None, evaluate=None):

        global dpth
        global min_pru
        global nodes
        global max_pru
        global passed
        passed = time.time()
        nodes = 0
        dpth = 0
        min_pru = 0
        max_pru = 0
        player = 2
        def max_value(state, alpha, beta, depth):
            global nodes
            global max_pru
            global passed
            cur_time = time.time()
            used_time = cur_time - passed
            if cutoff_test(state, depth, used_time):
                global dpth
                dpth = depth
                return evaluate(state)
            val = -9999
            for move in self.board.moves(state, 2):
                nodes += 1
                val = max(val, min_value(self.board.board_result(state, move, 2), alpha, beta, depth + 1))
                if val >= beta:
                    max_pru += 1
                    return val
                alpha = max(alpha, val)
            return val

        def min_value(state, alpha, beta, depth):
            global nodes
            global min_pru
            global passed
            current_time = time.time()
            used_time = current_time - passed
            # check if cutoff is reached
            if cutoff_test(state, depth, used_time):
                global dpth
                dpth = depth
                return evaluate(state)
            v = 9999
            for move in self.board.moves(state, 1):
                nodes += 1
                v = min(v, max_value(self.board.board_result(state, move, 1), alpha, beta, depth + 1))
                if v <= alpha:
                    min_pru += 1
                    return v
                beta = min(beta, v)
                print(alpha, beta, 'ab')
            return v

        cutoff_test = (cutoff_test or (lambda state, depth, time: depth > d or self.board.end(state)))
        evaluate = evaluate or (lambda state: self.board.evaluation(state))

        best_eval = -9999
        beta = 9999
        best_move = None
        state = state[::]
        for move in self.board.moves(state, 2):
            v = min_value(self.board.board_result(state, move, 2), best_eval, beta, 1)
            if v > best_eval:
                best_move = move
                best_eval = v
        t2 = time.time()
        print('Evaluation score: ', best_eval )
        print("Nodes generated:", nodes)
        print("Max depth reached:", dpth)
        print("Pruning in MIN-VALUE:", min_pru)
        print("Pruning in MAX-VALUE:", max_pru)
        print("Move:", best_move)
        print("Time used:", t2 - passed)
        return best_move

#Play the game
if __name__ == "__main__":
    root = Tk()
    camelot = MiniCamelot()
    camelot.start_game()
    MiniCamelotBoard(root, camelot)
    root.mainloop()
