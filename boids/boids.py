
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class Boids(object):
    def __init__(self, config, count=0, fly_to_middle=0, alert_distance=0, formation_flying_distance=0, formation_flying_strength=0): 
		
	# generate random velocities and positions
    def new_flock(self, count, lower_limits, upper_limits):
        
	
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
        

