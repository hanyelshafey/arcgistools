# Enter your Queary
row_id = input ("Enter your id")

# Set arcgisproject , main Map
aprx = arcpy.mp.ArcGISProject("CURRENT")
mainMap = aprx.listMaps("Map")[0]

# 'Main Map'
lyt = aprx.listLayouts()[0]
lyt.name
# 'Layout1'
parcelLayerMain = mainMap.listLayers("parcel")[0]
parcelLayerMain.definitionQuery = f"parcel_id = '{row_id}'"
mainMapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Map Frame")[0]
selParcelExtent = mainMapFrame.getLayerExtent(parcelLayerMain)
mainMapFrame.camera.setExtent(selParcelExtent)
mainMapFrame.camera.scale=mainMapFrame.camera.scale * 1.05
lyt.exportToJPEG(f"G:\{row_id}.jpg")
