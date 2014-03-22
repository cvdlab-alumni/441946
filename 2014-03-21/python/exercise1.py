from pyplasm import *
raggio = 0.3
#Function to translate color range from [0,1] to [0,255]
def RGB(color):
	return Color4f([color[0]/255.0,
					color[1]/255.0,
					color[2]/255.0,
					1.0])
#Function to creare a circle
def circle(r):
	def circle0(p):
		alpha= p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0

#Function that aligns to center a figure, given another figure for reference point 
def AlignToCenter(figures):
	xFrom = UKPOL(figures[0])[0][2][0]
	yFrom = UKPOL(figures[0])[0][1][1]
	xTo = UKPOL(figures[1])[0][2][0]
	yTo = UKPOL(figures[1])[0][1][1]
	#To use a reference point different to figure to translate if provided
	if(len(figures)>2): 
		figureTo = figures[2] 
	else :
		figureTo = figures[1]
	return T([1,2])([(xFrom - xTo)/2,(yFrom-yTo)/2])(figureTo)

#To create a 2D column given radius,center
def colonna2D(centro = [0,0]):
	return JOIN(T([1,2])([centro[0],centro[1]])(MAP(circle(raggio))(INTERVALS(2*PI)(32))))


floor1 = PROD([Q(8.4),Q(14.4)])
floor1 = COLOR(RGB([251,240,183]))(floor1)

floor2 = PROD([Q(7.8),Q(13.8)])
floor2 = COLOR(RGB([255,184,195]))(floor2)
floor2 = T(3)(0.1)(floor2)
floor2 = AlignToCenter([floor1,floor2])

floor3 = PROD([Q(7.2),Q(13.2)])
floor3 = COLOR(RGB([110,207,235]))(floor3)
floor3 = T(3)(0.2)(floor3)
floor3 = AlignToCenter([floor1,floor3])

floor4 = PROD([Q(6.6),Q(12.6)])
floor4 = COLOR(RED)(floor4)
floor4 = T(3)(0.3)(floor4)
floor4 = AlignToCenter([floor1,floor4])
	
floor5 = PROD([Q(6),Q(12)])
floor5 = COLOR(RGB([248,210,215]))(floor5)
floor5s = AlignToCenter([floor1,floor5])
floor5c = T(3)(0.4)(floor5s)


columns = PROD([Q(5.2),Q(11.4)])
columns = AlignToCenter([floor1,columns])

floor6 = DIFFERENCE([floor5,T([1,2])([0.8,1])(PROD([Q(4.4),Q(10)]))])

floor6 = COLOR(RGB([197,232,235]))(floor6)
floor6 = T(3)(2)(floor6)
floor6 = AlignToCenter([floor1,floor5,floor6])

verticiBaseColonne = UKPOL(S(3)(0)(columns))[0]

# print(verticiBaseColonne) 
distanzaColonneX = (verticiBaseColonne[2][0]-verticiBaseColonne[1][0]) / 5
distanzaColonneY = (verticiBaseColonne[1][1]-verticiBaseColonne[0][1]) / 12

partenzaX = UKPOL(columns)[0][0][0]
arrivoX = UKPOL(columns)[0][2][0]
partenzaY = UKPOL(columns)[0][0][1]
arrivoY = UKPOL(columns)[0][1][1]

colonneB = []
colonneA = []
for i in range(12):
	colonneB = colonneB + [T(3)(0.4)(colonna2D([partenzaX,partenzaY+distanzaColonneY * i]))]
	colonneB = colonneB + [T(3)(0.4)(colonna2D([arrivoX,partenzaY+distanzaColonneY * i]))]
for i in range(6):
 	colonneB = colonneB + [T(3)(0.4)(colonna2D([partenzaX+distanzaColonneX * i,arrivoY]))]
 	colonneB = colonneB + [T(3)(0.4)(colonna2D([partenzaX+distanzaColonneX * i,partenzaY]))]

for i in colonneB:
	colonneA = colonneA + [T(3)(1.6)(i)]

# for x in colonne: T(3)(0.4)(colonne)
two_and_half_model = STRUCT(colonneB + colonneA +  [floor1,floor2,floor3,floor4,floor5c,floor6])

#VIEW(two_and_half_model)
# VIEW(SKEL_1(building))
# VIEW(T(1)(1)(colonna2D(0.1)))