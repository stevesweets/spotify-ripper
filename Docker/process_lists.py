#!/bin/python2

import sys, os, subprocess

lists_dir = "/root/.spotify-ripper/share/lists"

download_lists = os.listdir(lists_dir)

for curr_list in download_lists:
    print("\n\n\n[ + ]  P R O C E S S I N G  C U R R E N T  L I S T :{}\n\n\n".format(curr_list))
    subprocess.call('spotify-ripper {}'.format(curr_list), shell=True, cwd=lists_dir)
    subprocess.call('mv {} {}.done'.format(curr_list,curr_list), shell=True, cwd=lists_dir)
