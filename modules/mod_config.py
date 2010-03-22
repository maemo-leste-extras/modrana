#!/usr/bin/python
#----------------------------------------------------------------------------
# Configuration options
#
# Rename this file to mod_config.py to use it
#----------------------------------------------------------------------------
# Copyright 2007-2008, Oliver White
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#---------------------------------------------------------------------------
from base_module import ranaModule
import os #TODO: testing import, remove this
from time import clock

def getModule(m,d):
  return(config(m,d))

class config(ranaModule):
  """Handle configuration, options, and setup"""
  def __init__(self, m, d):
    ranaModule.__init__(self, m, d)

  def firstTime(self):
    # Option: load a GPX replay
#    m = self.m.get('replayGpx', None)
#    if(m != None):
#      m.load('track.gpx')

    # Option: set your start position
    self.set("pos", (49.2, 16.616667)) # Brno
    #self.set("centred", False)  # don't keep the map centred on the start position
    #  self.set("pos_source", "default")

    # Option: set the initial view
    # WARNING: this locks to these coordinates, unless set to false
    self.set("centreOn", False)
    
    # Option: set the map tiles
    # osma, mapnik, etc - see mod_mapTiles for list
    # currently: gmap,gsat,mapnik,osma,cycle,pyrender,localhost
    # NOTE: cycle map seems to be missing some z14 tiles
    self.set('layer',"osma")


    # Option: whether to centre on your position
    #self.set('centred', False)

    start = clock()
    m = self.m.get('loadTracklog', None) #TODO: move this somewhere else
    if(m != None):
      files = os.listdir('tracklogs')
      files = filter(lambda x: x != '.svn', files)
      for file in files:
        m.load('tracklogs/'+file)
      print "Loading tracklogs took %1.2f ms" % (1000 * (clock() - start))


      #m.load('Znaim-Wien.gpx')
      #m.load('znojmo-brno.gpx')

    # Option: what tracklogs to paint: None, 'simple', 'colored', 'colored-dotted'
    self.set("showTracklog", 'simple')
    # Option: True => draw circles for debuging of the track drawing mechanism optimalization
    #self.set('debugCircles', False)
    # Option: Number of threads for batch-downloading tiles
    self.set('maxBatchThreads', 5)
    # Option: Folder for storing downloaded tile images (there should be a slash at the end)
    self.set('tileFolder', 'cache/images/')
    # this sets the number of threads for bach tile download
    # even values of 10 can lead to 3000+ open sockets on a fast internet connection
    # handle with care :)
    self.set('maxDlThreads', 5)
    # this sets the number of threads used for determining the size of the batch (from http headers)
    # NOTE: even though we are downloading only the headers,
    # for a few tousand tiles this can be an unrivila amount of data
    # (so use this with caution on metered connections)
    self.set('maxSizeThreads', 20)




    pass
