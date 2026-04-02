def abs(value):
		if value < 0:
			return -value
		return value

def move_axis(distance, forward, backward, world_size=None):
	if world_size == None: # is недоступен
		world_size = get_world_size()
	if distance <= world_size // 2:
		for _ in range(distance):
			move(forward)
	else:
		for _ in range(world_size-distance):
			move(backward)
def move_to_position(x, y):
	OPPOSITE = {
		East: West,
		West: East,
		North: South,
		South: North
	}
	world_size = get_world_size()
	dx = (x - get_pos_x()) % world_size
	dy = (y - get_pos_y()) % world_size
	move_axis(dx, East, OPPOSITE[East], world_size)
	move_axis(dy, North, OPPOSITE[North], world_size)
