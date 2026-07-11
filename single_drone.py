import utils


def farm_diagonal_pattern(plants):
	def choose_plant():
		current = utils.get_state()
		x, y = current['x'], current['y']
		current_plant = plants[(x + y) % len(plants)]
		utils.prepare_terrain(current_plant)
		plant(current_plant)
	utils.serpentine_rectangle([utils.harvest_if_ready, choose_plant])

def get_pumpkin():
	def plant_pumpkin():
		utils.prepare_terrain(Entities.Pumpkin)
		plant(Entities.Pumpkin)
	withered = utils.serpentine_rectangle([plant_pumpkin])
	while withered:
		x, y = withered.pop(0)
		utils.move_to_position(x, y)
		if not can_harvest():
			plant_pumpkin()
			withered.append((x, y))
	harvest()
	