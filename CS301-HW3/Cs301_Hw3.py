import sys
import time
import matplotlib.pyplot as plt
import random
'''
*** AUTHOR : ADNAN KAAN EKIZ ***

Example Sample:

0   0   0 | 0th level
0   1   0 | 1st level
0   0   0 | 2nd level
1   0   1 | 3rd level
0   0   1 | 4th level
0   0   0 | 5th level
1   0   0 | 6th level
0   0   0 | 7th level

    0   --> represents normal road
    1   --> represents obstacle in the road

8x3 matrix = road
vertical line represents levels = loc_x
horizontal line represents lanes = loc_y
each time lane changes total cost will also change = total_cost

*** Some Keynotes ***
-> For the table in the memorization part, dictionary will be used in order to get the earlier min values

*************************** Naive Recursive Function ******************************
'''

def NaiveRecursive(road,loc_x,loc_y):

    if(loc_x == len(road)-1):
        return 0

    costs = []

    if( loc_y > 0 and road[loc_x+1][loc_y-1] == 0 ):
        costs.append( NaiveRecursive(road,loc_x+1,loc_y-1) + 1 )

    if( road[loc_x+1][loc_y] == 0 ):
        costs.append( NaiveRecursive(road,loc_x+1,loc_y) )

    if( loc_y < 2 and road[loc_x+1][loc_y+1] == 0 ):
        costs.append( NaiveRecursive(road,loc_x+1,loc_y+1) + 1 )

    return min(costs)

'''
*************************** Top Down Recursive Function ******************************
'''

def TopDownRecursive(road,x,y,memo_table):


    if( x == len(road)-1 ):
        return 0

    costs = []

    if( road[x+1][y] == 0 ):

        key = str(x+1) + "-" + str(y)
        if key in memo_table:
            costs.append( memo_table[key] )

        else:
            result = TopDownRecursive(road,x+1,y,memo_table)
            costs.append(result)

    if( y > 0 and road[x+1][y-1] == 0 ):

        key = str(x+1) + "-" + str(y-1)
        if key in memo_table:
            costs.append( memo_table[key] + 1 )

        else:
            result = TopDownRecursive(road,x+1,y-1,memo_table)
            costs.append(result + 1)

    if( y < 2 and road[x+1][y+1] == 0 ):

        key = str(x+1) + "-" + str(y+1)
        if key in memo_table:
            costs.append(memo_table[key] + 1)

        else:
            result = TopDownRecursive(road,x+1,y+1,memo_table)
            costs.append(result + 1)

    key = str(x) + "-" + str(y)
    memo_table[key] = min(costs)

    return min(costs)

'''
*************************** Iterative Function ******************************
'''

def IterativeAlgorithm(road,memory):

    ct = 0

    while( ct < len(road)-1 ):

        ct += 1

        if( ct == 1 ):

            if (road[ct][0] != 1):
                memory[ct][0] = memory[ct - 1][1] + 1

            if (road[ct][1] != 1):
                memory[ct][1] = memory[ct - 1][1]

            if (road[ct][2] != 1):
                memory[ct][2] = memory[ct - 1][1] + 1
        else:

            if( road[ct][0] != 1 ):
                memory[ct][0] = min(memory[ct-1][0], memory[ct-1][1]+1)

            if( road[ct][1] != 1 ):
                memory[ct][1] = min(memory[ct-1][0]+1, memory[ct-1][1], memory[ct-1][2]+1)

            if( road[ct][2] != 1 ):
                memory[ct][2] = min(memory[ct-1][1]+1, memory[ct-1][2])

    return min( memory[len(memory)-1] )

'''
*************************** Road Generator Function ******************************
'''

def listGenerator(pow):
    num = 5 * pow
    road = []

    for i in range(num):
        level = [0, 0, 0]
        myR = random.randint(0, 2)
        if( i != 0 ):
            level[myR] = 1
        road.append(level)

    return road

'''
*************************** Main Function ******************************

Some example arrays to show that code is working :)

myRoad = [ [0, 0, 0],
           [0, 1, 0],
           [1, 0, 0],
           [0, 1, 0],
           [1, 0, 0],
           [0, 1, 0],
           [1, 0, 0],
           [0, 1, 0],
           [1, 0, 0],
           [0, 1, 0] ]
           
myRoad = [ [0, 0, 0],
           [0, 1, 0],
           [1, 0, 0],
           [0, 1, 0],
           [0, 0, 1],
           [0, 1, 0],
           [1, 0, 0],
           [0, 1, 0],
           [0, 0, 1],
           [0, 1, 0] ]
           
myRoad = [ [0, 0, 0],
           [1, 0, 0],
           [0, 0, 1],
           [1, 0, 0],
           [0, 0, 1],
           [1, 0, 0],
           [0, 0, 1],
           [1, 0, 0],
           [0, 0, 1],
           [1, 0, 0] ]
           
'''


# DESIGNED FOR MULTIPLE RANDOM ROAD MATRICES

naiveRec = []
memRec = []
iter = []

for i in range(1,4):
    myRoad = listGenerator(i)

    memory = []
    table = {}

    for i in myRoad:
        memory.append([sys.maxsize]*3)
    memory[0][0] = 0
    memory[0][1] = 0
    memory[0][2] = 0


    t1 = time.time()
    cost = NaiveRecursive(myRoad, 0, 1)
    time1 = time.time() - t1

    t2 = time.time()
    cost2 = TopDownRecursive(myRoad, 0, 1, table)
    time2 = time.time() - t2

    t3 = time.time()
    cost3 = IterativeAlgorithm(myRoad, memory)
    time3 = time.time() - t3

    print("Total number of lane changes:", cost, cost2, cost3)

    naiveRec.append(time1)
    memRec.append(time2)
    iter.append(time3)

    arr1 = []
    arr2 = []
    arr3 = []


print(naiveRec)
print(memRec)
print(iter)

plt.plot([1,2,3],naiveRec,color="red")
plt.plot([1,2,3],memRec,color="blue")
plt.plot([1,2,3],iter,color="green")

plt.xlabel("# of element in terms of 5*k")
plt.ylabel("Time")

plt.show()


'''
# DESIGNED FOR SINGLE ROAD MATRIX ONLY
myRoad = [ [0, 0, 0],
           [1, 0, 0],
           [0, 0, 1],
           [1, 0, 0],
           [0, 0, 1],
           [1, 0, 0],
           [0, 0, 1],
           [1, 0, 0],
           [0, 0, 1],
           [1, 0, 0] ]

table = {}
memory = []

for i in myRoad:
    memory.append([sys.maxsize]*3)
memory[0][0] = 0
memory[0][1] = 0
memory[0][2] = 0

t1 = time.time()
cost = NaiveRecursive(myRoad, 0, 1)
time1 = time.time() - t1

t2 = time.time()
cost2 = TopDownRecursive(myRoad, 0, 1, table)
time2 = time.time() - t2

t3 = time.time()
cost3 = IterativeAlgorithm(myRoad, memory)
time3 = time.time() - t3

print("Total number of lane changes:", cost, cost2, cost3)
print("Naive Recursive :",cost)
print("Top-Down Recursive :",cost2)
print("Iterative :",cost3)
'''
'''
    naiveRec.append(format(time1,".2f"))
    memRec.append(format(time2,".2f"))
    iter.append(format(time3,".2f"))
'''