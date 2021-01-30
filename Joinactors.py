# Join static mesh actors based on their label

import unreal

# Find Actors whose label contains "Glazed"
actor_list = unreal.EditorLevelLibrary.get_all_level_actors()
actor_list = unreal.EditorFilterLibrary.by_class(actor_list, unreal.StaticMeshActor.static_class())
actor_list = unreal.EditorFilterLibrary.by_actor_label(actor_list, "Glazed*", unreal.EditorScriptingStringMatchType.MATCHES_WILDCARD)

# Join the selected actors into a new one and delete the old ones
join_options = unreal.EditorScriptingJoinStaticMeshActorsOptions()
join_options.new_actor_label = "Glazed"
join_options.destroy_source_actors = True
new_actor = unreal.EditorLevelLibrary.join_static_mesh_actors(actor_list, join_options);

new_actor.set_folder_path("Objects")
