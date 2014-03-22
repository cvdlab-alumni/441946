from exercise2 import *

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

VIEW(STRUCT([floor1_3d,floor2_3d,floor3_3d,floor4_3d,floor5_3d]))