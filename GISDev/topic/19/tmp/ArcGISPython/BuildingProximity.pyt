# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "BuildingProximity"
        self.alias = "buildingproximity"

        # List of tool classes associated with this toolbox
        self.tools = [BuildingProximity]


class BuildingProximity:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Building Proximity"
        self.description = "Determines which buildings on TAMU's campus are near a targeted building"
        self.canRunInBackground = False # Only used in ArcMap
        self.category = "Building Tools"

    def getParameterInfo(self):
        """Define the tool parameters."""

        # Building number
        buildingNumber = arcpy.Parameter(
            displayName="Building Number",
            name="buildingNumber",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        # Buffer size
        bufferSize = arcpy.Parameter(
            displayName="Buffer Size",
            name="bufferSize",
            datatype="GPLong",
            parameterType="Required",
            direction="Input"
        )

        params = [buildingNumber, bufferSize]

        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        campus = r"H:/DevSource/GarretM_GEOG676/GISDev/topic/18/tmp/ArcGISPython/Campus.gdb"

        # Setup our user input variables
        buildingNumber_input = parameters[0].valueAsText
        bufferSize_input = int(parameters[1].value)

        # Generate our where_clause
        where_clause = "Number = '%s'" % buildingNumber_input

        # Check if building exists
        # Define the Structures feature class
        structures = campus + "/TAMU_structures"
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
        shouldProceed = False

        for row in cursor:
            if row.getValue("Number") == buildingNumber_input:
                shouldProceed = True

        # If we shouldProceed do so
        if shouldProceed:

            # Generate the name for our generated buffer layer
            buildingBuff = "/building_%s_buffed_%s" % (
                buildingNumber_input,
                bufferSize_input
            )

            # Get reference to building
            buildingFeature = arcpy.Select_analysis(
                structures,
                campus + "/building_%s" % buildingNumber_input,
                where_clause
            )

            # Buffer the selected building
            arcpy.Buffer_analysis(
                buildingFeature,
                campus + buildingBuff,
                bufferSize_input
            )

            # Clip the structures to our buffered feature
            arcpy.Clip_analysis(
                structures,
                campus + buildingBuff,
                campus + "/clip_%s" % buildingNumber_input
            )

            # Remove the feature class we just created
            arcpy.Delete_management(
                campus + "/building_%s" % buildingNumber_input
            )

        else:
            print("Seems we couldn't find the building you entered")
            return None

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
