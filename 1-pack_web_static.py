#!/usr/bin/python3
""" This script enerates a .tgz archives from the web_satic folder """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive """

    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "web_static_{}.tgz".format(time_now)
    archive_path = "versions/{}".format(filename)

    print("Packing web_static to {}".format(archive_path))

    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(archive_path))

    print("Successfully packed web_static to {}".format(archive_path))

    return archive_path
