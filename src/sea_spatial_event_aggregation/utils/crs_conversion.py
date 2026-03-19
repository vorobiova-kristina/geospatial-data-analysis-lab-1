import geopandas as gpd


def crs_to_local(gdf):
    """Конвертация в местную СК"""
    local_crs = gdf.estimate_utm_crs()
    gdf = gdf.to_crs(local_crs)
    return gdf
