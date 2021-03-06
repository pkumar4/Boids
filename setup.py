from setuptools import setup, find_packages
setup(
    name = "Boids",
    version = "0.1",
    description='Simulate flocking birds',
    license='MIT',
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/boids'],
    install_requires = ['matplotlib', 'numpy', 'pyyaml', 'argparse','mock', 'nose']
)
