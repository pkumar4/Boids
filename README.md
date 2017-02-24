Boids
=====

MPHYG001 Research Software Engineering With Python coursework 2

http://development.rc.ucl.ac.uk/training/engineering/

A refactoring exercise to streamline the code design and performance

```
usage: boids [-h] [--config CONFIG]

Simulating Boids: Refactored Bad Boids to simulate boids flying.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG, -c CONFIG
                        Boid simulator YAML configuration file. Defaults are

```


YAML configuration file example:
```
Boids:
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
  ylim: [-500, 1500]
```

