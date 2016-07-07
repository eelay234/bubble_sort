import random
import math
import time

def insertion_sort(A):
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
	    if A[j] < A[i]:
	       A[i], A[j] = A[j], A[i]

a = []
for i in range(1, 1001):
    a.append(int(random.random()*10001))

begin = time.time()
insertion_sort(a)
end = time.time()

print a
print "It took %.2f seconds" % (end - begin)
