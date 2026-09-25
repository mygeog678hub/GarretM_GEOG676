import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "H:/DevSource/GarretM_GEOG676/GISDev/topic/17/tmp/ArcGISPython"
#arcpy.CreateFileGDB_management(arcpy.env.workspace, "Campus.gdb")
# Define our geodatabase
campus = r"H:/DevSource/GarretM_GEOG676/GISDev/topic/17/tmp/ArcGISPython/Campus.gdb"
# Define our where clause
where = '"Type" = \'HOUSING TAMU\''
# Convert shape file to geodatabase
arcpy.FeatureClassToGeodatabase_conversion(
    "TAMU_structures.shp",
    campus
)
# Perform a select
arcpy.Select_analysis(campus + "/TAMU_structures", campus + "/housing", where)