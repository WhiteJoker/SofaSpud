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

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, NoSuchTableError
from sqlalchemy.orm import mapper, relation, scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.schema import MetaData, Table, Column, ForeignKey
from sqlalchemy.sql.expression import and_, desc
from sqlalchemy.types import Integer, DateTime, String, Boolean, Text

import os
import datetime
import sys
import app
import db

class DBConnection():
	def __init__(self, dbFileName="sofaspud.db"):
		
		print "Database is being initialized"
		
		self.dbFileName = dbFileName
		self.dbPath = os.path.join(app.DATA_DIR, self.dbFileName);
		self.engine = create_engine("sqlite:///%s" % self.dbPath)
		self.metadata = MetaData(self.engine)
		self.session = scoped_session(sessionmaker(bind = self.engine, autocommit = True))
		
		# DB exists, do upgrade
		if os.path.isfile(self.dbPath):
			self.doUpgrade = True;
		else:
			self.doUpgrade = False
	
		# DB VERSION
		latestDatabaseVersion = 1

		dbVersionTable = Table('DbVersion', self.metadata,
                     		Column('version', Integer, primary_key = True)
        )

		movieTable = Table('Movie', self.metadata,
						Column('id', Integer, primary_key = True),
						Column('dateAdded', DateTime(), default = datetime.datetime.utcnow),
						Column('dateChanged', DateTime(), default = datetime.datetime.utcnow),
						Column('name', String()),
						Column('year', Integer),
						Column('status', String()),
						Column('movieDb', String())
		)
		
		serieTable = Table('Serie', self.metadata,
						Column('id', Integer, primary_key = True),
						Column('dateAdded', DateTime(), default = datetime.datetime.utcnow),
						Column('dateChanged', DateTime(), default = datetime.datetime.utcnow),
						Column('tvDb', String()),
						Column('name', String()),
						Column('overview', Text()),
						Column('network', String()),
						Column('genre', String()),
						Column('runtime', String()),
						Column('airing', String()),
						Column('startYear', String()),
						Column('language', String()),
						Column('status', String()),
		)
		
		episodeTable = Table('Episode', self.metadata,
						Column('id', Integer, primary_key = True),
						Column('dateAdded', DateTime(), default = datetime.datetime.utcnow),
						Column('dateChanged', DateTime(), default = datetime.datetime.utcnow),
						Column('serieid', Integer, ForeignKey('Serie.id')),
						Column('tvDb', String()),
						Column('name', String()),
						Column('season', Integer),
						Column('episode', Integer),
						Column('description', Text()),
						Column('airDate', DateTime()),
						Column('status', String()),
		)
		
		# Mappers
		versionMapper = mapper(DbVersion, dbVersionTable)
		movieMapper = mapper(Movie, movieTable)
		serieMapper = mapper(Serie, serieTable, properties = {
			'episode': relation(Episode)
		})
		episodeMapper = mapper(Episode, episodeTable)
		
		self.metadata.create_all()
		
		if self.doUpgrade:
			upgradeDb()
		else:
			for nr in range(1, latestDatabaseVersion + 1):
				self.session.add(DbVersion(nr))
	            		            
	def upgradeDb():
	
		currentVersion = self.session.query(DbVersion).order_by(desc(DbVersion.version)).first()
		if currentVersion:
			if currentVersion.version == latestDatabaseVersion:
				log.debug('Database is up to date.')
				return

class DbVersion(object):
	def __init__(self, version):
		self.version = version
		
	def __repr__(self):
		return "<dbversion: %s" % self.version

class Movie(object):
	name = None
	status = None
	dateChanged = None
	
	def __repr__(self):
		return "<movie: %s" % self.name
        
class Serie(object):
	name = None
	status = None
	dateChanged = None
	
	def __repr__(self):
		return "<serie: %s" % self.name
		
class Episode(object):
	name = None
	serie = None
	status = None
	dateChanged = None
	
	def __repr__(self):
		return "<episode %s serie=%s" % (self.name, self.Serie.name)
