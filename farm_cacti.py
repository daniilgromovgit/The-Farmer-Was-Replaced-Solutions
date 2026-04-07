def farm_cacti():
	clear()
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			x, y = get_pos_x(), get_pos_y()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			move(North)
		move(East)
	while True:
		is_sorted = True
		world_size = get_world_size()
		for _ in range(world_size):
			for _ in range(world_size):
				x, y = get_pos_x(), get_pos_y()
				edge = world_size - 1
				if x < edge:	
					if measure(East) < measure():
						swap(East)
						is_sorted = False
				if y < edge:
					if measure(North) < measure():
						swap(North)
						is_sorted = False
				move(North)
			move(East)
		if is_sorted:
			harvest()
			break
