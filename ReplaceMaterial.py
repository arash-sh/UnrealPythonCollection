# Replace all material slots of static mesh actors with certain name
import unreal


##### complete undo may not be possible if too many operations performed

new_material = unreal.EditorAssetLibrary.load_asset("/Game/Materials/test_material")

actor_list = unreal.EditorLevelLibrary.get_all_level_actors()

	
for i in range(0, len(actor_list)):

	if actor_list[i].get_class() == unreal.StaticMeshActor.static_class():
		if  "EXTERIOR_WALL_VERTICAL_WOOD_SIDING" in actor_list[i].get_actor_label():
			for j in range(0, 8):
				old_material = actor_list[i].static_mesh_component.static_mesh.get_material(j)
				if old_material:
					actor_list[i].static_mesh_component.static_mesh.set_material(j, new_material)			
