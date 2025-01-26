#! /usr/bin/python3 

import os, subprocess, sys
from termcolor import colored

if len(sys.argv) < 2:
    print(colored(f'Usage: python3 reorientation.py <input folder name> <output folder name>', 'red'))
    sys.exit(1)
else:
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    if not os.path.exists(input_dir):
        print(colored(f'Error: Input directory {input_dir} does not exist.', 'red'))
        sys.exit(1)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
   

base_path = os.path.abspath('.')


input_folder = os.path.join(base_path, input_dir)
output_folder = os.path.join(base_path, output_dir)

input_list = []
output_list = []

# for filename in os.listdir(input_folder):
#     input_list.append(filename[:-3])
    
for filename in os.listdir(output_folder):
    output_list.append(filename[:-18])

for filename in os.listdir(input_folder):
    if filename[:-7] not in output_list:
        in_file = os.path.join(input_dir, filename)
        out_file = os.path.join(output_dir, filename[:-7] + '-reoriented.nii.gz')
        print(colored(f'[*] Reorienting >> {filename}', 'blue'))
        subprocess.run(['fslreorient2std'], [in_file], [out_file])
        print(colored('[*] Done', 'green'))
    else:
        print(colored(f'[!] {filename} is reoriented already', 'yellow'))
print(colored('[~] Reorientation Done', 'yellow'))