from pyplasm import *

raggio = 0.3

def conversore(pixel): return (pixel * 14.4) / 248
def circle(r):
	def circle0(p):
		alpha= p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0

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



def RGB(color,alfa=1.0):
	return Color4f([color[0]/255.0,
					color[1]/255.0,
					color[2]/255.0,
					alfa])

def colonna2D(centro = [0,0]):
	return JOIN(T([1,2])([centro[0],centro[1]])(MAP(circle(raggio))(INTERVALS(2*PI)(32))))

def sphere1(p): 
	return [COS(p[0]), SIN(p[0])]

def domain(n):
	return INTERVALS(PI)(n)

floor1 = PROD([Q(8.4),Q(14.4)])

floor2 = PROD([Q(7.8),Q(13.8)])
floor2 = AlignToCenter([floor1,floor2])

floor3 = PROD([Q(7.2),Q(13.2)])
floor3 = AlignToCenter([floor1,floor3])

floor4 = PROD([Q(6.6),Q(12.6)])
floor4 = AlignToCenter([floor1,floor4])
	
floor5 = PROD([Q(6),Q(12)])
floor5 = AlignToCenter([floor1,floor5])

floor1_3d = PROD([floor1,Q(0.1)])
floor2_3d = PROD([floor2,Q(0.1)])
floor3_3d = PROD([floor3,Q(0.1)])
floor4_3d = PROD([floor4,Q(0.1)])
floor5_3d = PROD([floor5,Q(0.1)])

floor2_3d = T(3)(0.1)(floor2_3d)
floor3_3d = T(3)(0.2)(floor3_3d)
floor4_3d = T(3)(0.3)(floor4_3d)
floor5_3d = T(3)(0.4)(floor5_3d)

floor1_3d = COLOR(RGB([205,133,63]))(floor1_3d)
floor2_3d = COLOR(RGB([205,133,63]))(floor2_3d)
floor3_3d = COLOR(RGB([205,133,63]))(floor3_3d)
floor4_3d = COLOR(RGB([205,133,63]))(floor4_3d)
floor5_3d = COLOR(RGB([205,133,63]))(floor5_3d)

columns = PROD([Q(5.2),Q(11.4)])
columns = AlignToCenter([floor1,columns])

verticiBaseColonne = UKPOL(S(3)(0)(columns))[0]


columns = PROD([Q(5.2),Q(11.4)])
columns = AlignToCenter([floor1,columns])


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
	colonneA = colonneA + [T(3)(2.37)(i)]   #QUA ALTEZZA COLONNE
colonneTOT = []
for i in range(36):
	colonneTOT = colonneTOT + [JOIN([colonneA[i],colonneB[i]])]


colonneNew = [colonneTOT[28]]+[colonneTOT[30]]

# VIEW(STRUCT(colonneNew))
pezzo_muro_interno_piccolo = CUBOID([0.3483,2.2247,2.37])
pezzo_muro_interno_lungo = CUBOID([0.3483,3.07741,2.37])
pezzettini_muro_interno_lungo = CUBOID([0.3640,0.348,2.37])
colonnine_quadrate = CUBOID([0.3483,0.3483,2.37])

xTrasl = 2.6
yTrasl = 2.3460674157303374
xTrasl2 = xTrasl + 2.952808988764045
pezzo_muro_interno_piccolot = T([1,2])([xTrasl, yTrasl])(pezzo_muro_interno_piccolo)
pezzo_muro_interno_piccolo2t = T([1,2])([xTrasl2, yTrasl])(pezzo_muro_interno_piccolo)
pezzo_muro_interno_lungot = T([1,2])([xTrasl,9.060674157303371])(pezzo_muro_interno_lungo)
pezzo_muro_interno_lungo2t = T([1,2])([xTrasl2,9.060674157303371])(pezzo_muro_interno_lungo)
pezzettini_muro_interno_lungoxt = T([1,2])([xTrasl,9.303])(pezzettini_muro_interno_lungo)
pezzettini_muro_interno_lungoyt = T([1,2])([xTrasl2,9.303])(pezzettini_muro_interno_lungo)


colonnine_quadratext = []
colonnine_quadrateyt = []
yTraslColonnina = 4.975280898876405
for i in range(5):
	colonnine_quadratext += [T([1,2])([xTrasl,yTraslColonnina+(0.8*i)]) (colonnine_quadrate)] 
	colonnine_quadrateyt += [T([1,2])([xTrasl2,yTraslColonnina+(0.8*i)]) (colonnine_quadrate)] 

