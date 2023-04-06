#!/usr/bin/python3
""" fabric script to create an archive of our webstatic directory
of my AirBnB webstatic directory
"""


from fabric.api import local
from datetime import datetime
from fabric import task

def do_pack():
    """ function to create an archive """

    time_now = datetime.now()
    time_str = time_now.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format
              (time_str))
        return ("versions/web_static_{}".format(time_str))

    except Exception as e:
        return None
