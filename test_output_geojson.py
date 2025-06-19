
# load modules
import os
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib import gridspec
plt.ion()
import pandas as pd
from scipy import interpolate
from scipy import stats
from datetime import datetime, timedelta
import pytz
from pyproj import CRS
from coastsat import SDS_download, SDS_preprocess, SDS_shoreline, SDS_tools, SDS_transects, SDS_slope


geojson_output_file = os.path.join(os.getcwd(), 'examples', 'tp2_L5_L7_S2_output_lines.geojson')
settings = {'output_epsg': 3826}
distance_threshold = 100

#test1 - load shorelines from a .geojson file: SDS.output_from_geojson(filename)
output = SDS_tools.output_from_geojson(geojson_output_file)
#test2- output multilinestring type SDS_tools.output_to_gdf_multilines(output, distance_threshold)
gdf = SDS_tools.output_to_gdf_multilines(output, distance_threshold)
gdf.crs = CRS(settings['output_epsg']) # set layer projection
# save GEOJSON layer to file
filename_output_ml = os.path.join(os.getcwd(),'examples','multilines_output_tph.geojsion')
gdf.to_file(filename_output_ml, driver='GeoJSON', encoding='utf-8')



