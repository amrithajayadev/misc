# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:19:32 2019

@author: jayada1
Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.

Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times will not be same for a train, but we can have arrival time of one train equal to departure of the other.

In such cases, we need different platforms, i.e at any given instance of time, same platform can not be used for both departure of a train and arrival of another.

Input:
The first line of input contains T, the number of test cases. For each test case, first line will contain an integer N, the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and departure times respectively.
Note: Time intervals are in the 24-hour format(hhmm),  of the for HHMM , where the first two charcters represent hour (between 00 to 23 ) and last two characters represent minutes (between 00 to 59).

Output:
For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= A[i] < D[i] <= 2359

Example:
Input:
2
6 
0900  0940 0950  1100 1500 1800
0910 1200 1120 1130 1900 2000
3
0900 1100 1235
1000 1200 1240 

Output:
3
1
"""

#code
t = int(input())

def max_sub_arr_sum(arr, n):
    max_sum = list()
    max_sum.append(arr[0])
    
    for i in range(1,n):
        max_sum.append(max([arr[i], max_sum[i-1]+arr[i]]))
    
    return max(max_sum)
    
def find_max_platforms(arr, dep, n):
    arr.sort()
    dep.sort()
    
    sched_arr = list()
    i = 0
    j = 0
    while i < n and j < n:
        if arr[i] == dep[j]:
            i += 1
            j += 1
        elif arr[i] < dep[j]:
            sched_arr.append(1)
            i += 1
        else:
            sched_arr.append(-1)
            j += 1
        
    while i < n:
        sched_arr.append(1)
        i += 1
    while j < n:
        sched_arr.append(-1)
        j += 1
     
    print(sched_arr)
    #print(max_sub_arr_sum(sched_arr, len(sched_arr)))        

while t >0:
    n = int(input())
    arrival = list(map(int, input().strip().split()))
    departure = list(map(int, input().strip().split()))
    find_max_platforms(arrival, departure, n)
    t -= 1
    
    
"""#code
t = int(input())

def max_sub_arr_sum(arr, n):
    max_sum = list()
    max_sum.append(arr[0])
    
    for i in range(1,n):
        max_sum.append(max([arr[i], max_sum[i-1]+arr[i]]))
    
    return max(max_sum)
    
def find_max_platforms(arr, dep, n):
    arr.sort()
    dep.sort()
    
    platforms = 1
    max_platforms = 1
    i = 1
    j = 0
    while i < n and j < n:
        if arr[i] == dep[j]:
            i += 1
            j += 1
        elif arr[i] < dep[j]:
            platforms += 1
            i += 1
            
            if platforms > max_platforms:
                max_platforms = platforms
        else:
            platforms -= 1
            j += 1
     
    print(max_platforms)
    #print(max_sub_arr_sum(sched_arr, len(sched_arr)))        

while t >0:
    n = int(input())
    arrival = list(map(int, input().strip().split()))
    departure = list(map(int, input().strip().split()))
    find_max_platforms(arrival, departure, n)
    t -= 1
    
"""