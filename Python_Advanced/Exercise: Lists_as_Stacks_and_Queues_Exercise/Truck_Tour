from collections import deque

petrol_stations = int(input())
stations = deque()

for _ in range(petrol_stations):
    current_fuel, distance = map(int, input().split())
    stations.append((current_fuel, distance))

start_position = 0
stops = 0

while stops < petrol_stations:
    tank_fuel = 0
    
    for current_fuel, distance in stations:
        tank_fuel += current_fuel
        if tank_fuel < distance:
            stations.rotate(-1)
            start_position += 1
            stops = 0
            break
        tank_fuel -= distance
        stops += 1
print(start_position)
