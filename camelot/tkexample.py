import tkinter as tk
import time
import random


class GameBoard(tk.Frame):
    def __init__(self, parent, named_1,
                 named_2, photo_w, photo_b, rows=14, columns=8, size=32, color1="white", color2="black"):
        '''size is the size of a square, in pixels'''

        self.named_1 = named_1
        self.named_2 = named_2
        self.photo_w = photo_w
        self.photo_b = photo_b
        self.list = []
        self.list2 = []
        for key in named_1.items():
            self.list.append(key[0])

        self.list.sort()
        self.name1_1 = self.list[0]
        self.name1_2 = self.list[1]
        self.name1_3 = self.list[2]
        self.name1_4 = self.list[3]
        self.name1_5 = self.list[4]
        self.name1_6 = self.list[5]

        for key in named_2.items():
            self.list2.append(key[0])

        self.list2.sort()
        self.name2_1 = self.list2[0]
        self.name2_2 = self.list2[1]
        self.name2_3 = self.list2[2]
        self.name2_4 = self.list2[3]
        self.name2_5 = self.list2[4]
        self.name2_6 = self.list2[5]
        self.location1_1 = named_1[self.name1_1]
        self.location1_2 = named_1[self.name1_2]
        self.location1_3 = named_1[self.name1_3]
        self.location1_4 = named_1[self.name1_4]
        self.location1_5 = named_1[self.name1_5]
        self.location1_6 = named_1[self.name1_6]
        self.location2_1 = named_2[self.name2_1]
        self.location2_2 = named_2[self.name2_2]
        self.location2_3 = named_2[self.name2_3]
        self.location2_4 = named_2[self.name2_4]
        self.location2_5 = named_2[self.name2_5]
        self.location2_6 = named_2[self.name2_6]
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
        self.name_holder = ''
        self.prev_name = 'random'
        self.location_list_1 = [self.location1_1, self.location1_2, self.location1_3, self.location1_4,
                                self.location1_5, self.location1_6]
        self.location_list_2 = [self.location2_1, self.location2_2, self.location2_3, self.location2_4,
                                self.location2_5, self.location2_6]
        self.turn = ""
        self.dead = []
        self.saved_x = 0
        self.saved_y = 0
        self.eaten_turn = 0
        self.plays = 0
        self.prev_turn = ''
        self.background = [(13, 0), (13, 1), (13, 2), (13, 5), (13, 6), (13, 7), (0, 7), (0, 6), (0, 5), (0, 2),
                           (0, 1), (12, 0), (12, 1), (12, 6), (12, 7), (1, 0), (1, 6), (1, 7), (0, 0), (11, 0),
                           (11, 7), (2, 0), (2, 7)]

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.canvas.bind("<B1-Motion>", self.move_image)
        self.canvas.bind("<ButtonRelease-1>", self.release_button)
        self.canvas.bind("<Configure>", self.refresh)

    def release_button(self, event):
        self.plays = 0

        print(self.turn)

    def move_image(self, event):
        self.yard_x = self.saved_x
        self.yard_y = self.saved_y
        x = event.x // 31
        y = event.y // 31
        if self.turn == "":
            self.turn = "w"
        elif self.turn == "w":
            self.prev_turn = "w"
            if x == self.named_1[self.name1_1][1] and y == self.named_1[self.name1_1][0]:
                self.name_holder = self.name1_1

                # self.turn = "b"

            elif x == self.named_1[self.name1_2][1] and y == self.named_1[self.name1_2][0]:
                self.name_holder = self.name1_2
                # self.turn = "b"

            elif x == self.named_1[self.name1_3][1] and y == self.named_1[self.name1_3][0]:
                self.name_holder = self.name1_3
                # self.turn = "b"

            elif x == self.named_1[self.name1_4][1] and y == self.named_1[self.name1_4][0]:
                self.name_holder = self.name1_4
                # self.turn = "b"

            elif x == self.named_1[self.name1_5][1] and y == self.named_1[self.name1_5][0]:
                self.name_holder = self.name1_5
                # self.turn = "b"

            elif x == self.named_1[self.name1_6][1] and y == self.named_1[self.name1_6][0]:
                self.name_holder = self.name1_6
                # self.turn = "b"


        elif self.turn == "b":
            self.prev_turn = "b"
            # if x == self.named_2[self.name2_1][1] and y == self.named_2[self.name2_1][0]:
            #     self.name_holder = self.name2_1
            #     self.turn = "w"
            #
            # elif x == self.named_2[self.name2_2][1] and y == self.named_2[self.name2_2][0]:
            #     self.name_holder = self.name2_2
            #     self.turn = "w"
            #
            # elif x == self.named_2[self.name2_3][1] and y == self.named_2[self.name2_3][0]:
            #     self.name_holder = self.name2_3
            #     self.turn = "w"
            #
            # elif x == self.named_2[self.name2_4][1] and y == self.named_2[self.name2_4][0]:
            #     self.name_holder = self.name2_4
            #     self.turn = "w"
            #
            # elif x == self.named_2[self.name2_5][1] and y == self.named_2[self.name2_5][0]:
            #     self.name_holder = self.name2_5
            #     self.turn = "w"
            #
            # elif x == self.named_2[self.name2_6][1] and y == self.named_2[self.name2_6][0]:
            #     self.name_holder = self.name2_6
            #     self.turn = "w"

            self.name_holder = self.com()
            self.turn = 'w'

        if self.prev_name != self.name_holder:

            if "player1" in self.name_holder:
                self.named_1[self.name_holder] = (y, x)

            elif "player2" in self.name_holder:

                self.named_2[self.name_holder] = \
                self.com_move(self.named_2[self.name_holder][0], self.named_2[self.name_holder][1])[1]
                y = self.named_2[self.name_holder][0]
                x = self.named_2[self.name_holder][1]
                print("commove ", y, x)
                self.addpiece(self.name_holder, self.photo_b, y, x)
                self.location_update(self.name_holder, x, y)
                print(self.name_holder, "pls here")
                # y = x[0]
                # x = x[1]
                self.turn = 'w'
            self.prev_name = self.name_holder

        if self.plays == 0:
            print(self.name_holder)
            if self.restriction(y, x, self.name_holder):
                print("here?")
                self.saved_x = x
                self.saved_y = y
                self.addpiece(self.name_holder, self.photo_w, y, x)
                self.location_update(self.name_holder, x, y)
                self.eaten_turn = 0
                self.plays = 1
                if self.turn == 'w':
                    self.turn = 'b'
                elif self.turn == 'b':
                    self.turn == 'w'

                print('1', self.location_list_1, '2', self.location_list_2)
        self.check_win()
        self.canvas.update()

    def com(self):
        big = 0
        potent = ''
        for k, v in self.named_2.items():
            y = v[0]
            x = v[1]
            ny = self.com_move(y, x)[1][0]
            nx = self.com_move(y, x)[1][1]
            list1 = self.location_list_1
            list2 = self.location_list_2
            try:
                list2.remove((y, x))
            except:
                pass
            print(ny, nx, 'nynx')
            list2.append((ny, nx))
            if big < self.eval(list1, list2):
                big = self.eval(list1, list2)
                potent = k
            list2.append((y, x))
        return potent

    def com_move(self, y, x):
        ty = self.alphabeta_cutoff_search(y, x, self.location_list_1, self.location_list_2)[0]
        tx = self.alphabeta_cutoff_search(y, x, self.location_list_1, self.location_list_2)[1]
        tx = tx[::-1]
        print(y, x, "thissssssssss")
        print("This is it", ty, tx)
        self.turn = 'w'
        return ty, tx

    def restriction(self, y, x, name):
        if "player1" in name:

            if self.named_1[name][0] - 2 < y < self.named_1[name][0] + 2 and \
                                            self.named_1[name][1] - 2 < x < self.named_1[name][1] + 2:

                if (y, x) not in self.location_list_1 and (y, x) not in self.location_list_2:
                    cy = self.named_1[name][0]
                    cx = self.named_1[name][1]

                    counter = 0

                    p_finder = [(cy + 1, cx), (cy - 1, cx), (cy + 1, cx + 1), (cy - 1, cx - 1), (cy + 1, cx - 1),
                                (cy - 1, cx + 1),
                                (cy, cx + 1), (cy, cx - 1)]

                    counter = 0

                    for i in p_finder:
                        for e in self.location_list_2:
                            counter += 1

                            if i == e and self.eaten_turn == 0:
                                counter = 0
                                self.can_eat_player(e, cy, cx, y, x, name)
                                #                             self.remove_piece((cy, cx))

                                self.eaten_turn += 1

                            if counter == len(self.location_list_2) * 8:
                                return True

                        for e in self.location_list_1:

                            if i == e:
                                self.can_jump_over(e, cy, cx, y, x, name)
                                return True

                    return False

        elif "player2" in name:
            print("lool ", self.named_2[name][0])
            if type(self.named_2[name][0]) == tuple:
                self.named_2[name] = (y, self.named_2[name][0][1])
                print(self.named_2[name])
            if self.named_2[name][0] - 2 < y < self.named_2[name][0] + 2 and \
                                            self.named_2[name][1] - 2 < x < self.named_2[name][1] + 2:
                if (y, x) not in self.location_list_2 and (y, x) not in self.location_list_1:
                    self.turn = 'w'
                    return True

        return False

    def possible_moves(self, cx, cy):
        print('tuple? ', cx)
        print(type(cx))
        if type(cx) == tuple:
            cx = cx[1]
        p_finder = [(cy + 1, cx), (cy - 1, cx), (cy + 1, cx + 1),
                    (cy - 1, cx - 1), (cy + 1, cx - 1), (cy - 1, cx + 1),
                    (cy, cx + 1), (cy, cx - 1)]
        for i in self.location_list_2:
            if i in p_finder:
                print("this is i: ", i)
                p_finder.remove(i)
                if i == (cy + 1, cx):
                    t = cy + 2, cx

                elif i == (cy - 1, cx):
                    t = cy - 2, cx

                elif i == (cy + 1, cx + 1):
                    t = cy + 2, cx + 2

                elif i == (cy - 1, cx - 1):
                    t = cy - 2, cx - 2

                elif i == (cy + 1, cx - 1):
                    t = cy + 2, cx - 2

                elif i == (cy - 1, cx + 1):
                    t = cy - 2, cx + 2

                elif i == (cy, cx + 1):
                    t = cy, cx + 2

                elif i == (cy, cx - 1):
                    t = (cy, cx - 2)
                p_finder.append(t)
        for i in self.location_list_1:
            if i in p_finder:
                p_finder.remove(i)
                if i == (cy + 1, cx):
                    t = cy + 2, cx

                elif i == (cy - 1, cx):
                    t = cy - 2, cx

                elif i == (cy + 1, cx + 1):
                    t = cy + 2, cx + 2

                elif i == (cy - 1, cx - 1):
                    t = cy - 2, cx - 2

                elif i == (cy + 1, cx - 1):
                    t = cy + 2, cx - 2

                elif i == (cy - 1, cx + 1):
                    t = cy - 2, cx + 2

                elif i == (cy, cx + 1):
                    t = cy, cx + 2

                elif i == (cy, cx - 1):
                    t = (cy, cx - 2)

                p_finder.append(t)
        for i in p_finder:
            if i in self.location_list_2 or i in self.location_list_1:
                p_finder.remove(i)
            if i in self.background:
                p_finder.remove(i)
            for e in i:
                if e < 0:
                    print(i, "ggg")
                    print(p_finder,'find')
                    try:
                        p_finder.remove(i)
                    except:
                        pass
        return p_finder

    def possible_pieces(self):
        loc_list1 = []
        loc_list2 = []
        for e in self.location_list_1:
            if e != (0, 0):
                loc_list1.append(e)
        for e in self.location_list_2:
            if e != (0, 0):
                loc_list2.append(e)
        possible_destination = []
        for i in loc_list1:
            print(self.max_val(self.board_result(i[0], i[1])))
        for i in loc_list2:
            print(self.max_val(self.board_result(i[0], i[1])))

    def board_result(self, cy, cx):
        print('board ', cx)
        if type(cx) == tuple:
            cx = cx[1]
        possible_moves = self.possible_moves(cy, int(cx))
        traction = []
        for i in possible_moves:
            traction.append([(cy, cx), i])

        print('tra', traction)
        print("trax ", cx)
        return traction

    def alphabeta_cutoff_search(self, y, x, state1, state2, d=6, cutoff_test=None, eval_fn=None):

        player = 2

        global dep
        global node
        global min_pru
        global max_pru
        global t1
        t1 = time.time()
        node = 0
        dep = 0
        min_pru = 0
        max_pru = 0
        state = state1 + state2
        print("alphabeta ", x)

        def max_value(state1, state2, alpha, beta, depth):
            global node
            global max_pru
            global t1
            current_time = time.time()
            used_time = current_time - t1
            # print(used_time)
            # print(used_time > 10)
            if cutoff_test(state1, state2, depth, used_time):
                global dep
                dep = depth
                return eval_fn(state1, state2)
            v = -10000
            for a in self.board_result(y, x):
                node += 1

                state2.append(a[1])
                # print(state)
                # print(self.game.result(state, a, 1))
                v = max(v, min_value(state1, state2, alpha, beta, depth + 1))
                state2.remove(a[1])
                if v >= beta:
                    max_pru += 1
                    return v
                alpha = max(alpha, v)

            # state2.remove(a[0])
            return v

        def min_value(state1, state2, alpha, beta, depth):
            global node
            global min_pru
            global t1
            current_time = time.time()
            used_time = current_time - t1
            # print(used_time)
            if cutoff_test(state1, state2, depth, used_time):
                global dep
                dep = depth
                return eval_fn(state1, state2)
            v = 10000
            for a in self.board_result(y, x):
                node += 1

                state2.append(a[1])
                # print(self.game.result(state, a, 2))
                v = min(v, max_value(state1, state2, alpha, beta, depth + 1))
                state2.remove(a[1])
                # print(v)
                if v <= alpha:
                    min_pru += 1
                    return v
                beta = min(beta, v)
            print("this is a", a)
            print("state:", state2, state1)
            #            state2.remove(a[0])
            return v

        cutoff_test = (cutoff_test or
                       (lambda state1, state2, depth, time: depth > d or
                                                            self.check_win() or time > .2))
        eval_fn = eval_fn or (lambda state1, state2: self.eval(state1, state2))
        best_score = -10000
        beta = 10000
        best_action = None
        # t1 = time.time()
        state = state[::]
        for a in self.board_result(y, x):
            print(a, "this is a and this is state", state1, state2)
            print(a[0])

            state2.append(a[1])
            v = min_value(state1, state2, best_score, beta, 1)
            state2.remove(a[1])
            if v > best_score:
                best_score = v
                best_action = a
                #        state2.remove(a[0])
        t2 = time.time()
        print("node generated:", node)
        print("maximum depth reached:", dep)
        print("times of prunning in MAX-VALUE:", max_pru)
        print("times of prunning in MIN-VALUE:", min_pru)
        print("alphabeta used time", t2 - t1)
        return best_action

    def max_val(self, traction):
        eval_list = []
        for i in traction:
            temp = self.location_list_1
            temp2 = self.location_list_2
            try:
                temp.remove(i[0])
                temp.append(i[1])
            except ValueError:
                print(temp2, "tt", temp)
                print("kk", i[0])

                temp2.remove(i[0])
                temp2.append(i[1])

            eval_list.append(self.eval(temp, temp2))
        return max(eval_list)

    def min_val(self, traction):
        eval_list = []
        for i in traction:
            temp = self.location_list_1
            temp2 = self.location_list_2
            try:
                temp.remove(i[0])
                temp.append(i[1])
            except ValueError:
                temp2.remove(i[0])
                temp2.append(i[1])
            except ValueError:
                pass

            eval_list.append(self.eval(temp, temp2))
        return min(eval_list)

    def check_win(self):
        if self.num_of_b() < 2 and self.num_of_w() < 2:
            print("Draw!")
            return 0
        elif ((13, 3) in self.location_list_1 and (13, 4) in self.location_list_1) or (self.num_of_b() == 0):
            print("White Wins!")
            return -1000

        elif ((0, 3) in self.location_list_2 and (0, 4) in self.location_list_2) or (self.num_of_w() == 0):
            print("Black Wins!")
            return 1000

    def num_of_b(self):
        b = 0
        for i in self.location_list_2:
            if i != (0, 0):
                b += 1
        return b

    def num_of_w(self):
        w = 0
        for i in self.location_list_1:
            if i != (0, 0):
                w += 1
        return w

    def proximity1(self, list):
        dist = 0
        dist2 = 1
        for i in list:
            if i != (0, 0):
                if i[0] > dist:
                    dist = i[0]
                if dist > i[0] > dist2:
                    dist2 = i[0]
        return (dist + dist2)

    def proximity2(self, list):
        dist = 100
        dist2 = 101
        for i in list:
            if i != (0, 0):
                print("chec", i, list)
                if i[0] < dist:
                    dist = i[0]
                if dist < i[0] < dist2:
                    dist2 = i[0]
        return (26 - (dist + dist2))

    def eval(self, list1, list2):
        # smaller is better eval_func = closest distance to goal * (1/2)(number of enemy pieces) - 2(number of your pieces)
        b = self.num_of_b()
        w = self.num_of_w()
        if w < 2 and b < 2:
            return 0
        elif (13, 3) in list1 and (13, 4) in list1:
            print("White Wins!")
            return -1000

        elif (0, 3) in list2 and (0, 4) in list2:
            print("Black Wins!")
            return 1000

        eval_func = 100 * (b - w) + 100 * (self.proximity2(list2) - self.proximity1(list1))
        print(eval_func)
        return eval_func

    def remove_piece(self, i):
        t = ''
        for k, v in self.named_2.items():
            print('v', v, 'i', i)
            if v == i:
                t = k
                self.canvas.delete(t)
                self.dead.append(t)
                # print('v ', v)
                break
        if t != '':
            self.named_2[t] = (0, 0)

            #  print('1', self.location_list_1, '2', self.location_list_2)

    def occupied(self, y, x):
        return

    def can_eat_player(self, i, cy, cx, y, x, name):
        #  if 'player1' in  name:
        if i == (cy + 1, cx):
            self.named_1[name] = (cy + 2, cx)
            t = cy + 2, cx

        elif i == (cy - 1, cx):
            self.named_1[name] = (cy - 2, cx)
            t = cy - 2, cx

        elif i == (cy + 1, cx + 1):
            self.named_1[name] = (cy + 2, cx + 2)
            t = cy + 2, cx + 2

        elif i == (cy - 1, cx - 1):
            self.named_1[name] = (cy - 2, cx - 2)
            t = cy - 2, cx - 2

        elif i == (cy + 1, cx - 1):
            self.named_1[name] = (cy + 2, cx - 2)
            t = cy + 2, cx - 2

        elif i == (cy - 1, cx + 1):
            self.named_1[name] = (cy - 2, cx + 2)
            t = cy - 2, cx + 2

        elif i == (cy, cx + 1):
            self.named_1[name] = (cy, cx + 2)
            t = cy, cx + 2

        elif i == (cy, cx - 1):
            self.named_1[name] = (cy, cx - 2)
            t = (cy, cx - 2)
        self.location_list_2.remove(i)
        self.location_update(name, t[1], t[0])
        self.plays = 1
        # ty = self.named_1[name][0]

        # tx = self.named_1[name][1]
        self.remove_piece(i)
        self.dead.append(i)
        # print("rem?")

        self.turn = 'b'
        self.addpiece(name, self.photo_w, t[0], t[1])

    def can_jump_over(self, i, cy, cx, y, x, name):
        #  if 'player1' in  name:
        if i == (cy + 1, cx):
            self.named_1[name] = (cy + 2, cx)
            t = cy + 2, cx

        elif i == (cy - 1, cx):
            self.named_1[name] = (cy - 2, cx)
            t = cy - 2, cx

        elif i == (cy + 1, cx + 1):
            self.named_1[name] = (cy + 2, cx + 2)
            t = cy + 2, cx + 2

        elif i == (cy - 1, cx - 1):
            self.named_1[name] = (cy - 2, cx - 2)
            t = cy - 2, cx - 2

        elif i == (cy + 1, cx - 1):
            self.named_1[name] = (cy + 2, cx - 2)
            t = cy + 2, cx - 2

        elif i == (cy - 1, cx + 1):
            self.named_1[name] = (cy - 2, cx + 2)
            t = cy - 2, cx + 2

        elif i == (cy, cx + 1):
            self.named_1[name] = (cy, cx + 2)
            t = cy, cx + 2

        elif i == (cy, cx - 1):
            self.named_1[name] = (cy, cx - 2)
            t = (cy, cx - 2)

        self.location_update(name, t[1], t[0])
        self.plays = 1

    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0, 0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size / 2)
        y0 = (row * self.size) + int(self.size / 2)
        self.canvas.coords(name, x0, y0)

    def location_update(self, name, x, y):
        if 'player1' in name:
            ind = None
            if '_1' in name:
                self.location1_1 = (y, x)
                self.named_1[name] = (y, x)
                ind = 0
            elif '_2' in name:
                self.location1_2 = (y, x)
                self.named_1[name] = (y, x)
                ind = 1
            elif '_3' in name:
                self.location1_3 = (y, x)
                self.named_1[name] = (y, x)
                ind = 2
            elif '_4' in name:
                self.location1_4 = (y, x)
                self.named_1[name] = (y, x)
                ind = 3
            elif '_5' in name:
                self.location1_5 = (y, x)
                self.named_1[name] = (y, x)
                ind = 4
            elif '_6' in name:
                self.location1_6 = (y, x)
                self.named_1[name] = (y, x)
                ind = 5
            temp = []
            for k, v in self.named_1.items():
                temp.append(v)
                #     print(v)
            #    print(temp)
            self.location_list_1 = []
            for elem in temp:
                #   print('e ', elem)
                self.location_list_1.append(elem)




        elif 'player2' in name:
            ind = None
            print("fc x", x)
            if type(x) == tuple:
                x = x[1]
            if '_1' in name:
                self.location2_1 = (y, x)
                self.named_2[name] = (y, x)
                ind = 0
            elif '_2' in name:
                self.location2_2 = (y, x)
                self.named_2[name] = (y, x)
                ind = 1
            elif '_3' in name:
                self.location2_3 = (y, x)
                self.named_2[name] = (y, x)
                ind = 2
            elif '_4' in name:
                self.location2_4 = (y, x)
                self.named_2[name] = (y, x)
                ind = 3
            elif '_5' in name:
                self.location2_5 = (y, x)
                self.named_2[name] = (y, x)
                ind = 4
            elif '_6' in name:
                self.location2_6 = (y, x)
                self.named_2[name] = (y, x)
                ind = 5
            temp = []
            for k, v in self.named_2.items():
                temp.append(v)
            self.location_list_2 = []
            for elem in temp:
                self.location_list_2.append(elem)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2

        for row in range(self.rows):
            color = self.color1
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1

        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


