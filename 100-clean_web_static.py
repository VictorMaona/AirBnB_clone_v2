#!/usr/bin/python3
# Fabfile will remove outdated archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Eliminate outdated archives.

    Args:
        number (int): Archives one should preserve.

    Only the most recent archive is kept if number is 0 or 1. If
    keeps the most and second-most recent archives if number is 2,
    such are.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
