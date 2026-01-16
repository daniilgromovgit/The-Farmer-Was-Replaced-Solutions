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
	flag = True
	if STATE == 'planting':
		if spawn_drone(plant_energy):
			move(East)
	if get_pos_x() == 0 and flag:
		STATE = 'pausing'
	if STATE == 'pausing':
		start = get_time()
		time_passed = 0
		while time_passed < 6.4:
			time_passed = get_time() - start
		STATE = 'harvesting'
		flag = False
	if STATE == 'harvesting':
		for petal in range(15, 6, -1):
			for _ in range(get_world_size()):
				if spawn_drone(make_get_energy(petal)):
					move(East)
		STATE = 'planting'
		flag = True
			

	
