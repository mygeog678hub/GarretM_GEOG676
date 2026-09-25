# Create a gdb and garage feature
import arcpy

folder_path = r"H:/DevSource/GarretM_GEOG676/lab_4"
arcpy.env.workspace = folder_path
gdb_name = "Test.gdb"
gdb_path = folder_path + "/" + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = "H:/DevSource/GarretM_GEOG676/lab_4/garages.csv"
garage_layer_name = "Garage_Points"
garages = arcpy.MakeXYEventLayer_management(csv_path, "X", "Y", garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + "/" + garage_layer_name

# open campus gdb, copy building feature to our gdb
campus = r"H:/DevSource/GarretM_GEOG676/lab_4/Campus.gdb"
buildings_campus = campus + "/Structures"
buildings = gdb_path + "/" + "Buildings"

arcpy.Copy_management(buildings_campus, buildings)

# Re-Projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + "/Garage_Points_reprojected", spatial_ref)

# Buffer the garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + "/Garage_Points_reprojected", gdb_path + "/Garage_Points_buffered", 150)

# Intersect our buffer with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + "/Garage_Building_Intersection", "All")
arcpy.TableToTable_conversion(gdb_path + "/Garage_Building_Intersection.dbf", "H:/DevSource/GarretM_GEOG676/lab_4", "nearbyBuildings.csv")

