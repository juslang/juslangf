import subprocess as sp
import argparse
import sys
import os


# Set this to the version number of the script
VERSION = "0.0.1"

VERBOSE = False

class BuildScriptError(Exception):
    """An Exception thrown by build_sript"""
    pass

def Main():
    parser = argparse.ArgumentParser(description='Build script for frontend')

    parser.add_argument('--verbose', action='count', help='Enable verbose mode')
    parser.add_argument('--version', action='count', help='Print version number and exit')
    # parser.add_argument('--level', required=True, help='Level files output directory')
    # parser.add_argument('files', nargs=argparse.REMAINDER, help='Optional filenames to check')
    # parser.add_argument('--exclude', action='append', help='Name of submodule to exclude')
    args = parser.parse_args()

    if args.version and args.version > 0:
        print("build_script.py %s" % VERSION)
        sys.exit(0)

    global VERBOSE

    VERBOSE=(args.verbose and args.verbose > 0)

    dst_path = '/root/server/webserver/dist/'
    if not os.path.isdir(dst_path):
      os.makedirs(dst_path)
      print(f"build_script.py: created {dst_path}.")

    try:
      ret_out = sp.check_call('docker-compose -f docker-compose.prod.yml up', shell=True)
    except CalledProcessError as e:
      print(e.output.decode())
    
    print(f"docker-compose up result: {ret_out}")
    try:
      ret_out = sp.check_call("cp -rf out/* /root/server/webserver/dist/", shell=True)
    except CalledProcessError as e:
      print(e.output.decode())
    
    print(f"successfully copied to {dst_path}, ret_out:{ret_out}")
    try:
      ret_out = sp.check_call('docker-compose -f docker-compose.prod.yml down', shell=True)
    except CalledProcessError as e:
      print(e.output.decode())
    
    print(f"docker-compose down result: {ret_out}")


if __name__ == '__main__':
    Main()