OPPOSITE = {
	East: West,
	West: East,
	North: South,
	South: North
}

def abs(value):
		if value < 0:
			return -value
		return value

def get_state():
	return {
		'x': get_pos_x(),
		'y': get_pos_y(),
		'world_size': get_world_size()
	}

def move_axis(distance, forward, backward, world_size):
	if distance <= world_size // 2:
		for _ in range(distance):
			move(forward)
	else:
		for _ in range(world_size - distance):
			move(backward)

def move_to_position(target_x, target_y, state):	
	dx = (target_x - state['x']) % state['world_size']
	dy = (target_y - state['y']) % state['world_size']
	move_axis(dx, East, OPPOSITE[East], state['world_size'])
	move_axis(dy, North, OPPOSITE[North], state['world_size'])
