#!/usr/bin/env python
#
# 
# Copyright (C) 2011 Edwin Bosveld
#
# This file is part of SofaSpud.
# 
# SofaSpud is free software: you can redistribute it and/or modify 
# it under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.
# 
# SofaSpud is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License 
# along with SofaSpud.  If not, see <http://www.gnu.org/licenses/>.

from app.config import db

PROG_DIR = '.'
FULLNAME = None
NAME = None
ARGS = []
SYS_ENCODING = ''
DATA_DIR = ''
CREATEPID = False
PIDFILE = ''

def start():
	print "App is being initialized"
	myDB = db.DBConnection()