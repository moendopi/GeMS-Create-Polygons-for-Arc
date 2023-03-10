# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# CreateOverlayPolys.py
# Created on: 2023-03-08 09:12:01.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: CreateOverlayPolys <OverlayLines> <Polygons> 
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy

# Script arguments
OverlayLines = arcpy.GetParameterAsText(0)

Polygons = arcpy.GetParameterAsText(1)

# Local variables:
Type = Polygons
IdentityConfidence = Type
Label = IdentityConfidence
Symbol = Label
DataSource = Symbol
Notes = DataSource
OverlayPolys_ID = Notes

# Process: Feature To Polygon
arcpy.FeatureToPolygon_management(OverlayLines, Polygons, "", "ATTRIBUTES", "")

# Process: Add Type
arcpy.AddField_management(Polygons, "Type", "TEXT", "", "", "254", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add IdentityConfidence
arcpy.AddField_management(Type, "IdentityConfidence", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Label
arcpy.AddField_management(IdentityConfidence, "Label", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Symbol
arcpy.AddField_management(Label, "Symbol", "TEXT", "", "", "254", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add DataSource
arcpy.AddField_management(Symbol, "DataSource", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Notes
arcpy.AddField_management(DataSource, "Notes", "TEXT", "", "", "254", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add OverlayPolys_ID
arcpy.AddField_management(Notes, "OverlayPolys_ID", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

