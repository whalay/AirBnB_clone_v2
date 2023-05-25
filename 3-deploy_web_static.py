#!/usr/bin/python3I
""" This script distributes an archive to the both webservers"""
from fabric.api import local, put, run, env, runs_once
from datetime import datetime
from os.path import isfile


env.hosts = ["54.197.113.126", "54.84.209.67"]
env.user = "ubuntu"


@runs_once
def do_pack():
    """ Generates a .tgz archive """

    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "web_static_{}.tgz".format(time_now)
    archive_path = "versions/{}".format(filename)

    print("Packing web_static to {}".format(archive_path))

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(archive_path))
    if result.failed:
        return None

    print("Successfully packed web_static to {}".format(archive_path))

    return archive_path


def do_deploy(archive_path):
    """ Distributes an archive to webserver """

    if not isfile(archive_path):
        return False

    print("Deploying new version")

    archive_name = archive_path.split("/")[-1]
    folder_name = archive_name[: -4]
    dir_path = "/data/web_static/releases/{}".format(folder_name)

    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(dir_path))
    result = run("tar -xzf /tmp/{} -C {}".format(archive_name, dir_path))

    if result.failed:
        return False

    run("cp -r {}/web_static/* {}".format(dir_path, dir_path))
    run("rm -rf /tmp/{} {}/web_static".format(archive_name, dir_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(dir_path))

    print("New version deployed!")

    return True


def deploy():
    """ Performs a full deployment from generating archive to deploying """

    filename = do_pack()
    if not filename:
        return False

    return do_deploy(filename)
