setx = {'green','blue'}
sety={'blue','yellow'}
print('original set elements: ')
print(setx)
print(sety)
print('\n Intersection of two said sets:')
setz = setx.intersection(sety)
print(setz)

setz2=setx.union(sety)
print(setz2)

setz3=setx.difference(sety)
print(setz3)

setz4=sety.difference(setx)
print(setz4)

setz5= setx.symmetric_difference(setx)
print(setz5)

setz6 = sety.symmetric_difference(setx)
print(setz6)