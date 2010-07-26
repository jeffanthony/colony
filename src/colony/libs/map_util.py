#!/usr/bin/python
# -*- coding: Cp1252 -*-

# Hive Colony Framework
# Copyright (C) 2008 Hive Solutions Lda.
#
# This file is part of Hive Colony Framework.
#
# Hive Colony Framework is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Colony Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Colony Framework. If not, see <http://www.gnu.org/licenses/>.

__author__ = "Jo�o Magalh�es <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision: 3219 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2009-05-26 11:52:00 +0100 (ter, 26 Mai 2009) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import copy

def map_extend(base_map, extension_map):
    """
    Extends the given map with the extension map,
    retrieving a map resulting of the merge of both maps.

    @type base_map: Dictionary
    @param base_map: The map to be used as base for
    the merge.
    @type extension_map: Dictionary
    @param extension_map: The map to be used to extend the base
    one.
    @rtype: Dictionary
    @return: The map that result of the merge of both maps.
    """

    # copies the base map to create the initial result map
    result_map = copy.copy(base_map)

    # iterates over all the keys and values
    # in the extension map
    for key, value in extension_map.items():
        # sets the extension value in the result map
        result_map[key] = value

    # returns the result map
    return result_map