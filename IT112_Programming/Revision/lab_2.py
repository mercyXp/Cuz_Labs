# Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
import array

my_array = array.array('i', [1,2,3,4,5])

for i in my_array:
    print(i)
print("=========")
print(my_array[0],my_array[1],my_array[2])
print("-------")

my_array.push(4)
print(my_array)