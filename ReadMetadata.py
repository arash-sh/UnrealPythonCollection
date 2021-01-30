# For all static mesh actors, read the metadata (datasmith user data) corresponding to certain keys and write the values as CSV file
import unreal
import os 

# List of metadata key that are of interest
keys = ["Datasmith_UniqueId", "Description", "Material", "Struct__Matl", "Cost", "Absorptance", "Base_Constraint", "Base_Offset", "Fire_Rating", "Function", "Insulation", "Location_Line", "Phase_Created", "STC", "Top_Constraint", "Top_Offset", "Type_Mark", "Workset", "Elevation", "Height", "Length", "Width"]
delim = ";" # delimiter in CSV file
dirPath = os.path.dirname(os.path.realpath(__file__))
f = open(dirPath+"\metadata.csv", "w+")  # Open CSV file

#print unreal.DatasmithContentLibrary.get_all_datasmith_user_data(unreal.StaticMeshActor.static_class())

actors = unreal.EditorLevelLibrary.get_all_level_actors()
actors = unreal.EditorFilterLibrary.by_class(actors, unreal.StaticMeshActor.static_class()) 

f.write( "Label" + delim+ delim.join(keys) + "\n") # write the header line for file

count = len(actors)
message = ""

with unreal.ScopedSlowTask(count, message) as slow_task:
	slow_task.make_dialog(True)               # Makes the dialog visible, if it isn't already

	for i in range(0, count):
		if slow_task.should_cancel():         # True if the user has pressed Cancel in the UI
			break
		actorLabel = actors[i].get_actor_label().encode('ascii', 'replace')
		message = "Working on " + actorLabel + " ( "+ str(i+1) + " / " + str(count) + " )"
		slow_task.enter_progress_frame(1, message)     # Advance progress by one frame.
		row = actorLabel
		for j in range(0, len(keys)):
			val = unreal.DatasmithContentLibrary.get_datasmith_user_data_value_for_key(actors[i],keys[j]) # Get the value for each metadata key
			row = row+ delim +val.encode('ascii', 'replace') # Write the metadata value to file

		f.write(row + "\n")
		
f.close()

#### hide objects in editor with specific key-value combination
# [actors, values]= unreal.DatasmithContentLibrary.get_all_objects_and_values_for_key("Description", unreal.StaticMeshActor.static_class())
# for i in range(0, len(actors)):
	# if values[i] == "Exterior Cladding":
		# actors[i].set_is_temporarily_hidden_in_editor(True)	
	#print  actors[i].get_actor_label()  + ";" + values[i] 


		
