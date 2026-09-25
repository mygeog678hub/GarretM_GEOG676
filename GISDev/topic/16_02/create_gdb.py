import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = "H:/DevSource/GarretM_GEOG676/GISDev/topic/16_02/tmp/ArcGISPython"

# arcpy.CreateFileGDB_management(arcpy.env.workspace, "DC.gdb")

whitehouse = arcpy.management.MakeXYEventLayer("wh.csv", "x", "y", "wh")

input_layers = ["Tree_Removal_in_Last_30_Days.shp", whitehouse]

arcpy.FeatureClassToGeodatabase_conversion(
    input_layers,
    r"H:/DevSource/GarretM_GEOG676/GISDev/topic/16_02/tmp/ArcGISPython/DC.gdb"
)

dcGdb = r"H:/DevSource/GarretM_GEOG676/GISDev/topic/16_02/tmp/ArcGISPython/DC.gdb"

arcpy.analysis.Near(
    dcGdb + "/Tree_Removal_in_Last_30_Days",
    dcGdb + "/wh",
    None,
    "NO_LOCATION",
    "NO_ANGLE",
    "PLANAR"
)

arcpy.Buffer_analysis(
    dcGdb + "/wh",
    dcGdb + "/wh_buffered",
    .009
)

arcpy.Intersect_analysis(
    [
        dcGdb + "/wh_buffered",
        dcGdb + "/Tree_Removal_in_Last_30_Days"
    ],
    dcGdb + "/intersection",
    "ALL"
)

arcpy.TableToTable_conversion(
    dcGdb + "/intersection.dbf",
    arcpy.env.workspace,
    "intersection.csv"
)