# Merge all static mesh actors (either based on layer or level)
import unreal

## merges actors based on label
# actor_list = unreal.EditorLevelLibrary.get_all_level_actors()
# actor_list = unreal.EditorFilterLibrary.by_class(actor_list, unreal.StaticMeshActor.static_class())
# actor_list = unreal.EditorFilterLibrary.by_actor_label(actor_list, "*", unreal.EditorScriptingStringMatchType.MATCHES_WILDCARD) 

## merges actors based on layer
levelname = unreal.GameplayStatics.get_current_level_name(unreal.EditorLevelLibrary.get_editor_world())
actor_list = unreal.EditorFilterLibrary.by_layer(unreal.EditorLevelLibrary.get_all_level_actors(), "Walls") # Find all actors in layer

# Set the option and merge the selected static meshe actors
merge_options = unreal.EditorScriptingMergeStaticMeshActorsOptions()
merge_options.new_actor_label = "MergedActor" 
merge_options.base_package_name = "/Game/peavy/OSU_Peavy_Central_RC16_2019_03_05/MergedAsset" # Path to new asset
merge_options.destroy_source_actors = True # Delete the old actor
result = unreal.EditorLevelLibrary.merge_static_mesh_actors(actor_list, merge_options)

