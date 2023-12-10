#!/usr/bin/python3
""" The function that initiates """
from fabric.api import *


env.hosts = ['35.153.231.137', '54.89.119.123']
env.user = "ubuntu"


def do_clean(number=0):
    """ eliminates outdated archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
