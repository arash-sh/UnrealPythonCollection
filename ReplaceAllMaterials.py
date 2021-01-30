# Replaces all materials used in the scene with those materials with the same label placed in a new folder
# Usefull when all the existing materials need to be replaced with new ones
import unreal

old_mat_path = "/Game/ModelImport/Room/Materials" # Path to old material assets
new_mat_path = "/Game/Materials" # Path to new material assets

# Get all static mesh actors in the scene
actor_list = unreal.EditorLevelLibrary.get_all_level_actors()
actor_list = unreal.EditorFilterLibrary.by_class(actor_list, unreal.StaticMeshActor.static_class()) 

# Find all the assets on the "old" folder 
mat_list=unreal.EditorAssetLibrary.list_assets(old_mat_path, recursive=False, include_folder=False) 

for i in range(0, len(mat_list)):
	old_material = unreal.EditorAssetLibrary.load_asset(mat_list[i])
	if old_material is None:
		print "The old material can't be loaded"
		quit()
	mat_name = mat_list[i].split('/')[-1].split('.')[-1] # Get material name from asset
	# In the 'new' folder, find the material that has the same name as the old material
	new_material = unreal.EditorAssetLibrary.load_asset(new_mat_path+'/'+mat_name)
	if new_material is None:
		print "The new material can't be loaded"
		quit()	
	else:
		print new_material
	# Replace materials	
	unreal.EditorLevelLibrary.replace_mesh_components_materials_on_actors(actor_list, old_material, new_material)
	


