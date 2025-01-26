#! /usr/bin/python3 

import os, subprocess, sys
from termcolor import colored

if len(sys.argv) < 2:
    print(colored(f'Usage: python3 conversion.py <input folder name> <output folder name>', 'red'))
    sys.exit(1)
else:
    input_dir = sys.argv[1]
    if not os.path.exists(input_dir):
        print(colored(f'Error: Input directory {input_dir} does not exist.', 'red'))
        sys.exit(1)
        
base_path = os.path.abspath('.')

input_folder = os.path.join(base_path, input_dir)

input_list = []

for filename in os.listdir(input_folder):
    in_file = os.path.join(input_dir, filename)
    print(colored(f'[*] Converting >> {filename} to .hdr', 'blue'))
    subprocess.run(['fslchfiletype'], [in_file])
    print(colored('[*] Done', 'green'))
        
print(colored('[~] Conversion Done', 'yellow'))