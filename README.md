# SEA library
**SEA (Spatial event aggregation)** is a library that allows users to aggregate poits based on their spatial distribution by city districts.

**Link to the library:** https://pypi.org/project/sea-spatial-event-aggregation/


**Code usage:**
```bash
pip install sea_spatial_event_aggregation

import pandas as pd
import geopandas as gpd

gdf_points = gpd.read_file ('...')
gdf_polygons = gpd.read_file ('...')

from sea_spatial_event_aggregation import *

points = PointLayer(data=gdf_points)
polygons = PolygonLayer(data=gdf_polygons, name='name')

count_points_in_polygon (points, polygons)

counts = count_points_in_polygon (points, polygons)
calculate_density(polygons, counts)
top_district (polygons, counts)