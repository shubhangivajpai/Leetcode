
#1381. Design a Stack With Increment Operation
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack1=[]
        self.maxSize=maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack1)<self.maxSize:
            self.stack1.append(x)
        

    def pop(self) -> int:
        if self.stack1:
             return self.stack1.pop()
        else:
            return -1 

    def increment(self, k: int, val: int) -> None:
        j=min(len(self.stack1),k)
        for i in range(j):
            self.stack1[i]+=val
               
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
