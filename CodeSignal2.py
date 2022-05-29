#Sol 1
def solution(sequence):
    d = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }

    stack = []
    
    for c in sequence:
        if c in d.keys():
            stack.append(c)
        elif c in d.values() and len(stack) != 0:
            k = stack[-1]
            if c == d[k]:
                stack.pop()
        else:
            return False
    if not len(stack):
        return True
    return False
  
  #Sol2
  #There is a bug 
  def solution(commands):

    maxSize = 10
    queue = [0] * maxSize
    answer = []
    head = 0
    tail = 0
    currentSum = 0

    for i in range(len(commands)):
        if commands[i] == '-':
            currentSum -= queue[head]
            head += 1
        else:
            value = 0
            for j in range(1, len(commands[i])):
                value = value * 10 + ord(commands[i][j]) - ord('0')
            currentSum += value
            queue[tail] = value
            tail = (tail + 1) % maxSize
        answer.append(currentSum)

    return answer
  
  
  #fixing 
  '''
  Given an array of commands, return an array of sums of all elements in the queue after each operation the machine performs.
  '''
  def solution(commands):

    maxSize = len(commands)
    queue = [0] * maxSize
    answer = []
    head = 0
    tail = 0
    currentSum = 0

    for i in range(len(commands)):
        if commands[i] == '-':
            currentSum -= queue[head]
            head += 1
        else:
            value = 0
            for j in range(1, len(commands[i])):
                value = value * 10 + ord(commands[i][j]) - ord('0')
            currentSum += value
            queue[tail] = value
            tail = (tail + 1) % maxSize
        answer.append(currentSum)

    return answer

  
 #Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def solution(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        ...

    def remove():
        ...

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans
def insert(x):
        left.push(x)
        

    def remove():
        right = Stack()
        while not left.isEmpty():
            a = left.pop()
            right.push(a)
        k = right.pop()
        while not right.isEmpty():
            b = right.pop()
            left.push(b)
  
  
  
  
  
