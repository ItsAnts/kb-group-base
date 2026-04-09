import time 
start = time.time()
profits = [500, -200, 700, -150, 300, -500, 300, -400, -400] * 1000
index: int = len(profits) - 1 # 9 - 1 = 8
while index != -1:
    if profits[index] < 0:
        profits.pop(index)
    index -= 1
# print(profits)
print(time.time() - start)


start = time.time()
profits_two = [500, -200, 700, -150, 300, -500, 300, -400, -400] * 1000
index_two: int = 0
while index_two != len(profits_two):
    if profits_two[index_two] < 0:
        profits_two.pop(index_two)
    else:
        index_two = index_two + 1
# print(profits_two)
print(time.time() - start)
