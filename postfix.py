import re
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

opstack=mystack([])
operand_output_list=[]
exp="(x + y)/(z * 5)"
input_list=re.split(r"(\D)",exp)

output_list=[]
for i in input_list:
    if (i=="("):
        opstack.push(i)
    elif(i=="+"or i=="-"):
        while (opstack.top()=="*" or opstack.top()=="/" or opstack.top()=="%" or opstack.top()=="//" ):
            output_list.append(opstack.top())
            opstack.pop()
        else:
            opstack.push(i)
        
    elif(i=="*" or i=="/" or i=="%" or i=="//" ):
        while (opstack.top()=="**" ):
           output_list.append(opstack.top())
           opstack.pop()
        else:
            opstack.push(i)
    elif(i=="**"):
        opstack.push(i)
    elif(i==")"):
        while (opstack.top()!="(" ):
            if (opstack.top()!='('):
                output_list.append(opstack.top())
            
                opstack.pop()

        opstack.pop()
                
                
                
    else:
        output_list.append(i)
while (not opstack.is_empty()):
    output_list.append(opstack.top())
    opstack.pop()
output_exp=""
for i in output_list:
    output_exp+=i
print (output_exp)
    

