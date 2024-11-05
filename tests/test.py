import os
import pytest
import geopandas as gpd
from blocksnet import BlocksGenerator, LandUse, LandUseProcessor

zones_to_lu = {"zone_1": LandUse.RECREATION, "zone_2": LandUse.RESIDENTIAL, "zone_3": LandUse.BUSINESS}

@pytest.fixture
def boundaries():
    gdf = gpd.read_parquet(os.path.join(data_path, "boundaries.parquet"))
    crs = gdf.estimate_utm_crs()
    return gdf.to_crs(crs)