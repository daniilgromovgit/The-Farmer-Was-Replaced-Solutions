set_world_size(max_drones() - 1)
STATE = 'planting'
def plant_energy():
	for _ in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()  
		plant(Entities.Sunflower)
		move(North)
def make_get_energy(target_petals):
	def get_energy():
		for _ in range(get_world_size()):
			if measure() == target_petals:
				harvest()
			move(North)
	return get_energy

while True:
	if STATE == 'planting':
		if spawn_drone(plant_energy):
			move(East)
	if get_pos_x() == 0:
		STATE = 'growing'
	if STATE == 'growing':
		start = get_time()
		while get_time() - start < 6.4:
			pass
		STATE = 'harvesting'
	if STATE == 'harvesting':
		for petal in range(15, 6, -1):
			for _ in range(get_world_size()):
				if spawn_drone(make_get_energy(petal)):
					move(East)
		STATE = 'planting'
