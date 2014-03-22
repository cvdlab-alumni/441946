from exercise1 import * 

base1S = PROD([Q(8.4),Q(0.1)])
base2S = T([1,2])([0.3,0.1])(PROD([Q(7.8),Q(0.1)]))
base3S = T([1,2])([0.6,0.2])(PROD([Q(7.2),Q(0.1)]))
base4S = T([1,2])([0.9,0.3])(PROD([Q(6.6),Q(0.1)]))
base5S = T([1,2])([1.2,0.4])(PROD([Q(6),Q(0.1)]))
deltaX = 1.08

fregio =  T([1,2])([1.2,2])(PROD([Q(6),Q(0.5)]))
tetto = JOIN([Q(7),MK([3.5,1.5])])
tetto = T([1,2])([0.7,2.5])(tetto)

colonneSouth = []
for i in range(6):
 	colonneSouth = colonneSouth + [T([1,2])([1.2+(deltaX * i),0.5])(CUBOID([0.6,1.6]))]

south = colonneSouth + [base1S,base2S,base3S,base4S,base5S,fregio,tetto]
#south



base1E = PROD([Q(14.4),Q(0.1)])
base2E = T([1,2])([0.3,0.1])(PROD([Q(13.8),Q(0.1)]))
base3E = T([1,2])([0.6,0.2])(PROD([Q(13.2),Q(0.1)]))
base4E = T([1,2])([0.9,0.3])(PROD([Q(12.6),Q(0.1)]))
base5E = T([1,2])([1.2,0.4])(PROD([Q(12),Q(0.1)]))
deltaX = 1.035

trave =  T([1,2])([1.2,2])(PROD([Q(12),Q(0.5)]))

#VIEW(STRUCT([base1E,base2E,base3E,base4E,base5E]))
colonneEast = []
for i in range(12):
 	colonneEast = colonneEast + [T([1,2])([1.2+(deltaX * i),0.5])(CUBOID([0.6,1.6]))]

east = colonneEast + [base1E,base2E,base3E,base4E,base5E,trave]
# VIEW(STRUCT(east))
#south


verticalNorth = R([2,3])(PI/2)(STRUCT(south))
verticalSouth = T(2)(14.4)(verticalNorth)
verticalEast =  R([1,2])(PI/2)(R([2,3])(PI/2)(STRUCT(east)))
verticalWest =  T(1)(8.4)(verticalEast)

mock_up_3D = STRUCT([two_and_half_model,verticalNorth,verticalSouth,verticalEast,verticalWest])


VIEW(mock_up_3D)