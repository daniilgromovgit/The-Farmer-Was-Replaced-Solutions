plants = [Entities.Grass, Entities.Tree, Entities.Carrot]
while True:
	if get_water() < 0.5:
		use_item(Items.Water)
	if get_ground_type() != Grounds.Soil:
		till()
	for _ in range(get_world_size()):
		x, y = get_pos_x(), get_pos_y()
		if can_harvest():
			harvest()
		plant(plants[(x + y) % len(plants)])
		move(South)
	move(West)
