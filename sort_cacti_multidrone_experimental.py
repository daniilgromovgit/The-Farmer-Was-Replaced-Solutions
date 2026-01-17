def plant_cacti_multidrone():
	world_size = get_world_size()
	for _ in range(world_size):
		if get_ground_type() != Grounds.Soil:
			till() 
		plant(Entities.Cactus)
		move(North)
def sort_cacti_axis(axis):
	def sort_cacti():
		AXIS = {
		'horizontal': (East, West, get_pos_x),
		'vertical': (North, South, get_pos_y),
		}
		forward, backward, get_pos = AXIS[axis]
		world_size = get_world_size()
		start = 0
		end = world_size - 1
		direction = forward
		swapped = True
		while swapped and end > start:
			swapped = False
	
			if direction == forward:
				while get_pos() < end:
					if measure() > measure(forward):
						swap(forward)
						swapped = True
					move(forward)
				end -= 1
				direction = backward
	
			else:
				while get_pos() > start:
					if measure() < measure(backward):
						swap(backward)
						swapped = True
					move(backward)
				start += 1
				direction = forward
	return sort_cacti
STAGE = 'planting'
clear()
set_world_size(max_drones() - 1)
while True:
	if STAGE == 'planting':
		if num_drones() == max_drones():
			plant_cacti_multidrone()
			while num_drones() != 1:
				pass
			STAGE = 'vertical_sort'
		spawn_drone(plant_cacti_multidrone)
		move(East)
	elif STAGE == 'vertical_sort':
		if num_drones() == max_drones():
			sort_cacti_axis('vertical')
			while num_drones() != 1:
				pass
			STAGE = 'horizontal_sort'
		spawn_drone(sort_cacti_axis('vertical'))
		move(East)
	elif STAGE == 'horizontal_sort':
		if num_drones() == max_drones():
				sort_cacti_axis('horizontal')
				while num_drones() != 1:
					pass
				harvest()
				STAGE = 'planting'
		spawn_drone(sort_cacti_axis('horizontal'))
		move(North)
			
