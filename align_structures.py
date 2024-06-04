import sys
import multiprocessing as mp
import numpy as np
from glob import glob
from pymol import cmd

###############################################################################
# this script aligns different chain Hs with one chain H from the input       #
# Author: Panyue Wang                                                         #
# Email: pywang@ucdavis.edu                                                   #
###############################################################################


def align_to_pdb(structures_to_align):
    cmd.load(structures_to_align, "to_align")
    # output
    output_path = '.' + structures_to_align.split('.')[1] + "_aligned.pdb"
    cmd.align("to_align", "target")
    cmd.save(output_path, selection="to_align")


if __name__ == "__main__":
    # read in the pdb file from command line
    cmd.load(sys.argv[1], "target")
    # structure to align
    structure_path = sys.argv[2]
    structures_to_align = glob(structure_path + "/*.pdb")

    num_of_processors = mp.cpu_count()
    num_of_files = len(structures_to_align)
    cpu_load = int(num_of_files / num_of_processors)
    print(f"each processor will process: {cpu_load} files")
    structure_array = np.zeros([num_of_processors, 2]).astype(str)
    for i in range(num_of_processors):
        for j in range(2):
            index = i * 2 + j
            print(index)
            if index < num_of_files:
                structure_array[i, j] = structures_to_align[index]
            else:
                break
    print("Number of processors: ", num_of_processors)
    pool = mp.Pool(num_of_processors)
    results = [pool.apply(align_to_pdb, args=(structure_array))
               for to_align in structure_array if to_align.all() != "0.0"]
    pool.close()

#     for structure in structures_to_align:
#         # select chain H
#         align_to_pdb(to_align, target, output_path)
