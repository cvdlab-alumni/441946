from exercise1 import * 
from random import * 

# VIEW(model)

base = CUBOID([1,1,1])
tetto = JOIN([ T([1,2])([-0.6,-0.6])(CUBOID([1.2,1.2])) , MK([0.,0.,0.3]) ])
base = COLOR(RGB([ 192,64,0]))(base)
tetto = COLOR(RGB([ 218,189,171]))(tetto) 	
casa = STRUCT([T([1,2])([-0.5,-0.5])(base),T(3)(1)(tetto)])

def centra(quadrato,lato): return T([1,2])([-(lato/2),-(lato/2)])(quadrato)

# def road(points):
# 	rapporto = 0.06
# 	base = MKPOL([points,[[1,2,3,4]],[[1]]])
# 	striscia = []

# 	primo = points[orientLine-1]
# 	secondo = points[orientLine]
# 	striscia += AA(MK)([primo,
# 					secondo,
# 					[primo[0]+rapporto,primo[1] ],
# 					[secondo[0]+rapporto,secondo[1]]  ])

# 	primo = points[orientLine-1]
# 	secondo = points[orientLine]
# 	striscia += AA(MK)([primo,
# 					secondo,
# 					[primo[0],primo[1]+rapporto ],
# 					[secondo[0],secondo[1]+rapporto]  ])

# 	primo = points[orientLine-1]
# 	secondo = points[orientLine]
# 	striscia += AA(MK)([primo,
# 					secondo,
# 					[primo[0]-rapporto,primo[1] ],
# 					[secondo[0]-rapporto,secondo[1]]  ])

# 	primo = points[orientLine-1]
# 	secondo = points[0]
# 	striscia += AA(MK)([primo,
# 					secondo,
# 					[primo[0],primo[1]-rapporto ],
# 					[secondo[0],secondo[1]-rapporto]  ])


# 	striscia = JOIN(striscia)
# 	# x_or_y = orientLine % 2
# 	# lunghezza = abs(primo[x_or_y] - secondo[x_or_y])
# 	# print (lunghezza/5)
# 	# pezzo_piccolo = CUBOID([rapporto,(float(lunghezza)/5)])
# 	# pezzo_grande = CUBOID([rapporto,(float(lunghezza)/5)*2])

# 	# if x_or_y == 1: x_or_y = 0 
# 	# else: x_or_y = 1
# 	# pezzo_piccolo = R([1,2])(PI/(1+x_or_y))(pezzo_piccolo)

# 	# linea = T(2)((lunghezza/2)/5)(pezzo_piccolo)
# 	# striscia_in_mezzo = linea

# 	# base =  COLOR(BLACK)(base)
# 	# striscia_in_mezzo =  COLOR(WHITE)(striscia_in_mezzo)
# 	carreggiata  = STRUCT([base,striscia])
# 	VIEW(carreggiata)





# def road(points):
# 	grande = CUBOID([1,1])
# 	grande = centra(grande,1)
# 	piccolo = CUBOID([0.8,0.8])
# 	piccolo = centra(piccolo,0.8)
# 	contorno = DIFFERENCE([grande,piccolo])
# 	VIEW(contorno)

case_random = []

for i in range(6):
	casa_add = S([1,2,3])([randrange(2,6),randrange(2,6),randrange(2,6)])(casa)
	case_random += [casa_add]

case_random[0] =  T([1,2])([-30,10])(case_random[0])
case_random[1] =  T([1,2])([-26,16])(case_random[1])
case_random[2] =  T([1,2])([-14,-12])(case_random[2])
case_random[3] =  T([1,2])([16,-16])(case_random[3])
case_random[4] =  T([1,2])([11,20])(case_random[4])
case_random[5] =  T([1,2])([24,30])(case_random[4])


case_random = STRUCT(case_random)
edifici = case_random
terreno = CUBOID([100,110])
terreno = T([1,2])([-50,-50])(terreno)
terreno = COLOR(RGB([102,255,102]))(terreno)
small_area_plan = STRUCT([model,edifici,terreno])

centro = [6,-6]


# VIEW(small_area_plan)




