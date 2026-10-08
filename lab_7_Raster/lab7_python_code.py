import arcpy


# Assign bands
source = r"H:/DevSource/GarretM_GEOG676/lab_7/landsat4"

band1 = arcpy.sa.Raster(source + r"/blue.tif")      # blue
band2 = arcpy.sa.Raster(source + r"/green.tif")     # green
band3 = arcpy.sa.Raster(source + r"/red.tif")       # red
band4 = arcpy.sa.Raster(source + r"/nir08.tif")     # NIR

combined = arcpy.CompositeBands_management(
    [band1, band2, band3, band4],
    source + r"/output_combined.tif"
)


# Hillshade
dem = r"H:/DevSource/GarretM_GEOG676/lab_7/dem/dem_30m.tif"

azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1

arcpy.ddd.HillShade(
    dem,
    r"H:/DevSource/GarretM_GEOG676/lab_7/dem/output_hillshade.tif",
    azimuth,
    altitude,
    shadows,
    z_factor
)


# Slope
output_measurement = "DEGREE"
z_factor = 1

arcpy.ddd.Slope(
    dem,
    r"H:/DevSource/GarretM_GEOG676/lab_7/dem/output_Slope.tif",
    output_measurement,
    z_factor
)

print("success!")