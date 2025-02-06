'''
Write a program that creates a list of at least 
five elements and demonstrates the use of the 
following operations: appending an element, 
inserting an element at a specified index, 
removing an element by its value, and using the pop method.
'''
def q1():
    fruits=[1,2,3,4,5,5,6,7]
    fruits.append(8)
    print(fruits)
    fruits.insert(0,0)
    print(fruits)
    fruits.remove(5)
    print(fruits)
    fruits.pop()
    print(fruits)

'''
Write a program that takes a list of 
numbers and prints the list in reverse 
order using two different methods: one 
by modifying the original list in place, 
and one by creating a new reversed list using slicing.
'''
def reverse_list():
    list1=[1,2,3,4,5,6]
    list1.reverse()
    print(list1)
    list2=[]
    for x in list1[::-1]:
        list2.append(x)
    print(list2)
'''
Write a program that accepts a list of strings 
and a target string from the user. Check if the 
target string is present in the list. If it is, 
print its index; if not, display an appropriate message.
'''
def q3():
    x=input('enter the strings: ')
    list=x.split()
    y=input('enter the target string: ')
    for j in list:
        if y==j:
            print(list.index(j))
            break
        elif y not in list:    
            print('item not found')   
'''
Write a program that finds and prints 
the maximum and minimum values from a 
list of numbers without using the built-in 
`max()` or `min()` functions.
'''

list=[12,32,123,21,1,211,3,123123,0,-20]
max=0
min=list[0]
for x in list:
    if max<x:
        max=x
    if min>x:
        min=x    
     
print(max)   
print(min)     
