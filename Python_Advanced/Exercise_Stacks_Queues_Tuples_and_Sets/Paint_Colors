from collections import deque

color_string = deque(input().split())

main_colors = ['red', 'blue', 'yellow']
secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}

collected_colors = []

while color_string:
    first_string = color_string.popleft()
    last_string = color_string.pop() if color_string else ""

    for color in (first_string + last_string, last_string + first_string):
        if color in main_colors or color in secondary_colors:
            collected_colors.append(color)
            break
    else:
        first_sub = first_string[:-1] if first_string else ""
        last_sub = last_string[:-1] if last_string else ""

        middle = len(color_string) // 2

        if first_sub:
            color_string.insert(middle, first_sub)
        if last_sub:
            color_string.insert(middle, last_sub)

final_colors = []
for color in collected_colors:
    if color in secondary_colors:
        required = secondary_colors[color]
        if all(main in collected_colors for main in required):
            final_colors.append(color)
    else:
        final_colors.append(color)

print(final_colors)



Example Input:
re ple blu pop e pur d
r ue nge ora bl ed
d yel blu e low redd

Output
['red', 'purple', 'blue']
['red', 'blue']
['yellow', 'blue', 'red']
