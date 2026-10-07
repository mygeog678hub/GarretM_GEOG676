# -*- coding: utf-8 -*-

import arcpy
import time


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "GraduatedColorsRenderer"
        self.alias = "graduatedcolorsrenderer"

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]


class GraduatedColorsRenderer:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Graduated Colors"
        self.description = "Create a graduated colored map based on a specific attribute of a layer"
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        """Define the tool parameters."""
        #original project name
        param0 = arcpy.Parameter(
            displayName="Input ArcGIS Pro Project Name",
            name="aprxInputName",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )

        # which layer you want to clasify to create a color map
        param1 = arcpy.Parameter(
            displayName="Layer to Classify",
            name="LayerToClassify",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )

        # Output folder location
        param2 = arcpy.Parameter(
            displayName="Output Location",
            name="OutputLocation",
            datatype="DEFolder",        
            direction="Input"
        )
        # Output Project Name
        param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3]
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
        # Define our progressor variables
        readTime = 2.5
        start = 0
        maximum = 100
        step = 25

        # Setup the progressor
        arcpy.SetProgressor("step", "Validating Project file...", start, maximum, step)        
        time.sleep(readTime)
        # Add message to the results pane
        arcpy.AddMessage("Validating Project file...")

        #Project File
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)

        # Grabs the first instance of a map from the .aprx
        campus = project.listMaps('Map')[0]

        # Increment the progressor and change the label; add message to the results pane
        arcpy.SetProgressorPosition(start + step*1)
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Finding your map layer...")

        # Loop through the layers of the Map
        for layer in campus.listLayers():
            # check if the layer is a feature layer
            if layer.isFeatureLayer:
                # copy the layer's symbology
                symbology = layer.symbology
                # Make sure the symboloty has renderer attribute
                if hasattr(symbology, 'renderer'):
                    # check layer name
                    if layer.name == parameters[1].valueAsText:

                        # Increment the progressor and change the label; add message to the results pane
                        arcpy.SetProgressorPosition(start + step*2)
                        arcpy.SetProgressorLabel("Calculating and classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...")

                        # Update the copy's renderer to "Graduated Colors Renderer"
                        symbology.updateRenderer("GraduatedColorsRenderer")

                        # Tell arcpy which field we want to base our choropleth off of
                        symbology.renderer.classificationField = "Shape_Area"

                        # Increment Progressor
                        arcpy.SetProgressorPosition(start + step*3)
                        arcpy.SetProgressorLabel("Cleaning up...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Cleaning up...")

                        # Set how many classes we'll have for the map
                        symbology.renderer.breakCount = 5

                        # Set color Ramp
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]

                        # Set the layer's actual symbology equal to the copy's
                        layer.symbology = symbology

                        arcpy.AddMessage("Finish Generating Layer...")
                    else:
                        print("No layers found")

                    # Increment Progressor
        arcpy.SetProgressorPosition(start + step*4)
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving...")

        # Define output project
        outputLocation = parameters[2].valueAsText
        outputProjectName = parameters[3].valueAsText

        outputProject = outputLocation + "/" + outputProjectName + ".aprx"

        # Save a copy of the project
        project.saveACopy(outputProject)

        arcpy.AddMessage("Finished generating layer.")


    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
