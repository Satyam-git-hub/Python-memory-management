'''In the below code the variables x and y are in stack memory refering to the same object which is 10
in the heap memory'''

x = 10
y = x
  
if id(x) == id(y):
    print("x and y refer to the same object")
#Output:x and y refer to the same object
'''In the below code as x's value is changed it refers to different value in the heap memory'''
x = 10
y = x
x += 1
  
if id(x) != id(y):
    print("x and y do not refer to the same object")
#output:x and y do not refer to the same object
# Literal 9 is an object
b = 9
 
# Reference count of object 9
# becomes 0.
'''as object 9 has a reference count 0 its is deallocated from the heap memory'''
b = 4
