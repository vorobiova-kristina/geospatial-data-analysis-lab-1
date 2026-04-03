import geopandas as gpd
from pandas import Series

from src.sea.core.geometries import PointLayer, PolygonLayer
from src.sea.exceptions import CRSMismatchError, UndefinedCRSError
from src.sea.utils.crs_conversion import crs_to_local


def check_crs(layer):
    if layer.data.crs is None:
        raise UndefinedCRSError(f"Не задана СК у слоя {layer.name}")


def count_points_in_polygon(
    points_gdf: PointLayer, polygons_gdf: PolygonLayer
) -> Series:

    check_crs(points_gdf)
    check_crs(polygons_gdf)

    polygons_local = crs_to_local(polygons_gdf.data)
    points_local = points_gdf.data.to_crs(polygons_local.crs)

    if polygons_local.crs != points_local.crs:
        raise CRSMismatchError(f"Системы координат слоев не совпадают!")

    points_in_districts = gpd.sjoin(polygons_local, points_local, predicate="contains")
    points_count = points_in_districts.groupby(polygons_gdf.name).size()
    return points_count


def calculate_density(
    polygons_gdf: PolygonLayer, count_column: Series
) -> gpd.GeoDataFrame:
    polygons_for_calc = polygons_gdf.data.copy()
    polygons_for_calc = polygons_for_calc.set_index(polygons_gdf.name)
    polygons_for_calc["count"] = count_column
    polygons_for_calc["count"] = polygons_for_calc["count"].fillna(0)
    polygons_for_calc["area"] = polygons_for_calc.area / 10**6
    polygons_for_calc["density"] = (
        polygons_for_calc["count"] / polygons_for_calc["area"]
    )
    return polygons_for_calc


def top_district(polygons_gdf: PolygonLayer, count_column: Series) -> gpd.GeoDataFrame:
    polygons_copy = polygons_gdf.data.copy()
    polygons_copy = polygons_copy.set_index(polygons_gdf.name)
    polygons_copy["count"] = count_column
    polygons_copy["count"] = polygons_copy["count"].fillna(0)
    polygons_ranking = polygons_copy.sort_values(by="count", ascending=False)
    return polygons_ranking
