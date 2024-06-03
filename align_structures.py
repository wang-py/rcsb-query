import sys
from glob import glob
from pymol import cmd

###############################################################################
# this script aligns different chain Hs with one chain H from the input       #
# Author: Panyue Wang                                                         #
# Email: pywang@ucdavis.edu                                                   #
###############################################################################


def align_to_pdb(to_align, target_pdb, output_path):
    cmd.align(to_align, target_pdb)
    cmd.save(output_path, selection=to_align)


if __name__ == "__main__":
    target = "target"
    to_align = "to_align"
    # read in the pdb file from command line
    cmd.load(sys.argv[1], target)
    # structure to align
    structure_path = sys.argv[2]
    structures_to_align = glob(structure_path + "/*.pdb")

    for structure in structures_to_align:
        cmd.load(structure, to_align)
        # output
        output_path = structure.split('.')[0] + "_aligned.pdb"
        # select chain H
        align_to_pdb(to_align, target, output_path)
