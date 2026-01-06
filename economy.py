def get_cost_for_area(x, y, entity):
	cost = get_cost(entity)
	if not cost:
		return None
	area = x * y
	result = {}
	for item in cost:
		result[item] = cost[item] * area # {Items.Hay:256,Items.Wood:256}
	return result
