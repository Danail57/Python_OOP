clothes_quantity = list(map(int, input().split( )))
rack_capacity = int(input())
racks = 0

while clothes_quantity:
    racks += 1
    current_rack_capacity = rack_capacity
    while clothes_quantity and clothes_quantity[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_quantity.pop()

print(racks)
