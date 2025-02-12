import array as arr
array_num = arr.array('i', [1,3,5,3,6,7,8,9,10])
print('original array: '+str(array_num))

print('Number of occcurences of the number 3 the said array'+str(array_num.count(3)))

array_num.reverse()
print('reverse the order of the items')
print(str(array_num))