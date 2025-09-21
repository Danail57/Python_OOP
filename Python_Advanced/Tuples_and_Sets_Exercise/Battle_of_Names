odd_set = set()
even_set = set()

number = int(input())
for i in range(1, number + 1):
    name = input()
    current_number = sum(ord(ch) for ch in name) // i

    if current_number % 2 == 0:
        even_set.add(current_number)
    else:
        odd_set.add(current_number)

odd_sum = sum(odd_set)
even_sum = sum(even_set)


if odd_sum == even_sum:
    result = odd_set | even_set
elif odd_sum > even_sum:
    result = odd_set - even_set
else:
    result = odd_set ^ even_set

print(", ".join(str(x) for x in result))
