# Import a datasmith file and possibly place it in the scene 
import unreal

# Add proper file directory and open a udatasmith scene
datasmith_file = "D:/PythonProject/Content/Datasmith/Room.udatasmith"
datasmith_scene = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(datasmith_file)

# check scene initialization
if datasmith_scene is None:
	print "LoadDatasmith Failed"
	quit()
		
#
# ** import **
# set the option on how to import the datasmith scene
option = unreal.DatasmithImportBaseOptions()

# import into a new level
option.include_camera = False
option.include_light = False 
option.include_geometry = True
option.include_material = True 
option.scene_handling = unreal.DatasmithImportScene.CURRENT_LEVEL # Whether and where to spawn. options: ASSETS_ONLY, CURRENT_LEVEL, NEW_LEVEL
# option.hierarchy_handling = unreal.DatasmithImportHierarchy.USE_MULTIPLE_ACTORS 


# import datasmith scene in Unreal
destination_folder = "/Game/ModelImport"
result = datasmith_scene.import_scene(destination_folder, option)

if not result.import_succeed:
	print "Import Failed"
	quit()
