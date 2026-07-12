OPPOSITE = {East: West, West: East, North: South, South: North}
DEFAULT_PLANTS = [
	Entities.Carrot,
	Entities.Grass,
	Entities.Tree,
]
# ==========================
# ENTITIES
# ==========================
ENTITIES_LIMITS = {
	Entities.Cactus: {
		"min_size": 0,
		"max_size": 9,
		"min_growth_time": 1,
		"max_growth_time": 1,
		"valid_terrain": [Grounds.Soil],
	},
	Entities.Sunflower: {
		"min_petals": 7,
		"max_petals": 15,
		"min_growth_time": 5.6,
		"max_growth_time": 8.4,
		"valid_terrain": [Grounds.Soil],
	},
	Entities.Bush: {
		"min_growth_time": 3.2,
		"max_growth_time": 4.8,
		"drop_item": "Items.Wood",
		"valid_terrain": [Grounds.Grassland, Grounds.Soil],
	},
	Entities.Carrot: {
		"min_growth_time": 4.8,
		"max_growth_time": 7.2,
		"valid_terrain": [Grounds.Soil],
	},
	Entities.Dinosaur: {
		"min_growth_time": 0.18,
		"max_growth_time": 0.22,
		"valid_terrain": [Grounds.Grassland, Grounds.Soil],
	},
	Entities.Grass: {
		"min_growth_time": 0.5,
		"max_growth_time": 0.5,
		"valid_terrain": [Grounds.Grassland, Grounds.Soil],
	},
	Entities.Pumpkin: {
		"min_growth_time": 0.2,
		"max_growth_time": 0.38,
		"valid_terrain": [Grounds.Soil],
	},
	Entities.Tree: {
		"min_growth_time": 5.6,
		"max_growth_time": 8.4,
		"valid_terrain": [Grounds.Grassland, Grounds.Soil],
	},
}
# MAX_DRONES = max_drones()
# WORLD_SIZE_FOR_MULTIDRONE = MAX_DRONES - 1
