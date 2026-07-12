import constants


def move_axis(distance, forward, backward, world_size):
    if distance <= world_size // 2:
        for _ in range(distance):
            move(forward)
    else:
        for _ in range(world_size - distance):
            move(backward)


def get_state():
    return {"x": get_pos_x(), "y": get_pos_y(), "size": get_world_size()}


def move_to_position(target_x, target_y):
    current = get_state()
    dx = (target_x - current["x"]) % current["size"]
    dy = (target_y - current["y"]) % current["size"]
    move_axis(dx, East, constants.OPPOSITE[East], current["size"])
    move_axis(dy, North, constants.OPPOSITE[North], current["size"])


def serpentine_rectangle(actions=None, columns=None, rows=None):
    if columns == None:
        columns = get_world_size()
    if rows == None:
        rows = get_world_size()
    path = []
    stats = {}
    for i in range(columns):
        for _ in range(rows):
            state = get_state()
            path.append((state["x"], state["y"]))
            if actions:
                for action in actions:
                    action()
                    stat = measure()
            if stat in stats:
                stats[stat].append((state["x"], state["y"]))
            else:
                stats[stat] = [(state["x"], state["y"])]
            if i % 2 == 0:
                move(North)
            else:
                move(South)
        move(East)
    return path, stats


def prepare_terrain(Entity):
    if (
        get_ground_type()
        not in constants.ENTITIES_LIMITS[Entity]["valid_terrain"]
    ):
        till()


def harvest_if_ready():
    if can_harvest():
        harvest()


def water_soil(treshold=0.7):
    if get_water() < treshold:
        use_item(Items.Water)