# image comes from the silk icon set which is under a Creative Commons
# license. For more information see http://www.famfamfam.com/lab/icons/silk/

black = "bcirc.png"
white = "wcirc.gif"
background = "black.gif"


def onPressToMove(self, event):  # get initial location of object to be moved
    winX = event.x - self.canvas.canvasx(0)
    winY = event.y - self.canvas.canvasy(0)
    self.dragInfo["Widget"] = self.canvas.find_closest(event.x, event.y, halo=5)[0]

    # reset the starting point for the next move
    self.dragInfo["xCoord"] = winX
    self.dragInfo["yCoord"] = winY


if __name__ == "__main__":
    root = tk.Tk()
    background = tk.PhotoImage(file=background)
    background = background.subsample(13, 13)
    player1 = tk.PhotoImage(file=white)
    player1 = player1.subsample(25, 25)
    player2 = tk.PhotoImage(file=black)
    player2 = player2.subsample(8, 8)
    board = GameBoard(root, {"player1_1": (4, 2), "player1_2": (4, 3), "player1_3": (4, 4), "player1_4": (4, 5),
                             "player1_5": (5, 3), "player1_6": (5, 4)},
                      {"player2_1": (8, 3), "player2_2": (8, 4), "player2_3": (9, 2), "player2_4": (9, 3)
                          , "player2_5": (9, 4), "player2_6": (9, 5)}, player1, player2)

    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)

    board.addpiece("player1_1", player1, 4, 2)
    board.addpiece("player1_2", player1, 4, 3)
    board.addpiece("player1_3", player1, 4, 4)
    board.addpiece("player1_4", player1, 4, 5)
    board.addpiece("player1_5", player1, 5, 3)
    board.addpiece("player1_6", player1, 5, 4)
    board.addpiece("player2_1", player2, 8, 3)
    board.addpiece("player2_2", player2, 8, 4)
    board.addpiece("player2_3", player2, 9, 2)
    board.addpiece("player2_4", player2, 9, 3)
    board.addpiece("player2_5", player2, 9, 4)
    board.addpiece("player2_6", player2, 9, 5)
    board.addpiece("background", background, 13, 0)
    board.addpiece("background0", background, 13, 1)
    board.addpiece("background1", background, 13, 2)
    board.addpiece("background2", background, 13, 5)
    board.addpiece("background3", background, 13, 6)
    board.addpiece("background4", background, 13, 7)
    board.addpiece("background5", background, 0, 7)
    board.addpiece("background6", background, 0, 6)
    board.addpiece("background7", background, 0, 5)
    board.addpiece("background8", background, 0, 2)
    board.addpiece("background9", background, 0, 1)
    board.addpiece("background10", background, 12, 0)
    board.addpiece("background11", background, 12, 1)
    board.addpiece("background12", background, 12, 6)
    board.addpiece("background13", background, 12, 7)
    board.addpiece("background14", background, 1, 0)
    board.addpiece("background15", background, 1, 1)
    board.addpiece("background16", background, 1, 6)
    board.addpiece("background17", background, 1, 7)
    board.addpiece("background18", background, 0, 0)
    board.addpiece("background19", background, 11, 0)
    board.addpiece("background20", background, 11, 7)
    board.addpiece("background21", background, 2, 0)
    board.addpiece("background22", background, 2, 7)
    root.mainloop()
