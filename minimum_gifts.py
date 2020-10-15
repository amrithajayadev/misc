"""
Minimum Gifts
Problem Description
A Company has decided to give some gifts to all of its employees. For that, company has given some rank to each employee. Based on that rank, company has made certain rules to distribute the gifts.

The rules for distributing the gifts are:

Each employee must receive at least one gift.

Employees having higher ranking get a greater number of gifts than their neighbours.

What is the minimum number of gifts required by company?

Constraints
1 < T < 10

1 < N < 100000

1 < Rank < 10^9

Input
First line contains integer T, denoting the number of testcases.

For each testcases:

First line contains integer N, denoting number of employees.

Second line contains N space separated integers, denoting the rank of each employee.

Output
For each testcase print the number of minimum gifts required on new line.

Time Limit
1

Examples
Example 1

Input

2

5

1 2 1 5 2

2

1 2

Output

7

3

Explanation

For testcase 1, adhering to rules mentioned above,

Employee # 1 whose rank is 1 gets one gift

Employee # 2 whose rank is 2 gets two gifts

Employee # 3 whose rank is 1 gets one gift

Employee # 4 whose rank is 5 gets two gifts

Employee # 5 whose rank is 2 gets one gift

Therefore, total gifts required is 1 + 2 + 1 + 2 + 1 = 7

Similarly, for testcase 2, adhering to rules mentioned above,

Employee # 1 whose rank is 1 gets one gift

Employee # 2 whose rank is 2 gets two gifts

Therefore, total gifts required is 1 + 2 = 3

"""


# 1 2 1 5 2
def minimum_gifts(n, rank):
    gift_count = [1]*n
    for i in range(0, n-1):
        if rank[i] > rank[i + 1] or rank[i] > rank[i - 1]:
            gift_count[i] = max(gift_count[i - 1], gift_count[i + 1]) + 1
    if rank[n-1] > rank[n-2]:
        gift_count[n-1] = gift_count[n-2] + 1
    return gift_count


# res = minimum_gifts(5, [1, 2, 1, 5, 2])
# res = minimum_gifts(2, [1, 2])
# [3,2,1] --> [3,2,1]

# res = minimum_gifts(8, [3, 2, 1, 7, 6, 5, 10, 15])
res = minimum_gifts(7, [5, 4, 3, 2, 1, 2 , 3])
print(res)
print(sum(res))
