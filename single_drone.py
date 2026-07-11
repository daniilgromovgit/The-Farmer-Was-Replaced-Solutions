import utils
PLANTS = [

	Entities.Bush,
	Entities.Carrot,
	Entities.Grass,
]

def farm_diagonal_pattern(plants):
	def choose_plant():
		current = utils.get_state()
		x, y = current['x'], current['y']
		current_plant = plants[(x + y) % len(plants)]
		utils.prepare_terrain(current_plant)
		plant(current_plant)
	utils.serpentine_rectangle([utils.harvest_if_ready, choose_plant])

while True:
	farm_diagonal_pattern(PLANTS)