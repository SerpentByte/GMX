# Table potential implementation and benchmarking

### This folder contains code for implementation of 
### GROMACS tabulated potentials and it's benchmarkings.
</br>
## File information
### Python scripts
1. init_config.py        generation of initial structure
       Usage: <path-to-python3>/python3 init_config.py <number of particles>
       It will adjust the number of particles so as to be able to generate
       a perfect cubic lattice with mass=1, density=0.884. Box dimensions
       are calculated from mass, number of particles and density.
       *System reference: 
       Understanding Molecular Simulation: From Algorithms to Applications,
       Page 145
       
</br>
