def run_stage(task, move_dir, next_stage, is_ready):
		spawn_drone(task)
		move(move_dir)
		if num_drones() == max_drones():
			while num_drones() != 1:
				pass
			if is_ready:
				harvest()
			return next_stage
		return None
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
STAGES = {
	'planting': (
		plant_cacti_multidrone,
		East,
		'vertical_sort',
		False
	),
	'vertical_sort': (
		sort_cacti_axis('vertical'),
		East,
		'horizontal_sort',
		False
	),
	'horizontal_sort': (
		sort_cacti_axis('horizontal'),
		North,
		'planting',
		True
	),
}
STAGE = 'planting'
clear()
set_world_size(max_drones() - 1)
while True:
	task, move_dir, next_action, is_ready = STAGES[STAGE]
	next_stage = run_stage(task, move_dir, next_action, is_ready)
	if next_stage:
		STAGE = next_stage
