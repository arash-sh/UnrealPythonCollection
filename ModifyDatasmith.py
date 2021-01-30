# Organize the actors of a udatasmith scene into layers based on their label and replace some materials.

datasmith_file = "D:/PythonProject/Content/Datasmith/Room.udatasmith"
datasmith_scene = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(datasmith_file)


# check scene initialization
if datasmith_scene is None:
	print "LoadDatasmith Failed"
	quit()

#
# ** pre import **
# change the actor's layer
actor_label = "Group_353"
for actor in datasmith_scene.get_all_mesh_actors():
    if actor_label in actor.get_label():
		actor.set_layer("Table")
		
#
# ** import **
# set the option on how to import the datasmith scene
option = unreal.DatasmithImportBaseOptions()

# import into a new level
# (since we import into a new level, you can't use Blutility because the Blutility actor will be destroyed at the creation of the new level)
option.scene_handling = unreal.DatasmithImportScene.NEW_LEVEL
option.include_camera = False
 option.include_light = True 
 option.include_goometry = True
 option.include_material = True 
 option.scene_handling = unreal.DatasmithImportScene.NEWLEVEL 
 option.hierarchy_handling = unreal.DatasmithImportHierarchy.USE_MULTIPLE_ACTORS 


# import datasmith scene in Unreal
destination_folder = "/Game/PythonImpoprt"
result = datasmith_scene.import_scene(destination_folder, option)

if not result.import_succeed:
	print "Import Failed"
	quit()

# # 
# ** post import **
# load materials
wood_material = unreal.EditorAssetLibrary.load_asset("/Game/PythonImpoprt/table/Materials/Color_F19")
if wood_material is None:
	print "The wood material can't be loaded"
	quit()

default_material = unreal.EditorAssetLibrary.load_asset("/Game/PythonImpoprt/table/Materials/Default")
if default_material is None:
	print "The default material can't be loaded"
	quit()

# find all StaticMesh Actor in the Level and place a certain material with another one.
actor_list = unreal.EditorLevelLibrary.get_all_level_actors()
actor_list = unreal.EditorFilterLibrary.by_class(actor_list, unreal.StaticMeshActor)
unreal.EditorLevelLibrary.replace_mesh_components_materials_on_actors(actor_list, default_material, wood_material)

