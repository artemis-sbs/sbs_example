import sbs
import lib.sbs_scatter.scatter as scatter

asteroidList = []

def add_asteroids(sim, g, name):
	landmark = None
	for v in g:
		asteroidID = sim.make_new_passive("behav_asteroid", "Asteroid 1")
		asteroidList.append(asteroidID)
		asteroid = sim.get_space_object(asteroidID)
		sim.reposition_space_object(asteroid, v.x, v.y, v.z)
		if landmark is None:
			landmark = sim.add_navpoint(v.x, v.y+100,v.z, name, "yellow");



########################################################################################################
def  HandleScriptStart(sim):
	print("Script start ")
	# playerID will be a NUMBER, a unique value for every space object that you create.
	playerID = sim.make_new_player("behav_playership", "Battle Cruiser")
	sbs.assign_player_ship(playerID)


	# making a bunch of asteroids
	add_asteroids(sim, scatter.line(10, -2000,0,0, 2200,0, 1000,True), "line RND")
	add_asteroids(sim, scatter.arc(20, -2000,0,0, 500, 0, 45,False), "line RND")
	add_asteroids(sim, scatter.ring(4,4, -2000,0,-1000, 800, 100, 0, 160,True), "ring rnd")
	add_asteroids(sim, scatter.ring_density([2, 4, 20], 2000,0,-1000, 800, 200, 0, 360,False), "ring density")
	add_asteroids(sim, scatter.sphere(50, 0,0,4000, 400), "sphere")
	add_asteroids(sim, scatter.sphere(50, -2000,0,2000, 200, 800, ring=True), "sphere-Ring")
	add_asteroids(sim, scatter.rect_fill(5,5,  2000,0, 4000, 500, 500, True), "Grid")
	add_asteroids(sim, scatter.box_fill(5,5,5,  -2000, 0, 4000, 500, 500,500), "Box")



def  HandleScriptTick(sim):
	print("Script tick")

########################################################################################################
def HandleConsoleObjectSelection(sim, obj_selected_id):
	pass



