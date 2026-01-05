def abs(value):
		if value < 0:
			return -value
		return value

def move_to_position(x, y):
	world_size = get_world_size()
	while get_pos_x() != x or get_pos_y() != y:
		dx = x - get_pos_x()
		dy = y - get_pos_y()
		if dx:
			if abs(dx) > world_size // 2:
				if dx > 0:
					dx -= world_size
				else:
					dx += world_size
			if dx > 0:
				move(East)
			else:
				move(West)
		if dy:
			if abs(dy) > world_size // 2:
				if dy > 0:
					dy -= world_size
				else:
					dy += world_size
			if dy > 0:
				move(North)
			else:
				move(South)
