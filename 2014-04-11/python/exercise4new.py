from exercise3new import * 


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

# VIEW(STRUCT([asta,base,camera]))

# lampione = STRUCT([asta,base,camera])


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
shelter = STRUCT([colonne,tetto,inmezzo,arco])


pair_x = [T(1)(0.1), CUBOID([0.1,0.3,4]) ]
panca = STRUCT(NN(3)(pair_x))
VIEW(panca)
# VIEW(shelter)




