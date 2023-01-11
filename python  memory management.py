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
def create_cycle():
 
    # create a list x
    x = [ ]
 
    # A reference cycle is created
    # here as x contains reference to
    # to self.
    x.append(x)
  
'''create_cycle()
Because create_cycle() creates an object x which refers to itself, the object x will not automatically be freed when the function returns. This will cause the memory that x is using to be held onto until the Python garbage collector is invoked.
'''
x = []
x.append(l)
x.append(2)
 
# delete the list from memory or
# assigning object x to None(Null)
del x
# x = None
'''The reference count for the list created is now two. However, since it cannot be reached from inside Python and cannot possibly be used again, it is considered garbage. In the current version of Python, this list is never freed. 
 '''
# loading gc
import gc
 
# get the current collection
# thresholds as a tuple
print("Garbage collection thresholds:",
                    gc.get_threshold())
#output:Garbage collection thresholds: (700, 10, 10) 
'''Here, the default threshold on the above system is 700. This means when the number of allocations vs. the number of deallocations is greater than 700 the automatic garbage collector will run.'''
