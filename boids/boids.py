
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class Boids(object):
    def __init__(self, config, count=0, fly_to_middle=0, alert_distance=0, formation_flying_distance=0, formation_flying_strength=0): 
		#get config 
		self.config=config

		# setup flock
		self.boid_count=count
		self.position_limits = self.config['Boids']['position_limits']
		self.velocity_limits = self.config['Boids']['velocity_limits']
		self.fly_to_middle = fly_to_middle
		self.alert_distance = alert_distance
		self.formation_flying_distance = formation_flying_distance
		self.formation_flying_strength = formation_flying_strength
		
		self.positions  = self.new_flock(self.boid_count,
							np.array(self.position_limits[0:2]),
							np.array(self.position_limits[2:4]))
		self.velocities = self.new_flock(self.boid_count,
							np.array(self.velocity_limits[0:2]),
							np.array(self.velocity_limits[2:4]))
		
	# generate random velocities and positions
    def new_flock(self, count, lower_limits, upper_limits):
        width=upper_limits-lower_limits
        return (lower_limits[:,np.newaxis] + 
            np.random.rand(2, count)*width[:,np.newaxis])
        
	
	# Fly towards the middle
    def fly_towards_middle(self, strength):
        

	# Fly away from nearby boids
    def avoid_nearby_boids(self, alert_distance):
        
		
	# Try to match speed with nearby boids
    def match_speeds(self, formation_flying_distance, formation_flying_strength):
        
       
	
	# and update positions and velocities
    def update_boids(self):
        
		
	# animation runs update_boids() for each frame
    def animate(self,frame, scatter):
        

	# run animation
    def simulate(self):
        

