from argparse import ArgumentParser
import sys
import yaml
from StringIO import StringIO
from boids import Boids

def process():
    parser = ArgumentParser(description = "Simulating Boids")
    parser.add_argument('--config', '-c', type=str, default="",  help="config YAML file. If not provided defaults are applied")
    arguments= parser.parse_args()
    
    #dictionary containing the configuration for the boids simulator
    cfg={}

    #default settings YAML 
    default="""Boids:
  count: 50
  position_limits: [-450, 300, 50, 600]
  velocity_limits: [0, -20, 10, 20]
Dynamics:
  alert_distance: 100
  fly_to_middle_strength: 0.01
  formation_flying_strength: 0.125
  formation_flying_distance: 10000
Animation:
  frames: 50
  interval: 50
  xlim: [-500, 1500]
  ylim: [-500, 1500]"""

    #open given cfg file within try block to catch wrong filename etc.
    try:
        with open(arguments.config) as cfg_file:
            cfg=yaml.load(cfg_file)

    except:
        #use default settings if no or wrong config file given!
        print "Error reading config file. Program will run with default values as below"
        print default
        cfg=yaml.load(StringIO(default))
    
    
    #run boids simulation with given settings
    boids=Boids(cfg, cfg['Boids']['count'], cfg['Dynamics']['fly_to_middle_strength'], 
				cfg['Dynamics']['alert_distance'], cfg['Dynamics']['formation_flying_distance'], 
				cfg['Dynamics']['formation_flying_strength'])
    boids.simulate()


if __name__ == "__main__":
    process()

