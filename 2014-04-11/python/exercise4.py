from exercise3 import * 


base = CUBOID([1,1,0.2])
asta = CYLINDER([0.2,5])(64)
base = T([1,2])([-0.5,-0.5])(base)

lampa = JOIN([T([1,2])([-0.2,-0.2])(CUBOID([0.4,0.4])),T([1,2,3])([-0.35,-0.35,0.7])(CUBOID([0.7,0.7]))])
lampa = T(3)([5])(lampa)
lampa = SKEL_2(lampa)
lampa2 = JOIN([lampa,T([1,2,3])([-0.25,-0.25,6])(CUBOID([0.5,0.5]))])

lampa = SKEL_2(lampa)
lampa = COLOR(Color4f(1.0,1.0,1.0,0.2))(lampa)
lampa2 = SKEL_2(lampa2)

camera = STRUCT([lampa,lampa2])


base = COLOR(BLACK)(base)
asta = COLOR(RGB([193,193,187]))(asta)
camera = COLOR(RGB([219,219,49]))(camera)
lampione = STRUCT([asta,base,camera])

base = CYLINDER([0.4,0.2])(64)
colonnina = STRUCT([asta,base])
dist = 1.6150444 * 5
pair_x = [T(1)(dist/3), colonnina]
colonne = STRUCT(NN(4)(pair_x))
colonne = STRUCT([colonne]+[T([1,2])([dist+dist/3,dist/3])(colonnina)]+[T([1,2])([dist/3,dist/3])(colonnina)] )

pair_x = [T(1)(dist/3), CUBOID([dist/3-0.2,0.3,4]) ]
tramezzo = STRUCT(NN(3)(pair_x))
tramezzo = T([2,3])([-0.15,0.6])(tramezzo)
tetto = T([1,2,3])([dist/3-0.25,-0.25,5])(CUBOID([dist+0.5,dist/3+0.5,0.3]))
tramezzo_lato = T([1,2,3])([dist/3-0.2,0.1,0.6])(CUBOID([0.4,dist/3-0.2,4])) 
tramezzo_lato2 = T([1,2,3])([dist/3+dist-0.2,0.1,0.6])(CUBOID([0.4,dist/3-0.2,4])) 

inmezzo = STRUCT([tramezzo,tramezzo_lato2,tramezzo_lato])
shelter = STRUCT([colonne,tetto,inmezzo])

arco = S([1,2])([(dist+0.5)/2,(dist/3+0.5)/2])(MAP(sphere1)(domain(32)))
arco = PROD([Q(dist/3),arco])
arco = T(3)(5)(arco)
arco = R([1,2])(PI/2)(arco)
arco = T(1)(6.72)(arco)

colonne = COLOR(RGB([146,115,115]))(colonne)
tetto = COLOR(RGB([196,84,84]))(tetto)
inmezzo = COLOR(RGB([196,184,184],0.5))(inmezzo)
arco = COLOR(RGB([174,174,83]))(arco)
shelter = STRUCT([colonne,tetto,inmezzo,arco])


pair_x = [T(1)(0.1), CUBOID([0.1,0.3,4]) ]
panca = STRUCT(NN(3)(pair_x))


tronco = JOIN( [CYLINDER([1.5,0])(32),T(3)(10)(CYLINDER([0.8,0])(32))])
tronco = COLOR(RGB([150, 75,0]))(tronco)

rami = SPHERE(4)([8,8])
rami = T(3)(10)(rami)
rami = COLOR(GREEN)(rami)


albero = STRUCT([tronco,rami])



lampione = S([1,2,3])([0.2,0.2,0.2])(lampione)
fila_lampioni = [T(2)(-1),lampione]
fila_lampioni1 = STRUCT(NN(10)(fila_lampioni))

lampione = T(1)(8.5)(lampione)
fila_lampioni = [T(2)(-1),lampione]
fila_lampioni2 = STRUCT(NN(10)(fila_lampioni))

fila_lampioni_tot = STRUCT([fila_lampioni1,fila_lampioni2])

fermata_bus = S([1,2,3])([0.2,0.2,0.2])(shelter)
fermata_bus = T([1,2])([3,-10])(fermata_bus)

albero = S([1,2,3])([0.2,0.2,0.2])(albero)
fila_alberi = [T(1)(1),T(2)(-11)(albero)]
fila_alberi = STRUCT(NN(8)(fila_alberi))

alberi_in_tondo = MAP(circle(raggio))(INTERVALS(2*PI)(32))
print alberi_in_tondo

area_plan_whit_urban = STRUCT([small_area_plan,fila_lampioni_tot,fermata_bus,fila_alberi])


VIEW(area_plan_whit_urban)


