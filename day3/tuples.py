#creating tuple
a=(1,2,3,4,5,5,'raizada')
print(a)
print(len(a))
print(a[1:]) #slicing the tuple
#checking if an item is present
if 'raizada' in a:
    print('found it')
#adding two tupples    
b=('apple','orange')
c=a+b
print(c)
list=list(c)
list.remove('raizada')
c=tuple(list)
print(c)
