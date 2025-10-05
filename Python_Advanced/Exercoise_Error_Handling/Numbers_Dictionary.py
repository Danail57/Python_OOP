numbers_dictionary = {}

while (key := input()).lower() != 'Search':
    try:
        value = int(input())
        numbers_dictionary[key] = value
    except ValueError:
        print("The variable number must be an integer")

while (key := input()).lower() != 'Remove':
    try:
        print(numbers_dictionary[key])
    except KeyError:
        print("Number does not exist in dictionary")

while (key := input()).lower() != 'End':
    try:
        del numbers_dictionary[key]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
