import numpy as np
import sys
import time
import random

# Return 1000 random integers from the “discrete uniform” distribution
# in the “half-open” interval [0, 500)
#seq = np.random.randint(0, 500, size=1000)

# Modify a sequence in-place by shuffling its contents
#np.random.shuffle(a)

list_of_lists = [[], [], [], [], [], [], []]
for i in range (0, 6):
        for j in range (0, 10**(i+1)):
                item = random.randint(0, 10**(i+1))
                list_of_lists[i].append(item)

#########################

def heapsort(a):
        #converts to heap
        length = len(a) - 1
        lowestParent = length /2
        for i in range (lowestParent, -1, -1):
                moveDown(a, i, length)

        #makes heap into sorted array
        for i in range(length, 0, -1):
                if a[0] > a[i]:
                        exch(a, 0, i)
                        moveDown(a, 0, i-1)
        

def moveDown(a, lo, hi):
        largest = 2 * lo + 1
        while largest <= hi:
                #basically the value on right is less than on left
                if (largest < hi) and (a[largest] < a[largest + 1]):
                        largest +=1

                #if the value on right is larger than value above
                if a[largest] > a[hi]:
                        exch(a, largest, hi)
                        #move the above down to the value on the right position
                        hi = largest
                        largest = 2 * hi + 1
                else:           

                        return


##########################
rando = random.Random(42)
def quicksort3way(a):
        partition3way(a,0,len(a))

def partition3way(a, start, stop):
        if stop - start < 2:
                return
        key = a[rando.randrange(start,stop)]
        e = u = start
        g = stop
        while u < g:
                if a[u] < key:
                        exch(a,u,e)
                        e = e +1
                        u = u +1
                elif a[u] == key:
                        u = u + 1
                else:
                        g = g - 1
                        exch(a,u,g)


#########################               

def exch(a, i, j):
        swap = a[i]
        a[i] = a[j]
        a[j] = swap

def partition(a, lo, hi):
        i = lo + 1
        j = hi
        while 1:
                while i <= j and a[i] <= a[lo]:
                        i += 1
                while i <= j and a[lo] <= a[j]:
                        j -= 1
                if i > j:
                        break
                exch(a, i, j)
        exch(a, lo, j)
        return j

def quick(a, lo, hi):
        if hi <= lo:
                return
        j = partition(a, lo, hi)
        quick(a, lo, j-1)
        quick(a, j+1, hi)

def quicksort(a):
        random.shuffle(a)
        quick(a, 0, len(a)-1)

##################################

def merge(a, aux, lo, mid, hi):
        for k in range(lo, hi+1):
                aux[k] = a[k]
        i = lo
        j = mid + 1
        for k in range(lo, hi+1):
                if i > mid:
                        a[k] = aux[j]
                        j += 1
                elif j > hi:
                        a[k] = aux[i]
                        i += 1
                elif aux[j] < aux[i]:
                        a[k] = aux[j]
                        j += 1
                else:
                        a[k] = aux[i]
                        i += 1

def sort(a, aux, lo, hi):
        if hi <= lo:
                return
        mid = lo + (hi-lo)/2
        sort(a, aux, lo, mid)
        sort(a, aux, mid+1, hi)
        merge(a, aux, lo, mid, hi)

def mergesort(a):
        aux = [0] * len(a)
        sort(a, aux, 0, len(a)-1)


quicksort(list_of_lists[1])
mergesort(list_of_lists[1])
quicksort3way(list_of_lists[1])
heapsort(list_of_lists[1])

string_length = 0
while __name__ == "__main__":
        string_length = int(raw_input("Enter length to test 0 through 5. Also, if you are done, enter 111: "))
        #you should use this interface style of input instead! It is better
        #string_length = int(raw_input("Enter length to test 0 through 5. Also, if you are done, enter 111: "))
        if string_length == 111:
                break
# apply mergesort
        print 'Running mergesort ...'
        start = time.clock()
        mergesort(list_of_lists[string_length])
        end = time.clock()
        print 'Elapsed time:', end-start
        print 'Results correct?', list_of_lists[string_length]!=range(string_length)
        #######################################################

# apply quicksort
        print 'Running quicksort ...'
        start = time.clock()
        quicksort(list_of_lists[string_length])
        end = time.clock()
        print 'Elapsed time:', end-start

        print 'Results correct?', list_of_lists[string_length]!=range(string_length)
########################################
# apply quicksort3way

        print 'Running quicksort3way ...'
        start = time.clock()
        quicksort3way(list_of_lists[string_length])
        end = time.clock()
        print 'Elapsed time:', end-start


        print 'Results correct?', list_of_lists[string_length]!=range(string_length)
#######################################
# apply heapsort

        print 'Running heapsort ...'
        start = time.clock()
        heapsort(list_of_lists[string_length])
        end = time.clock()
        print 'Elapsed time:', end-start


        print 'Results correct?', list_of_lists[string_length]!=range(string_length)
