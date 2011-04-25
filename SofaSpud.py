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

import sys
import app
import os

def start_server():
	
	# some prelimenary setup
	app.FULLNAME = os.path.normpath(os.path.abspath(__file__))
	app.NAME = os.path.basename(app.FULLNAME)
	app.PROG_DIR = os.path.dirname(app.FULLNAME)
	app.DATA_DIR = app.PROG_DIR
	app.ARGS = sys.argv[1:]
	app.CREATEPID = False
	
	print "SofaSpud has started"
	
	app.start()
	
	sys.exit();

if __name__ == '__main__':	
	start_server()