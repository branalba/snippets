#!/usr/bin/env python
# title           :pythonstarter.py
# description     :Starter file for new python projects
# author          :Brandon Alba <branalba42@gmail.com>
# date            :20210701
# version         :0.1
# usage           :./pythonstarter.py
# notes           :
# python_version  :3.9.5
# ==============================================================================

# module imports
import click

# program info
APP_NAME = "Python Starter"
APP_VERSION = 0.1

#####################
# MAIN PROGRAM
#####################


@click.command()
# click parameters
@click.version_option(version=APP_VERSION, prog_name=APP_NAME)
@click.option('--verbose', '-v', default=0, type=click.IntRange(0, 2),
              help="Runs program with verbose output for debugging purposes.")
def main(
        verbose
):

    click.echo("Successfully ran our binary!")
