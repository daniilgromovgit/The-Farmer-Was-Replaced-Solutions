def farm_pumpkins():
	clear()
	dead_map = []
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			x, y = get_pos_x(), get_pos_y()
			if get_ground_type() != Grounds.Soil:
				till()
			if not can_harvest():
				plant(Entities.Pumpkin)
				dead_map.append((x, y))
			move(North)
		move(East)
			
	while dead_map:
		x, y = dead_map.pop(0)
		move_to_position(x, y)
		if not can_harvest():
			plant(Entities.Pumpkin)
			dead_map.append((x, y))

	harvest()
