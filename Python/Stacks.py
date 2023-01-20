from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    #Print out all elemnts in the stack in LIFO order
    def print(self):
        if  self.is_empty():
            print("Stack is Empty!")
            return

        while not self.is_empty():
            print(self.pop())

    def reverse_string(self,word):
        for i in word:
            self.push(i)
        
        while not self.is_empty():
            print(self.pop(),end="")

    #is_balanced("({})")
    #is_balanced("())")
    def is_balanced(self,param):
        
        para_dict = {'(':')','[':']','{':'}'}
        stack = Stack()
    
        for i in param:

            if i in para_dict.keys():
                stack.push(i)

            else:
                if stack.is_empty():
                    return False
                open_brace = stack.pop()   

                if i != para_dict[open_brace]:
                    return False

        return stack.is_empty()

        


if __name__ == '__main__':
    stack = Stack()
    #stack.push(5)
    #stack.push(9)
    #stack.push(50)
    #stack.push(17)
    #stack.print()

    #should return "91-DIVOC ereuqnoc lliw eW"
    #stack.reverse_string("We will conquere COVID-19")
    print(stack.is_balanced("({{[]}})"))
    print(stack.is_balanced("))[]}})"))
    print(stack.is_balanced("({[]}({}))"))
    print(stack.is_balanced("(]}({})"))

    