import pandas as pd

opd_df = pd.read_csv("../product_cost_dcos.csv")
item_id_list = []
# create memoization table of size n*W - n rows 100 , W cols 1000
rows = 9
cols = 201
t = [[-1] * cols] * rows


# memoization
def knapsack_memoization(item, dc_order_qty, cost, limit, n):
    if n == 0 or limit == 0:
        return 0
    if t[n][limit] != -1:
        return t[n][limit]
    if dc_order_qty[n - 1] < limit:
        t[n][limit] = max(
            cost[n - 1] + knapsack_memoization(item, dc_order_qty, cost, limit - dc_order_qty[n - 1], n - 1)
            , knapsack_memoization(item, dc_order_qty, cost, limit, n - 1))
        return t[n][limit]
    else:
        t[n][limit] = knapsack_memoization(item, dc_order_qty, cost, limit, n - 1)
        return t[n][limit]


item = opd_df.product_id.to_list()
dc_order_qty = opd_df.dc_order_qty.to_list()
cost = opd_df.cost_inv.to_list()
n = len(item)


def print_2d_array(t):
    if t:
        t_rows = len(t)
        for row in range(t_rows):
            print(t[row])


# profit = knapsack(item, dc_order_qty, cost, 200, n)
print_2d_array(t)

# Top down approach

