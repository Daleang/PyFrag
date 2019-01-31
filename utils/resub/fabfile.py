# -*- coding: utf-8 -*-

__author__ = 'xiaobo'


import time
import os
from os import sys, path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from configure import *
from fabric.api import *

env.user = USERNAME
env.hosts = [HOSTNAME]



def deploy(JOBDIR, REMOTEDIR, JOBNAME):
    with cd(REMOTEDIR):
       run('rm -rf 1 2 3 4 5 *out adfinputfile jobinfo.txt job.py result sub')
       with lcd(JOBDIR):
          local('bash $PYFRAGHOME/bin/resub.sh %s' % JOBNAME)