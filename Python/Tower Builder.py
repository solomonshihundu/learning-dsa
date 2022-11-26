# PYRAMID ONE
#       *
#       * *
#       * * *
#       * * * *
#       * * * * *


def tower_one(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*",end="")
        print("\n")

rows = 5
tower_one(rows)

# PYRAMID TWO
#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5

def tower_two(rows):
    for i in range(rows):
        for j in range(i+1):
            print(j+1,end="")
        print("\n")
        
rows = 6
tower_two(rows)

#  A
#  B B
#  C C C
#  D D D D
#  E E E E E

def tower_three(rows):
    ascii_value = 65
    for i in range (rows):
        for j in range(i+1):
            alpha = chr(ascii_value)
            print(alpha,end="")

        ascii_value += 1
        print("\n")

rows = 6
tower_three(rows)


# * * * * *
# * * * *
# * * *
# * *
# *

def tower_four(rows):
    for i in range(rows,0,-1):
        for j in range(0,i):
            print("*",end=" ")

        print("\n")

rows = 6
tower_four(rows)

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def tower_five(rows):
    for i in range(rows,0,-1):
        for j in range(0,i):
            print(j+1,end=" ")

        print("\n")

rows = 6
tower_five(rows)

#        *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

def tower_six(rows):
    k = 0

    for i in range(1, rows + 1):
        for space in range (1,(rows -i) + 1):
            print(end=" ")

        while k != (2*i -1):
            print("*",end="")
            k += 1

        k = 0
        print()

rows = 6
tower_six(rows)



        
