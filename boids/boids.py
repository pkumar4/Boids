
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
        middle=np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle[:, np.newaxis]
        self.velocities -= direction_to_middle * strength

	# Fly away from nearby boids
    def avoid_nearby_boids(self, alert_distance):
        separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        far_away = square_distances > alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0,:,:][far_away] =0
        separations_if_close[1,:,:][far_away] =0
        self.velocities += np.sum(separations_if_close,1) 
		
	# Try to match speed with nearby boids
    def match_speeds(self, formation_flying_distance, formation_flying_strength):
        separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        velocity_differences = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis]
        very_far=square_distances > formation_flying_distance
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0,:,:][very_far] =0
        velocity_differences_if_close[1,:,:][very_far] =0
        return (-1) * np.mean(velocity_differences_if_close, 1) * formation_flying_strength
        
       
	
	# invoke fly_towards_middle and avoid_nearby_boids
	# and update positions and velocities
    def update_boids(self):
        self.fly_towards_middle(self.fly_to_middle)  
        self.avoid_nearby_boids(self.alert_distance) 
        self.velocities += self.match_speeds(self.formation_flying_distance, self.formation_flying_strength)
        self.positions += self.velocities
		
	# animation runs update_boids() for each frame
    def animate(self,frame, scatter):
        self.update_boids()
        scatter.set_offsets(zip(self.positions[0], self.positions[1]))

	# run animation
    def simulate(self):
        figure=plt.figure()
        axes=plt.axes(xlim=self.config['Animation']['xlim'], ylim=self.config['Animation']['ylim'])
        scatter=axes.scatter(self.positions[0],self.positions[1])
        anim = animation.FuncAnimation(figure, self.animate, fargs=[scatter], 
                                       frames=self.config['Animation']['frames'], interval=self.config['Animation']['interval'])
        plt.show()
        

