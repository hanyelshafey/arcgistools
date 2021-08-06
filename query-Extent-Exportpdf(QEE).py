# coding: utf-8
aprx = arcpy.mp.ArcGISProject("CURRENT")
mainMap = aprx.listMaps("Main Map")[0]
mainMap.name
# 'Main Map'
lyt = aprx.listLayouts()[0]
lyt.name
# 'Layout1'
countriesLayerMain = mainMap.listLayers("Countries")[0]
countriesLayerMain.definitionQuery = "NAME = 'Egypt'"
mainMapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Main Map Frame")[0]
selCountryExtent = mainMapFrame.getLayerExtent(countriesLayerMain)
mainMapFrame.camera.setExtent(selCountryExtent)
mainMapFrame.camera.scale=mainMapFrame.camera.scale * 1.05
lyt.exportToPDF(r"G:\GIS\arcpy\UDEMY ARCPY\test.pdf")
# 'G:\\GIS\\arcpy\\UDEMY ARCPY\\test.pdf'
