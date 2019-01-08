import time
import random

player_health = 100
enemy_health = 100

while player_health > 0 and enemy_health > 0:
	print('Your health ' + str(player_health))
	print('Enemy health: ' + str(enemy_health))
	print()

	attack = input ('What type of attack? (Hit or Magic) ')
	time.sleep(0.25)

	if attack == 'Hit':
		damage = random.radint(5,10)
	elif attack = 'Magic':
		damage = random.radint(1,20)
