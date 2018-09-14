#!/usr/bin/env python
# -*- coding: utf-8 -*-

import distutils.log
import platform
import subprocess
from distutils.cmd import Command

from setuptools import setup


class DockerStart(Command):
    description = "Spin Docker as defined in docker-compose.yml"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = [
            "docker-compose", "up", "--detach", "--no-build", "--no-color"
        ]
        where = "GNU/Linux"
        if platform.system() == 'Windows':
            where = "Windows"
            command.append("db-win")
        else:
            command.append("db")
        self.announce(
            'Running command: {} on {}'.format(command, where),
            level=distutils.log.INFO)
        subprocess.check_call(command)


class DockerStop(Command):
    description = "Stop Docker service"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = ["docker-compose", "down"]
        where = "GNU/Linux"
        if platform.system() == 'Windows':
            where = "Windows"
        self.announce(
            'Running command: {} on {}'.format(command, where),
            level=distutils.log.INFO)
        subprocess.check_call(command)


setup(
    name='rs',
    version='0.1',
    description='"To be written"',
    url='https://github.com/jdpc91/redabitsScabcr',
    author='RedaBits',
    author_email='redabits@gmail.com',
    license='Propietary',
    packages=['rs'],
    install_requires=[],
    scripts=[],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False,
    cmdclass={
        'docker_start': DockerStart,
        'docker_stop': DockerStop
    })
