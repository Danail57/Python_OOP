class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()

while True:
    print("\n--- Menu ---")
    print("1. Push item")
    print("2. Pop item")
    print("3. Peek item")
    print("4. Check if the Stack is empty")
    print("5. Exit")
    choice = input('Enter your choice: ')

    if choice == '1':
        added_number = int(input('Enter the number: '))
        stack.push(added_number)
        print('Added number: {}'.format(added_number))

    elif choice == '2':
        if not stack.is_empty():
            removed_item = stack.pop()
            print('Removed item: {}'.format(removed_item))
        else:
            print('Stack is empty. Nothing to pop.')

    elif choice == '3':
        if not stack.is_empty():
            print(f'The last stack element is: {stack.peek()}')
        else:
            print('Stack is empty. Nothing to peek.')

    elif choice == '4':
        if not stack.is_empty():
            print('The stack is not empty.')
        else:
            print('The stack is empty.')

    elif choice == '5':
        print('Exiting...')
        break

    else:
        print('Invalid choice. Try again.')
