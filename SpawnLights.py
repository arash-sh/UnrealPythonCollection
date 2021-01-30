# Spawn a point light for every actor that has "Lamp" in its label 
import unreal

actor_list = unreal.EditorLevelLibrary.get_all_level_actors()

for i in range(0, len(actor_list)):
	if  "Lamp" in actor_list[i].get_actor_label():
		loc = unreal.Actor.get_actor_location(actor_list[i]) 
		print actor_list[i].get_actor_bounds(True)
		light = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.PointLight.static_class(),loc)
	