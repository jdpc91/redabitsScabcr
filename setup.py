#!/usr/bin/env python
# -*- coding: utf-8 -*-

import distutils.log
import platform
import subprocess
from distutils.cmd import Command

from setuptools import setup
from setuptools.command.test import test as TestCommand


class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests'])


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
    install_requires=['SQLAlchemy>=1.2', 'pyodbc>=4.0', 'requests>=2.19'],
    scripts=['bin/rsb'],
    tests_require=['nose', 'coverage', 'mimesis'],
    zip_safe=False,
    cmdclass={
        'docker_start': DockerStart,
        'docker_stop': DockerStop,
        'test': NoseTestCommand
    })
