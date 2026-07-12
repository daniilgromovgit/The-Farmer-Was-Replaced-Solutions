import constants
import single_drone

while True:
	single_drone.farm_diagonal_pattern(constants.DEFAULT_PLANTS)
	single_drone.get_pumpkin()
	single_drone.get_energy()
