import time
import matplotlib.pyplot as plt
import statistics
import random

def i_binarySearch(alist,item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return False

def r_binarySearch(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item<alist[midpoint]:
                return r_binarySearch(alist[:midpoint],item)
            else:
                return r_binarySearch(alist[midpoint+1:],item)


#initialize the lists

list_v4 = range(10000)
list_v5 = range(100000)
list_v6 = range(1000000)
list_v7 = range(10000000)

total_list = [list_v4,list_v5,list_v6,list_v7]
'''
#---- PART B -----

i_time = []
r_time = []

for i in total_list:

    t1 = time.time()
    i_binarySearch(i,1)
    t2 = time.time()-t1

    i_time.append(t2)

for i in total_list:
    t1 = time.time()
    r_binarySearch(i, 1)
    t2 = time.time() - t1

    r_time.append(t2)

print("Iterative Time Results:")
print(i_time[0],i_time[1],i_time[2],i_time[3])
print("Recursive Time Results:")
print(r_time[0],r_time[1],r_time[2],r_time[3])

plt.plot([4,5,6,7],i_time,color="red")
plt.plot([4,5,6,7],r_time,color="blue")

plt.xlabel("# of element in terms of 10^k")
plt.ylabel("Time")

plt.show()

#---- PART C -----

means_i = []
means_r = []

std_i = []
std_r = []

for l in range(len(total_list)):
    for_i = []
    for_r = []

    for i in range(50):

        t1_i = time.time()
        i_binarySearch(total_list[l], random.randint(1,len(total_list[l])-1))
        t2_i = time.time() - t1_i

        for_i.append(t2_i)

        t1_r = time.time()
        r_binarySearch(total_list[l], random.randint(1,len(total_list[l])-1))
        t2_r = time.time() - t1_r

        for_r.append(t2_r)

    print("Mean for 10 ^", l+4)

    print("For Iterative Function:")
    print("Mean:")
    print(statistics.mean(for_i))
    means_i.append(statistics.mean(for_i))

    print("Standard Deviation:")
    print(statistics.stdev(for_i))
    std_i.append(statistics.stdev(for_i))

    print("For Recursive Function")
    print("Mean:")
    print(statistics.mean(for_r))
    means_r.append(statistics.mean(for_r))

    print("Standard Deviation:")
    print(statistics.stdev(for_r))
    std_r.append(statistics.stdev(for_r))


plt.plot([4,5,6,7],means_i,color="red")
plt.plot([4,5,6,7],means_r,color="blue")
plt.plot([4,5,6,7],std_i,color="orange")
plt.plot([4,5,6,7],std_r,color="green")

plt.xlabel("# of element in terms of 10^k")
plt.ylabel("Time")

plt.show()
'''
#----- PART D ------

def improved_r_binarySearch(alist, l, r, item):
    if r >= l:
        midpoint = l + ((r - l)//2)
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] > item:
            return improved_r_binarySearch(alist, l, midpoint-1, item)
        else:
            return improved_r_binarySearch(alist, midpoint+1, r, item)
    else:
        return False

i_time_partd = []
r_time_partd = []
impr_time_partd = []

for i in total_list:

    ti_1 = time.time()
    i_binarySearch(i,1)
    ti_2 = time.time()-ti_1

    i_time_partd.append(ti_2)

    tr_1 = time.time()
    r_binarySearch(i,1)
    tr_2 = time.time()-tr_1

    r_time_partd.append(tr_2)

    timr_1 = time.time()
    improved_r_binarySearch(i,0,len(i)-1,1)
    timr_2 = time.time()-timr_1

    impr_time_partd.append(timr_2)

plt.plot([4,5,6,7],i_time_partd,color="red")
plt.plot([4,5,6,7],r_time_partd,color="blue")
plt.plot([4,5,6,7],impr_time_partd,color="orange")

plt.xlabel("# of element in terms of 10^k")
plt.ylabel("Time")

plt.show()