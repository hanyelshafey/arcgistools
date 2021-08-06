# Enter your Queary
lyrname = input ("Enter your id")
row_id = input ("Enter your id")

# Set arcgisproject , main Map
aprx = arcpy.mp.ArcGISProject("CURRENT")
mainMap = aprx.listMaps("Map")[0]

# 'Main Map'
lyt = aprx.listLayouts()[0]
lyt.name
# 'Layout1'
countriesLayerMain = mainMap.listLayers(f"{lyrname}")[0]
countriesLayerMain.definitionQuery = f"id = '{row_id}'"
mainMapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Main Map Frame")[0]
selCountryExtent = mainMapFrame.getLayerExtent(countriesLayerMain)
mainMapFrame.camera.setExtent(selCountryExtent)
mainMapFrame.camera.scale=mainMapFrame.camera.scale * 1.05

