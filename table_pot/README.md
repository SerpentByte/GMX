# Table potential implementation and benchmarking

## This folder contains code for implementation of 
## GROMACS tabulated potentials and it's benchmarkings.

### File information

#### Python scripts

1. init_config.py --> generation of initial structure</br>
       Usage: <path-to-python3>/python3 init_config.py <number of particles></br>
       It will adjust the number of particles so as to be able to generate</br>
       a perfect cubic lattice with mass=1, density=0.884. Box dimensions</br>
       are calculated from mass, number of particles and density.</br>
       Default output file is init.gro.</br>
       *System reference: </br>
       Understanding Molecular Simulation: From Algorithms to Applications, Page 145
       
</br>

2. gen_table_pot.py --> generate the table potential table.</br>
       Usage: <path-to-python3>/python3 gen_table_pot.py</br>
       By default, the output file is table.xvg.
       
</br>

#### Miscellaneous files

3. autorun.sh --> a BASH script to run all simulations.</br>

4. nrg_min.mdp --> energy minimization mdp file for internal LJ potential.</br>

5. nrg_min_tab.mdp --> energy minimization mdp file for tabulated LJ potential.</br>

6. prod.mdp --> production run mdp file for internal LJ potential.</br>

7. prod_tab.mdp --> production run mdp file for tabulated LJ potential.</br>

8. Rest are standard gromacs files. Please refer to the GROMACS manual.</br>
   http://manual.gromacs.org/current/reference-manual/index.html
