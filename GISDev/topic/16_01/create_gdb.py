import arcpy

folder_path = "H:/DevSource/GarretM_GEOG676/GISDev/topic/16_01/temp/ArcGISPython"

arcpy.management.CreateFileGDB(folder_path, "Test.gdb")