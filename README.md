# UnrealPythonCollection

Collection of a few python scripts for processing actors and assets in Unreal Engine, especially useful when importing large datasmith files.
List of scripts:

 -  ImportDataSmith.py: Import a datasmith file and possibly place it in a new scene 
 - Joinactors.py: Join static mesh actors based on their label
 - MergeMeshes.py: Merge all static mesh actors selected either based on layer or label
 - ModifyDatasmith.py: Organize the actors of a datasmith scene into layers based on their label and replace certain materials
 - ReadMetadata.py: For all static mesh actors, read the metadata (datasmith user data) corresponding to certain keys and write the values into a CSV file
 - ReplaceAllMaterials.py: Replace all materials used in the scene with those materials with the same label selected from a new folder
 - ReplaceMaterial.py: Replace all material slots of static mesh actors with certain label
 - ShowProgress.py: Template for showing a progress bar while performing slow tasks
 - SpawnLights.py: Spawn a point light for every actor that has "Lamp" in its label 

The Unreal Python API reference can be found [here](https://docs.unrealengine.com/en-US/PythonAPI/index.html)