clear()
set_world_size(max_drones() - 1)
def farm_pumpkins_multidrone():
	dead_map = []
	world_size = get_world_size()
	for _ in range(world_size):
		x, y = get_pos_x(), get_pos_y()
		use_item(Items.Water)
		if get_ground_type() != Grounds.Soil:
			till()
		if not can_harvest():
			plant(Entities.Pumpkin)
			dead_map.append((x, y))
		move(North)
	while dead_map:
		x, y = dead_map.pop(0)
		move_to_position(x, y)
		if not can_harvest():
			plant(Entities.Pumpkin)
			dead_map.append((x, y))
		
while True:
	if num_drones() == max_drones():
		farm_pumpkins_multidrone()
		while num_drones() != 1:
			pass
		harvest()
	spawn_drone(farm_pumpkins_multidrone)
	move(East)
