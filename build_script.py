import subprocess as sp
import argparse
import sys
import os
import locale


# Set this to the version number of the script
VERSION = "0.0.1"

VERBOSE = False

DEVNULL = open(os.devnull, 'w')
encoding = locale.getpreferredencoding()

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

    ret_out = sp.check_output(['docker-compose', '-f', 'docker-compose.prod.yml', 'up'], stderr=DEVNULL).decode(encoding).strip()
    print(f"docker-compose up result: {ret_out}")
    if ret_out:
      # ret_out = sp.check_output(['cp', '-rf', 'out/*', dst_path], stderr=DEVNULL).decode(encoding).strip()
      os.system("cp -rf out/* /root/server/webserver/dist/")
      print(f"build_script.py: successfully copied to {dst_path}.")
    ret_out = sp.check_output(['docker-compose', '-f', 'docker-compose.prod.yml', 'down'], stderr=DEVNULL).decode(encoding).strip()
    print(f"docker-compose down result: {ret_out}")


if __name__ == '__main__':
    Main()