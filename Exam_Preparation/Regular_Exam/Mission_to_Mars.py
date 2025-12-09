from collections import deque


solar_energy = list(map(int, input().split(", ")))
daily_distances = deque(map(int, input().split(", ")))

resources = deque([
    ("Iron", 80),
    ("Titanium", 90),
    ("Aluminium", 100),
    ("Chlorine", 60),
    ("Sulfur", 70)
])

collected = []

days = 0

while days < 7 and solar_energy and daily_distances and resources:
    days += 1

    energy = solar_energy.pop()
    distance = daily_distances.popleft()

    total = energy + distance
    resource_name, required = resources[0]

    if total >= required:
        collected.append(resource_name)
        resources.popleft()

if not resources:
    print("Mission complete! All minerals have been collected.")
else:
    print("Mission not completed! Awaiting further instructions from Earth.")

if collected:
    print("Collected resources:")
    for r in collected:
        print(r)
