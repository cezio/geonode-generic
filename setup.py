# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="geonode_generic",
    version="0.1",
    author="",
    author_email="",
    description="geonode_generic, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="geonode_generic geonode django",
    url='https://github.com/geonode_generic/geonode_generic',
    packages=['geonode_generic',],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
	   'Django==1.8.18',
       'six==1.10.0',
       'django-cuser==2017.3.16',
       'django-model-utils==3.0.0',
       'pyshp==1.2.12',
       'celery==4.1.0',
       'Shapely>=1.5.13,<1.6.dev0',
       'proj==0.1.0',
       'pyproj==1.9.5.1',
       'pygdal==2.2.1.3',
       'inflection==0.3.1'
       # 'geonode>=2.9'
    ],
)