piano_base = STRUCT([floor1_3d,floor2_3d,floor3_3d,floor4_3d,floor5_3d])
interno = STRUCT([pezzo_muro_interno_piccolot,
			pezzo_muro_interno_piccolo2t,
			pezzo_muro_interno_lungot,
			pezzo_muro_interno_lungo2t]
			+ colonnine_quadrateyt + colonnine_quadratext)
interno = T([3])([0.4])(interno)

offsetY = -0.95
colonneNewRetro = T([2])([offsetY])(STRUCT(colonneNew))
colonneNewAnte =  T([2])([offsetY - 9.35])(STRUCT(colonneNew))


colonneInterne = STRUCT([colonneNewAnte,colonneNewRetro])

colonneEsterne = colonneTOT

interno = COLOR(RGB([218,189,171]))(interno)
colonneEsterne = COLOR(RGB([218,189,171]))(STRUCT(colonneEsterne))
colonneInterne = COLOR(RGB([218,189,171]))(colonneInterne)

secondo_piano = STRUCT([interno,piano_base,colonneInterne,colonneEsterne])



floor6 = DIFFERENCE([floor5,T([1,2])([0.8,1])(PROD([Q(4.4),Q(10)]))])

floor6 = COLOR(RGB([197,232,235]))(floor6)
floor6 = T(3)(2)(floor6)
floor6 = AlignToCenter([floor1,floor5,floor6])

floor_piccolo =  PROD([Q(4.5),Q(10.7)]) 
floor_piccolo = AlignToCenter([floor1,floor_piccolo])

floorGrande = PROD([Q(5.8),Q(12)])
floorGrande = AlignToCenter([floor1,floorGrande])  


rialzo_tetto = DIFFERENCE([floorGrande,floor_piccolo])
rialzo_tetto = PROD([rialzo_tetto,Q(0.3)])
rialzo_tetto = T(3)(2.77)(rialzo_tetto)
rialzo_tetto = COLOR(RGB([218,189,171]))(rialzo_tetto)


piano_rialzo_interno =  PROD([Q(3.2359),Q(9.8696)])
piano_rialzo_interno = AlignToCenter([floor1,piano_rialzo_interno])  
piano_piccolo = PROD([Q(1.923),Q(8.5696)])
piano_piccolo = AlignToCenter([floor1,piano_piccolo]) 
rialzo_interno = DIFFERENCE([piano_rialzo_interno,piano_piccolo])
rialzo_interno = PROD([rialzo_interno,Q(0.3)])
rialzo_interno = T([1,3])([0.05,2.77])(rialzo_interno)
rialzo_interno = COLOR(RGB([218,189,171]))(rialzo_interno)



rialzo_facciate = CUBOID([5.8,0.3483,0.6])
rialzo_facciate = T([1,2,3])([1.3,1.2,3.07])(rialzo_facciate)


triangolo_tetto = JOIN([Q(6.6),MK([3.3,0.8])])
triangolo2 = T(1)(0.2)(JOIN([Q(6.2),MK([3.1,0.6])]))
triangolo_tetto_3d = PROD([triangolo_tetto,Q(0.1)])
triangolo_sporgenza = DIFFERENCE([triangolo_tetto,triangolo2 ])
triangolo_sporgenza_3d = PROD([triangolo_sporgenza,Q(0.3)])

sopra_facciata_triangolo = STRUCT([triangolo_sporgenza_3d,T(3)(0.1)(triangolo_tetto_3d)])
sopra_facciata_triangolo = R([2,3])(PI/2)(sopra_facciata_triangolo)
sopra_facciata_triangolo = T([1,2,3])([0.9,1.5,3.67])(sopra_facciata_triangolo)

sopra_facciata = STRUCT([sopra_facciata_triangolo,rialzo_facciate])
sopra_facciata_front = sopra_facciata
sopra_facciata_retro = T([2])(11.65)(sopra_facciata)

sopra_facciate = STRUCT([sopra_facciata_retro,sopra_facciata_front])
sopra_facciate = COLOR(RGB([143,118,92]))(sopra_facciate)

terzo_piano = STRUCT([rialzo_tetto,rialzo_facciate,sopra_facciate,rialzo_interno])

model = STRUCT([piano_base,secondo_piano,terzo_piano])
# VIEW(STRUCT([piano_base,secondo_piano,terzo_piano]))

