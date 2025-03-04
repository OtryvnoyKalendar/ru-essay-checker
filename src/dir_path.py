""""""

import os
import sys


def get_lower_directory_path(directory):
    """"""
    script_path = os.path.abspath(sys.argv[0])
    script_dir = os.path.dirname(script_path)
    target_dir = os.path.join(os.path.dirname(script_dir), directory)
    target_dir = os.path.relpath(target_dir)
    return target_dir + os.path.sep
