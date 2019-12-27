# Installation

1. Install Docker
2. docker pull mdillon/postgis

[Link](https://hub.docker.com/r/mdillon/postgis/)
# Usage


*show all images:*

    docker images

*find out image id, then use it to run*:

    docker run b2a8

*connect that thing with other postgresql:*

    docker run -it --link <NAME GIVEN AT CREATION OF CONTAINER> :postgres --rm postgres \
    sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'

*run after already creating container*:

    docker run mdillon/postgis

    docker ps //get id of container

    docker exec -it 71c667e29110 /bin/bash

*use psql to log onto*:

    psql -U postgresql

    \c testgeo

* use postgres*:

    \c \<bla> => connect to bla
    \d \<table> => get info about table
    \q => quit

# [Introduction to PostGIS](https://www.youtube.com/watch?v=hMn74o11wdk)

* Spatial Data Types:
  - Points (x,y)
  - Lines ([p1,p2,p3,..])
  - Polygones ([l1,l2,l3,...] closed)

* shp2pgsql => shape to sql


## Map-Data => postGIS

[converter-script](https://github.com/openstreetmap/osm2pgsql)
* Install: sudo apt install osm2pgsql
* Enable hstore: in psql: CREATE EXTENSION hstore;
* Convert: osm2pgsql berlin-latest.osm.pbf -d khama -H localhost -P 5432 -U khama --hstore
## QGIS: GUI for POSTGIS

[Link](https://www.qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu)
* Install:
  - sudo add-apt-repository ppa:ubuntugis/ppa
  - sudo apt install qgis  
