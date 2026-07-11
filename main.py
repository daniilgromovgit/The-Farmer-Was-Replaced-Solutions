import single_drone
PLANTS = [

	Entities.Bush,
	Entities.Carrot,
	Entities.Grass,
]
while True:
	single_drone.farm_diagonal_pattern(PLANTS)