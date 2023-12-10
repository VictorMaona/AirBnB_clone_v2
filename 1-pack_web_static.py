#!/usr/bin/python3
"""creates a.tgz archive using the web_static folder contents."""
from fabric.api import local
import time


def do_pack():
    """Produce tgz archive by utilizing the web_static folder."""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
