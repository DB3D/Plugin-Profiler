
import bpy 
import os 
import Path
import json

BLENDER_VERSION = bpy.utils.resource_path("USER")                 #.../Blender Foundation/Blender/2.9x/
BLENDER_ADDON = os.path.join(BLENDER_VERSION,"scripts","addons")  #.../Blender Foundation/Blender/2.9x/scripts/addons/
BLENDER_USER = os.path.dirname(BLENDER_VERSION)                   #.../Blender Foundation/Blender/
BLENDER_DATA = os.path.join(BLENDER_USER,"data")                  #.../Blender Foundation/Blender/data/
PLUGIN_DATA = os.path.join(BLENDER_DATA,"Plugin-Profiler")        #.../Blender Foundation/Blender/data/Plugin-Profiler/
PLUGIN_PRESET = os.path.join(PLUGIN_DATA,"presets")               #.../Blender Foundation/Blender/data/Plugin-Profiler/presets/
TRACKER_PRESET = os.path.join(PLUGIN_DATA,"exectracker")          #.../Blender Foundation/Blender/data/Plugin-Profiler/presets/exectracker/

def make_default_dirs():
    """generate the default preset directories"""
    for p in [ BLENDER_DATA, PLUGIN_DATA, PLUGIN_PRESET, TRACKER_PRESET,]:
        if (not os.path.exists(p)): 
            Path(p).mkdir(parents=True, exist_ok=True)
    return None

def trackerpreset_to_prefs(preset_path):
    """preset json file -> dict -> addon_prefs"""

    return None 

def prefs_to_trackerpreset():
    """addon_prefs-> dict -> json file"""

    return None 

class PLUGINPROFILER_OT_add_trackerpreset(bpy.types.Operator):
    """save a preset"""

    bl_idname = "plugin_profiler.add_trackerpreset"
    bl_label = ""
    bl_description = ""
    bl_options = {'INTERNAL'}

    preset_name : bpy.props.StringProperty()

    def execute(self, context):

        return {'FINISHED'}

class PLUGINPROFILER_OT_remove_trackerpreset(bpy.types.Operator):
    """remove a preset"""

    bl_idname = "plugin_profiler.remove_trackerpreset"
    bl_label = ""
    bl_description = ""
    bl_options = {'INTERNAL'}

    preset_name : bpy.props.StringProperty()

    def execute(self, context):

        return {'FINISHED'}


class PLUGINPROFILER_PT_scatter_preset_header(bpy.types.Panel):

    bl_idname      = "PLUGINPROFILER_PT_scatter_preset_header"
    bl_label       = ""
    bl_category    = ""
    bl_space_type  = "VIEW_3D"
    bl_region_type = "HEADER"

    def draw(self, context):
        layout = self.layout
        layout.label(text="")
        return None