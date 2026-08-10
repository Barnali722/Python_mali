class Stack:
    def __init__(self):
        self.stack = [10,20,30,40]

    # Push element onto stack
    def push(self, item,index):
        self.stack.index = index
        #print(item, "pushed into stack.")
        #if len(self.stack)==0:
            #print("wrong input")
        #else :
             #self.stack[index] = self.stack.append(item)(int(input("Enter index no : ")))
        self.stack.append(item)

    # Pop element from stack
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
        else:
            print(self.stack.pop(), "popped from stack.")

    # Peek at top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Top element is:", self.stack[-1])

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Return size of stack
    def size(self):
        print("Size of stack:", len(self.stack))

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (Top to Bottom):")
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i])

# Main Program
s = Stack()

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Size")
    print("6. Check if Empty")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(s)==0:
            print("stack is empty")
        else:
            index = int(input("Enter index no : "))
            item = input("Enter element to push: ")
            print(item, "pushed into stack.")


    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        s.size()

    elif choice == 6:
        if s.is_empty():
            print("Stack is Empty.")
        else:
            print("Stack is Not Empty.")

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid Choice! Please try again.")
