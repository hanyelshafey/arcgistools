# Enter your Queary
row_id = input ("Enter your id")

# Set arcgisproject , main Map
try:
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    mainMap = aprx.listMaps("Map")[0]
    # 'Main Map'
    lyt = aprx.listLayouts()[0]
    # 'Layout1'
    parcelLayerMain = mainMap.listLayers("parcel")[0]
    parcelLayerMain.definitionQuery = f"parcel_id = '{row_id}'"
    mainMapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Map Frame")[0]
    selParcelExtent = mainMapFrame.getLayerExtent(parcelLayerMain)
    mainMapFrame.camera.setExtent(selParcelExtent)
    mainMapFrame.camera.scale=mainMapFrame.camera.scale * 1.05
    lyt.exportToJPEG(f"G:\{row_id}.jpg")
except:
    print("Check your layout and layer name 'parcel' and field name 'parcel_id'")
