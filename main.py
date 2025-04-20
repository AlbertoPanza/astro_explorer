planets = ['Mercury', 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
my_commander = input('Please enter the commander name: ')
my_target = input('Please enter your target body: ').strip().capitalize()

if my_target in planets:
	print(f'\nCommander {my_commander} mission to {my_target} planner.')
else:
	print("Invalid choice! Please enter a correct planet's name.")
