# coding=utf-8
# flask & env demo
__author__ = 'Jesús Jerez <jerezmoreno@gmail.com>'


import os
import subprocess


if __name__ == '__main__':
    child = subprocess.Popen([os.path.join(os.path.realpath(os.path.dirname(__file__)), "run.sh")], shell=True)
    try:
        child.wait()
    except KeyboardInterrupt:
        child.terminate()