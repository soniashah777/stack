class mystack:
    
    def __init__(self,l1):
        self.list1 = l1
        
    #is empty
    def is_empty(self):
        if len(self.list1)==0:
            return True
        else:
            return False
    #push
    def push(self,ele):
        self.list1.append(ele)
       
    #top
    def top(self):
        if self.is_empty():
            return None
        else:
            return self.list1[-1]
    #pop
    def pop(self):
        if self.is_empty():
            print('List is empty')
        else:
            self.list1.remove(self.top())
      
    def display (self):
        print (self.list1)

    #running cmd    

obj=mystack([1,2,3])
obj.push(6)
obj2=mystack([23,78])
obj2.push(90)
print ("In obj")

print ("In obj2")

print(obj.pop())


