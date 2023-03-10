# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# CreateMapUnitPolys.py
# Created on: 2023-03-08 09:21:39.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: CreateMapUnitPolys <ContactsAndFaults> <Polygons> 
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy

# Script arguments
ContactsAndFaults = arcpy.GetParameterAsText(0)

Polygons = arcpy.GetParameterAsText(1)

# Local variables:
MapUnit = Polygons
IdentityConfidence = MapUnit
Label = IdentityConfidence
Symbol = Label
DataSourceID = Symbol
Notes = DataSourceID
DataSource_ID = Notes

# Process: Feature To Polygon
arcpy.FeatureToPolygon_management(ContactsAndFaults, Polygons, "", "ATTRIBUTES", "")

# Process: Add MapUnit
arcpy.AddField_management(Polygons, "MapUnit", "LONG", "", "", "", "10", "NULLABLE", "NON_REQUIRED", "")

# Process: Add IdentityConfidence
arcpy.AddField_management(MapUnit, "IdentityConfidence", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Label
arcpy.AddField_management(IdentityConfidence, "Label", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Symbol
arcpy.AddField_management(Label, "Symbol", "TEXT", "", "", "254", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add DataSourceID
arcpy.AddField_management(Symbol, "DataSourceID", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Notes
arcpy.AddField_management(DataSourceID, "Notes", "TEXT", "", "", "254", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add DataSource_ID
arcpy.AddField_management(Notes, "DataSource_ID", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

