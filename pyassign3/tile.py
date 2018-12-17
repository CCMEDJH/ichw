# tile.py
# Du JunHao (CCMEDJH)
# December 16, 2018
"""This program is for tile problem and its visualization.

This program provides a recursion functions to calculate
all the ways to cover a wall using specific bricks.
You can also visualize one of these methods"""


import sys, copy, time, turtle, random


def tile(wall_dic, wall, m, n, ans, mono_ans):
    """This is the function that implements the tile recursion.

    'wall_dic' is the dictionary of the wall's serial number.
    'wall' is the list of the wall's coordinate.
    'm' is the length of the brick.
    'n' is the width of the brick.
    'ans' is all kinds of the answer
    'mono_ans'is the answer you get every time you recurse."""

    if len(wall) == 0:    # If the whole wall is covered，Jump out of this recursive
        mono = copy.deepcopy(mono_ans)
        ans.append(mono)    # Stores the single answer into a list of all the answers
        stop_time = time.time()
        print('\r Using ' + str(round((stop_time - begin_time), 2)) + ' seconds. There are '
              + str(len(ans)) + ' methods.', end='', flush=True)
        # Synchronous output calculation results and medical time
        pass
    elif len(wall) != 0:    # If the wall is not covered
        # Get the smallest point on the wall
        hei_b1 = int(wall[0][0])
        wid_b1 = int(wall[0][1])
        # Test whether the new brick can be laid vertically
        compare_cross = 0
        for i in range(m):
            for t in range(n):
                if [int(hei_b1) + i, int(wid_b1) + t] in wall:
                    compare_cross += 0
                else:
                    compare_cross += 1
        if compare_cross == 0:    # You can do it vertically
            bricks = []
            for i in range(m):
                for t in range(n):
                    brick = wall_dic[hei_b1 + i, wid_b1 + t]    # Get all the coordinates of the bricks you want to lay
                    bricks.append(brick)    # Aggregate all the coordinates of a brick into a list
                    wall.remove([hei_b1 + i, wid_b1 + t])    # Remove the paved bricks from the wall
            mono_ans.append(bricks)    # Put the paved bricks into the result
            tile(wall_dic, wall, m, n, ans, mono_ans)    # Recursion
            mono_ans.remove(bricks)    # Restore the original result for the next recursion
            for i in range(m):
                for t in range(n):
                    wall.append([hei_b1 + i, wid_b1 + t])     # Remove the tiles and restore the wall
                    wall.sort()   # In order to get the smallest coordinate on the wall
        # Test whether the new brick can be laid sideways
        compare_length = 0
        for i in range(n):
            for t in range(m):
                if [int(hei_b1) + i, int(wid_b1) + t] in wall:
                    compare_length += 0
                else:
                    compare_length += 1
        if m != n and compare_length == 0:    # You can do it sideways, and rule out the situation of 'm = n'
            bricks = []
            for i in range(n):
                for t in range(m):
                    brick = wall_dic[hei_b1 + i, wid_b1 + t]     # Get all the coordinates of the bricks you want to lay
                    bricks.append(brick)    # Aggregate all the coordinates of a brick into a list
                    wall.remove([hei_b1 + i, wid_b1 + t])    # Remove the paved bricks from the wall
            mono_ans.append(bricks)     # Put the paved bricks into the result
            tile(wall_dic, wall, m, n, ans, mono_ans)    # Recursion
            mono_ans.remove(bricks)    # Restore the original result for the next recursion
            for i in range(n):
                for t in range(m):
                    wall.append([hei_b1 + i, wid_b1 + t])    # Remove the tiles and restore the wall
                    wall.sort()    # In order to get the smallest coordinate on the wall


def visual(method, m, t):
    """This function is to visualize the results.

    'method' is the tile method you choose.
    'm' is the length of the wall
    't' is the the maximum value of length or width,
    in order to draw the entire wall on the window """
    wn = turtle.Screen()
    wn.colormode(255)    # Set the fill color to RGB mode
    PEN = turtle.Turtle()
    PEN.speed(0)
    PEN.shape('circle')
    PEN.color('white')
    PEN.pensize(1)
    para = 500 / int(t)    # para is the parameter to draw the entire wall on the window
    for i in method:
        # Convert the brick serial number to coordinates
        min, max = i[0], i[-1]
        x1, x2 = para * ((int(min) - 1) % int(m)) - 250, para * ((int(max) - 1) % int(m) + 1) - 250
        y1, y2 = para * ((int(min) - 1) // int(m)) - 250, para * ((int(max) - 1)// int(m) + 1) - 250
        # Draw a brick
        PEN.up()
        PEN.goto(x1, y1)
        PEN.down()
        r, g, b = random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)
        PEN.fillcolor(r, g, b)    # Fill each brick a different color
        PEN.begin_fill()
        PEN.goto(x1, y2)
        PEN.goto(x2, y2)
        PEN.goto(x2, y1)
        PEN.goto(x1, y1)
        PEN.end_fill()

    PEN.hideturtle()
    turtle.done()
    print('Print complete')


def judge_print(all_ans):
    """Determine whether to print all results by user's input"""

    judge = input('Do you want to print all of them? (Y for Yes / N for No) ', )
    if judge == 'Y':
        t = 1    # "t" is the serial number of the method.
        for i in all_ans:
            print('Method No.' + str(t) + ' : ' + str(i))  # Output all results
            t += 1
    elif judge == 'N':
        pass
    else:
        print('You have input the wrong instruction, please try again.')
        main()


def main():
    """Main function
    Get the length and width of the wall and brick from the user
    Run the recursive tile laying function
    Then export the results and visualize them"""

    # User input the size of wall and brick:
    hei_w = input("Your wall's width:  ", )
    wid_w = input("Your wall's height:  ", )
    m = input("Your brick's width:  ", )
    n = input("Your brick's height:  ", )
    # Generates the coordinates and ordinal numbers of the wall:
    wall = []
    wall_dic = {}
    for i in range(int(wid_w)):
        for t in range(int(hei_w)):
            wall_dic[i, t] = len(wall_dic) + 1    # Give each coordinate a value for visualization
            wall.append([i, t])    # Coordinate the wall
    # Get the result by recursion:
    sys.setrecursionlimit(1000000)
    all_ans = []    # The results of all final output
    mono_ans = []    # The result of every recursion output
    global begin_time
    begin_time = time.time()
    tile(wall_dic, wall, int(m), int(n), all_ans, mono_ans)    # Run the tile function
    # Process the resulting data: print them or draw them:
    print('')    # Line feed
    print('Operation is done')
    if len(all_ans) != 0:
        judge_print(all_ans)
        choose = input('Which one do you want to see?  ', )    # Choose a method
        print('You have choose No.' + choose + ' : ' + str(all_ans[int(choose) - 1]))
        print('Printing...')
        t = max(hei_w, wid_w)
        visual(all_ans[int(choose) - 1], hei_w, t)    # Visualize the result that be chosen
    else:    # If get no result
        print('There is no feasible method, please try again')
        main()    # Run main function again


if __name__ == '__main__':
    main()
