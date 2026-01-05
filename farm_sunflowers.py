def farm_sunflowers():
	clear()
	petals_map = {}
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			x, y = get_pos_x(), get_pos_y()
			petals = measure()
			if petals in petals_map:
				petals_map[petals].append((x,y))
			else:
				petals_map[petals] = [(x, y)]
			move(North)
		move(East)
	start = get_time()
	while get_time() - start < 3.8:
		pass
	while petals_map:
		max_petals = max(petals_map)
		coords = petals_map.pop(max_petals)
		for x, y in coords:
			move_to_position(x, y)
			harvest()
