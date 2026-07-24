import constants
import utils


def farm_diagonal_pattern(plants):
	def choose_plant():
		current = utils.get_state()
		x, y = current["x"], current["y"]
		current_plant = plants[(x + y) % len(plants)]
		utils.prepare_terrain(current_plant)
		plant(current_plant)

	utils.serpentine_rectangle([
		utils.water_soil,
		utils.harvest_if_ready,
		choose_plant,
	])


def get_pumpkin():
	def plant_pumpkin():
		utils.prepare_terrain(Entities.Pumpkin)
		plant(Entities.Pumpkin)

	withered, _ = utils.serpentine_rectangle([harvest, plant_pumpkin])
	while withered:
		x, y = withered.pop(0)
		utils.move_to_position(x, y)
		if not can_harvest():
			plant_pumpkin()
			withered.append((x, y))
	harvest()


def get_energy():
	def plant_sunflower():
		utils.prepare_terrain(Entities.Sunflower)
		plant(Entities.Sunflower)

	_, sunflowers_map = utils.serpentine_rectangle([harvest, plant_sunflower, measure])

	start = get_time()
	while (
		get_time() - start
		< constants.ENTITIES_LIMITS[Entities.Sunflower]["min_growth_time"]
	):
		print("They are growing :)")
		pet_the_piggy()

	while sunflowers_map:
		max_petals = max(sunflowers_map)
		coords = sunflowers_map.pop(max_petals)
		for x, y in coords:
			utils.move_to_position(x, y)
			harvest()


def polyculture_farming():
	POLYCULTURE_PLANTS = [
		Entities.Grass,
		Entities.Bush,
		Entities.Tree,
		Entities.Carrot,
	]

	def plant_random_culture():
		current_plant = POLYCULTURE_PLANTS[
			random() * len(POLYCULTURE_PLANTS) // 1
		]
		utils.prepare_terrain(current_plant)
		plant(current_plant)

	def get_companion_and_coords():
		while "we have not found a companion":
			companion = get_companion()
			if companion:
				return companion
			harvest()  # Может и пустая лишнее действие
			plant_random_culture()

	def plant_companion():
		companion, coords = get_companion_and_coords()
		x, y = coords
		utils.move_to_position(x, y)
		utils.prepare_terrain(companion)
		utils.harvest_if_ready()
		plant(companion)

	plant_companion()
