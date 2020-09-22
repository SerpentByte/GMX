## path to gromacs executable
gmx="/home/wasim/programs/gromacs/gmx-2019.6/bin/gmx"

## path to python. 
## choose or set according to your systnrg_min
#  anaconda/miniconda installation
python="/home/wasim/miniconda3/bin/python3" 
# in-built python
#python="/usr/bin/python3"


## normal gmx LJ particles simulation
#  energy minimization
$gmx grompp -f nrg_min.mdp -c init.gro -p topol.top -o em.tpr
$gmx mdrun -v -deffnm em
#  production run
$gmx grompp -f prod.mdp -c em.gro -p topol.top -o run.tpr
$gmx mdrun -v -deffnm run


# ## LJ particles simulation using tabulated LJ 
# ## potentials in table.xvg
# #  energy minimization
$gmx grompp -f nrg_min_tab.mdp -c init.gro -p topol.top -o em_tab.tpr
$gmx mdrun -v -deffnm em_tab -table table.xvg
# # #  production run
$gmx grompp -f prod.mdp -c em_tab.gro -p topol.top -o run_tab.tpr
$gmx mdrun -v -deffnm run_tab -table table.xvg

rm *#