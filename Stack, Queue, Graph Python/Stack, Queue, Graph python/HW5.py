#HW 5
#Due Date: 12/13/2019, 11:59PM 
########################################
#
# Name: Michael Castell
# Collaboration Statement:
#
########################################

# ---Copy your Queue code from lab 8 and your Stack code from HW3 here (you can remove their comments)  
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__


class Stack:
    def __init__(self):
        self.top = None
        self.count=0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return (self.top == None)

    def __len__(self): 
        # YOUR CODE STARTS HERE
        return self.count

    def push(self,value):
        # YOUR CODE STARTS HERE
        new_node = Node(value)
        temp = self.top
        self.top = new_node
        self.top.next = temp
        self.count += 1
             
    def pop(self):
        # YOUR CODE STARTS HERE
        if(self.top == None):
            return None
        else:
            temp = self.top.value
            self.top = self.top.next
            self.count -= 1
            return temp

    def peek(self):
        # YOUR CODE STARTS HERE
        return self.top.value


class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        # --- Your code starts here
        if(self.count > 0):
            return False
        return True

    def enqueue(self, x):
        # --- Your code starts here
        new_node = Node(x)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            self.count = self.count + 1
        else:
            temp = self.head
            while(not(temp.next == None)):
                temp = temp.next
            temp.next = new_node
            self.tail = new_node
            self.count = self.count + 1

    def contains(self, item):
        if(self.head == None):
            return False
        temp = self.head
        while(temp.next is not None):
            if(temp.value == item):
                return True
            temp = temp.next
        return False


    def dequeue(self):
        # --- Your code starts here
        if(self.head == None):
            return 'Queue is empty'
        temp = self.head
        if(self.head.next == None):
            self.count = 0
            self.head = None
            self.tail = None
            return temp.value
        self.head = self.head.next
        self.count = self.count - 1
        return temp.value

    def __len__(self):
        # --- Your code starts here
        return self.count

    def reverse(self): 
        # --- Your code starts here
        if(not(self.head == None)):
            if(not(self.head.next == None)):
                temp = self.head
                self.tail = self.head
                loop_num = self.count
                for i in range(0, loop_num):
                    temp_head = self.head
                    self.head = Node(temp.value)
                    self.head.next = temp_head
                    temp = temp.next
                for i in range(0, loop_num):
                    temp = self.head
                    while(not(temp.next.next == None)):
                        temp = temp.next
                    temp.next = None




#----- HW5 Graph code     
class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start):
        '''
            >>> g1 = {'A': ['B','D','G'],
            ... 'B': ['A','E','F'],
            ... 'C': ['F'],
            ... 'D': ['A','F'],
            ... 'E': ['B','G'],
            ... 'F': ['B','C','D'],
            ... 'G': ['A','E']}
            >>> g=Graph(g1)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'G', 'E', 'F', 'C']
        '''
        # YOUR CODE STARTS HERE
        temp = Queue()
        visited = []

        temp.enqueue(start)
        visited.append(start)

        while(not temp.isEmpty()):
            start = temp.dequeue()
            for i in range(len(self.vertList[start])):
                unvisited = self.vertList[start].copy()
                unvisited.sort()
                if(not unvisited[i][0] in visited):
                    visited.append(unvisited[i][0])
                    temp.enqueue(unvisited[i][0])
        
        return visited
        

    def dfs(self, start):
        '''
            >>> g1 = {'A': ['B','D','G'],
            ... 'B': ['A','E','F'],
            ... 'C': ['F'],
            ... 'D': ['A','F'],
            ... 'E': ['B','G'],
            ... 'F': ['B','C','D'],
            ... 'G': ['A','E']}
            >>> g=Graph(g1)
            >>> g.dfs('A')
            ['A', 'B', 'E', 'G', 'F', 'C', 'D']
        '''
        # OUR CODE STARTS HERE
        temp = Stack()
        visited = []
        temp.push(start)

        while(not temp.isEmpty()):
            print(temp)
            start = temp.pop()
            if(not start in visited):
                visited.append(start)
                unvisited = self.vertList[start].copy()
                unvisited.sort(reverse=True)
                for x in range(len(self.vertList[start])):
                    if(unvisited[x][0] not in visited):
                        temp.push(unvisited[x][0])

        return visited
