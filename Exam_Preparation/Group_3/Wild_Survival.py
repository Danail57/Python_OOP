from collections import deque

bee_groups = deque(map(int, input().split(" ")))
bee_eaters_groups = deque(map(int, input().split(" ")))

while bee_eaters_groups and bee_groups:
    attackers = bee_eaters_groups.popleft()
    bees = bee_groups.pop()

    while bees > 0 and attackers > 0:
        if bees >= 7:
            bees -= 7
            attackers -= 1
        else:
            bees = 0
            break

    if bees == 0 and attackers > 0:
        bee_eaters_groups.appendleft(attackers)
    elif attackers == 0 and bees > 0:
        bee_groups.append(bees)

print("The final battle is over!")

if not bee_groups and not bee_eaters_groups:
    print("But no one made it out alive!")
elif bee_groups:
    print("Bee groups left: " + ", ".join(map(str, bee_groups)))
elif bee_eaters_groups:
    print("Bee-eater groups left: " + ", ".join(map(str, bee_eaters_groups)))
