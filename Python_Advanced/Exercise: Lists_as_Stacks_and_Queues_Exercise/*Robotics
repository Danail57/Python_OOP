import datetime
from datetime import timedelta
from collections import deque

robots_data = input().split(';')
robots = []

for robot in robots_data:
    name, process_time = robot.split('-')
    robots.append([name, int(process_time), 0])

starting_time = input()
current_time = datetime.datetime.strptime(starting_time, "%H:%M:%S")

products = deque()
product = input()

while product != 'End':
    products.append(product)
    product = input()

while products:
    current_time += timedelta(seconds=1)

    for robot in robots:
        if robot[2] > 0:
            robot[2] -= 1
    product = products.popleft()
    assigned = False

    for robot in robots:
        if robot[2] == 0:
            robot[2] = robot[1]
            print(f"{robot[0]} - {product} [{current_time.strftime('%H:%M:%S')}]")
            assigned = True
            break
    if not assigned:
        products.append(product)
