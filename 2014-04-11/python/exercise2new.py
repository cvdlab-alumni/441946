from exercise1new import *

tempio = STRUCT([piano_base,secondo_piano,terzo_piano])

# VIEW(STRUCT([piano_base] + colonneTOT[0:2]))

# VIEW(DIFFERENCE([tempio,T(2)(2)(CUBOID([8.4,15,6]))]))
facciata_south = DIFFERENCE([tempio,T(2)(2)(CUBOID([8.4,15,6]))])
facciata_east = DIFFERENCE([tempio,T(1)(2)(CUBOID([8.4,15,6]))])
facciata_west = R([1,2])(PI)(facciata_east)
facciata_north = R([1,2])(PI)(facciata_south)
colonne_davanti = []

facciata_north = T([1,2])([8.4,14.4])(facciata_north)
facciata_east = T(1)(-2)(facciata_east)
facciata_west = T([1,2])([10.4,14.4])(facciata_west)

facciata_south = COLOR(RGB([190,90,64]))(facciata_south)
facciata_north = COLOR(RGB([190,90,64]))(facciata_north)
facciata_east = COLOR(RGB([228,175,162]))(facciata_east)
facciata_west = COLOR(RGB([228,175,162]))(facciata_west)

facciate = STRUCT([facciata_east,facciata_south,facciata_west,facciata_north])

# VIEW(facciate)
# colonne_davanti[0] = colonneTOT[0]
# colonne_davanti[5] = colonneTOT[1]