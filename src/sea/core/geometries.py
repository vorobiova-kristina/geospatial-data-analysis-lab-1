from dataclasses import dataclass

import geopandas as gpd


@dataclass
class PointLayer:
    """
    a class that contains a layer with point objects

    attributes:
    data (gpd.GeoDataFrame): table with geometries
    """

    data: gpd.GeoDataFrame


@dataclass
class PolygonLayer:
    """
    a class that holds contains a layer with polygon objects

    attributes:
    data (gpd.GeoDataFrame): table with geometries
    name (str): name of the district
    """

    data: gpd.GeoDataFrame
    name: str
