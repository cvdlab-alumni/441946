from exercise1 import * 

base1 = PROD([Q(8.4),Q(0.1)])
base2 = T([1,2])([0.3,0.1])(PROD([Q(7.8),Q(0.1)]))
base3 = T([1,2])([0.6,0.2])(PROD([Q(7.2),Q(0.1)]))
base4 = T([1,2])([0.9,0.3])(PROD([Q(6.6),Q(0.1)]))
base5 = T([1,2])([1.2,0.4])(PROD([Q(6),Q(0.1)]))
deltaX = 1
colonneSouth = []
for i in range(6):
 	colonneSouth = colonneSouth + [T([1,2])([1.2+(deltaX * i),0.5])(CUBOID([0.1,1.6]))]

VIEW(STRUCT(colonneSouth + [base1,base2,base3,base4,base5]))
#south