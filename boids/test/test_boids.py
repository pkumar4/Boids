from ..boids import Boids
from nose.tools import assert_almost_equal, assert_equal
import os
import yaml
import numpy as np
import random
from mock import Mock, patch

# Test the new_flock(self, count, lower_limits, upper_limits) function
def test_new_flock():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'samples_new_flock_unit.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            rand       = fixture.pop('rand')
            positions  = fixture.pop('positions')
            velocities = fixture.pop('velocities')
            with patch.object(np.random, 'rand', return_value=rand) as mock_method:
                boids = Boids()
                npTest.assert_array_equal(np.asarray(positions),  boids.positions)
                npTest.assert_array_equal(np.asarray(velocities), boids.velocities)

def test_fly_towards_middle():
    #randomized test
    # generate random range data
    length=random.randint(10,50)
    boids=Boids({},length)
    boids.positions=np.array([random.random()*np.arange(length), random.random()*np.arange(length)])
    fly_middle=boids.fly_towards_middle(random.random())

    # check length
    assert_equal(fly_middle.size, 2*length)
    # for range variables it should sum to zero due to symmetry
    assert_almost_equal(np.sum(fly_middle), 0, delta = 1e-10)

    #regression test
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','sample_fly_to_middle_unit.yml')))
    boid_data=regression_data["before"]
    positions=np.array([boid_data[0], boid_data[1]])
    velocities=np.array([boid_data[2], boid_data[3]])
    #feed data into boid
    boids=Boids({})
    boids.positions=positions
    boids.velocities=velocities
    #do update check if same values obtained
    boids.velocities += boids.fly_towards_middle(0.01)
    boids.positions += boids.velocities
    for after,before in zip(regression_data["after"],positions.tolist()+velocities.tolist()):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.02)
	

def test_avoid_nearby_boids():
    # generate random range data
    length=random.randint(10,50)
    boids=Boids({},length)
    boids.positions=np.array([100*random.random()*np.arange(length), 100*random.random()*np.arange(length)])
    collisions=boids.avoid_nearby_boids(1000)

    # check length
    assert_equal(collisions.size, 2*length)
    # for range variables it should sum to zero due to symmetry
    assert_almost_equal(np.sum(collisions), 0, delta = 1e-10)

    #regression test
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','sample_avoid_collisions_unit.yml')))
    boid_data=regression_data["before"]
    positions=np.array([boid_data[0], boid_data[1]])
    velocities=np.array([boid_data[2], boid_data[3]])
    #feed data into boid
    boids=Boids({})
    boids.positions=positions
    boids.velocities=velocities
    #do update check if same values obtained
    boids.velocities += boids._avoid_collisions(100)
    boids.positions += boids.velocities
    for after,before in zip(regression_data["after"],positions.tolist()+velocities.tolist()):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.02)
	

def test_match_speeds():
    # generate random range data
    length=random.randint(10,50)
    boids=Boids({}, length)
    speed=boids.match_speeds(100,100)

    # check length
    assert_equal(speed.size, 2*length)
    # for range variables it should sum to zero due to symmetry
    assert_almost_equal(np.sum(speed), 0, delta = 1e-10)
    
    #regression test
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','matchSpeed.yml')))
    boid_data=regression_data["before"]
    positions=np.array([boid_data[0], boid_data[1]])
    velocities=np.array([boid_data[2], boid_data[3]])
    #feed data into boid
    boids=Boids({})
    boids.positions=positions
    boids.velocities=velocities
    #do update check if same values obtained
    boids.velocities += boids.match_speeds(10000,0.125)
    boids.positions += boids.velocities
    for after,before in zip(regression_data["after"],positions.tolist()+velocities.tolist()):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.02)
	

