
import bpy 
import os 
import pathlib
import json

#This module is a preset implementation from scratch
#note that a preset system already exists in blender

BLENDER_VERSION = bpy.utils.resource_path("USER")                 #.../Blender Foundation/Blender/2.9x/
BLENDER_ADDON = os.path.join(BLENDER_VERSION,"scripts","addons")  #.../Blender Foundation/Blender/2.9x/scripts/addons/
BLENDER_USER = os.path.dirname(BLENDER_VERSION)                   #.../Blender Foundation/Blender/
BLENDER_DATA = os.path.join(BLENDER_USER,"data")                  #.../Blender Foundation/Blender/data/
PLUGIN_DATA = os.path.join(BLENDER_DATA,"Plugin-Profiler")        #.../Blender Foundation/Blender/data/Plugin-Profiler/
PLUGIN_PRESET = os.path.join(PLUGIN_DATA,"presets")               #.../Blender Foundation/Blender/data/Plugin-Profiler/presets/
TRACKER_PRESET = os.path.join(PLUGIN_PRESET,"exectracker")        #.../Blender Foundation/Blender/data/Plugin-Profiler/presets/exectracker/

def make_default_dirs():
    """generate the default preset directories"""
    for p in [ BLENDER_DATA, PLUGIN_DATA, PLUGIN_PRESET, TRACKER_PRESET,]:
        if (not os.path.exists(p)): 
            pathlib.Path(p).mkdir(parents=True, exist_ok=True)
    return None

def get_trackerpresets():
    for root, directories, file in os.walk(TRACKER_PRESET):
        for file in file: 
            if file.endswith(".json"):
                yield file.replace(".json","")

def trackerpreset_to_prefs(preset_path):
    """preset json file -> dict -> addon_prefs"""

    return None 

def prefs_to_trackerpreset(preset_path):
    """addon_prefs-> dict -> json file"""

    return None 

class PLUGINPROFILER_OT_add_trackerpreset(bpy.types.Operator):
    """save a preset"""

    bl_idname = "plugin_profiler.add_trackerpreset"
    bl_label = ""
    bl_description = ""
    bl_options = {'INTERNAL'}

    preset_name : bpy.props.StringProperty()

    def __init__(self):
        make_default_dirs()
        self.preset_path = os.path.join(TRACKER_PRESET,self.preset_name+".json")
        return None

    def execute(self, context):

        if (self.preset_name in ["","."," "]): #probably should do better check for that? user is not supposed to be dummy for this plugin
            def draw(self, context):
                self.layout.label(text="Please choose a valid preset name")
                return  None
            bpy.context.window_manager.popup_menu(draw, title="Operation Cannot be Done", icon="ERROR")
            return {'FINISHED'}

        """
        #prevent overwrite? 
        if os.path.exists(self.preset_path): 
            def draw(self, context):
                self.layout.label(text="This preset already exists")
                return  None
            bpy.context.window_manager.popup_menu(draw, title="Operation Cannot be Done", icon="ERROR")
            return {'FINISHED'}
        """

        #addon_prefs-> dict -> json file
        d = {}
        prefs = bpy.context.preferences.addons["Plugin-Profiler"].preferences
        d["exectracker_module_path"] =prefs.exectracker_module_path

        d["exectracker_modules_ignore"] = [m.name for m in prefs.exectracker_modules_ignore]
        d["exectracker_modules_ignore_idx"] = prefs.exectracker_modules_ignore_idx

        d["exectracker_modules_only"] = [m.name for m in  prefs.exectracker_modules_only]
        d["exectracker_modules_only_idx"] = prefs.exectracker_modules_only_idx

        d["exectracker_functions_ignore"] = [m.name for m in  prefs.exectracker_functions_ignore]
        d["exectracker_functions_ignore_idx"] = prefs.exectracker_functions_ignore_idx
        d["exectracker_functions_ignore_proxy"] = prefs.exectracker_functions_ignore_proxy

        d["exectracker_functions_only"] = [m.name for m in  prefs.exectracker_functions_only]
        d["exectracker_functions_only_idx"] = prefs.exectracker_functions_only_idx
        d["exectracker_functions_only_proxy"] = prefs.exectracker_functions_only_proxy

        d["exectracker_print_funcname"] = prefs.exectracker_print_funcname
        d["exectracker_print_funcdepth"] = prefs.exectracker_print_funcdepth
        d["exectracker_print_sourcepath"] = prefs.exectracker_print_sourcepath
        d["exectracker_print_datetime"] = prefs.exectracker_print_datetime
        d["exectracker_print_functime"] = prefs.exectracker_print_functime
        d["exectracker_ignore_listcomp"] = prefs.exectracker_ignore_listcomp

        with open(self.preset_path, 'w') as f:
            json.dump(d, f, indent=4)

        return {'FINISHED'}

class PLUGINPROFILER_OT_load_trackerpreset(bpy.types.Operator):
    """load a preset"""

    bl_idname = "plugin_profiler.load_trackerpreset"
    bl_label = ""
    bl_description = ""
    bl_options = {'INTERNAL','UNDO'}

    preset_name : bpy.props.StringProperty()

    def __init__(self):
        self.preset_path = os.path.join(TRACKER_PRESET,self.preset_name+".json")
        return None

    def execute(self, context):

        if (not os.path.exists(self.preset_path)): #improbable
            print("Plugin-Profiler: Looks like the preset you want to load do not exists")
            return {'FINISHED'}

        #preset json file -> dict -> addon_prefs
        prefs = bpy.context.preferences.addons["Plugin-Profiler"].preferences

        with open(self.preset_path) as f:
            d = json.load(f)

        if ("exectracker_module_path" in d):
            prefs.exectracker_module_path = d["exectracker_module_path"]

        if ("exectracker_modules_ignore" in d):
            prefs.exectracker_modules_ignore.clear()
            for n in d["exectracker_modules_ignore"]:
                e = prefs.exectracker_modules_ignore.add()
                e.name = n
        if ("exectracker_modules_ignore_idx" in d):
            prefs.exectracker_modules_ignore_idx = d["exectracker_modules_ignore_idx"]

        if ("exectracker_modules_only" in d):
            prefs.exectracker_modules_only.clear()
            for n in d["exectracker_modules_only"]:
                e = prefs.exectracker_modules_only.add()
                e.name = n
        if ("exectracker_modules_only_idx" in d):
            prefs.exectracker_modules_only_idx = d["exectracker_modules_only_idx"]

        if ("exectracker_functions_ignore" in d):
            prefs.exectracker_functions_ignore.clear()
            for n in d["exectracker_functions_ignore"]:
                e = prefs.exectracker_functions_ignore.add()
                e.name = n
        if ("exectracker_functions_ignore_idx" in d):
            prefs.exectracker_functions_ignore_idx = d["exectracker_functions_ignore_idx"]
        if ("exectracker_functions_ignore_proxy" in d):
            prefs.exectracker_functions_ignore_proxy = d["exectracker_functions_ignore_proxy"]

        if ("exectracker_functions_only" in d):
            prefs.exectracker_functions_only.clear()
            for n in d["exectracker_functions_only"]:
                e = prefs.exectracker_functions_only.add()
                e.name = n
        if ("exectracker_functions_only_idx" in d):
            prefs.exectracker_functions_only_idx = d["exectracker_functions_only_idx"]
        if ("exectracker_functions_only_proxy" in d):
            prefs.exectracker_functions_only_proxy = d["exectracker_functions_only_proxy"]

        if ("exectracker_print_funcname" in d):
            prefs.exectracker_print_funcname = d["exectracker_print_funcname"]
        if ("exectracker_print_funcdepth" in d):
            prefs.exectracker_print_funcdepth = d["exectracker_print_funcdepth"]
        if ("exectracker_print_sourcepath" in d):
            prefs.exectracker_print_sourcepath = d["exectracker_print_sourcepath"]
        if ("exectracker_print_datetime" in d):
            prefs.exectracker_print_datetime = d["exectracker_print_datetime"]
        if ("exectracker_print_functime" in d):
            prefs.exectracker_print_functime = d["exectracker_print_functime"]
        if ("exectracker_ignore_listcomp" in d):
            prefs.exectracker_ignore_listcomp = d["exectracker_ignore_listcomp"]

        return {'FINISHED'}

class PLUGINPROFILER_OT_remove_trackerpreset(bpy.types.Operator):
    """remove a preset"""

    bl_idname = "plugin_profiler.remove_trackerpreset"
    bl_label = ""
    bl_description = ""
    bl_options = {'INTERNAL'}

    preset_name : bpy.props.StringProperty()

    def __init__(self):
        self.preset_path = os.path.join(TRACKER_PRESET,self.preset_name+".json")
        return None

    def execute(self, context):

        if (not os.path.exists(self.preset_path)): #improbable
            print("Plugin-Profiler: Looks like the preset you want to delete do not exists")
            return {'FINISHED'}

        os.remove(self.preset_path)

        return {'FINISHED'}

class PLUGINPROFILER_PT_trackerpreset_panel(bpy.types.Panel):
    """draw preset popover panel"""

    bl_idname      = "PLUGINPROFILER_PT_trackerpreset_panel"
    bl_label       = ""
    bl_category    = ""
    bl_space_type  = "VIEW_3D"
    bl_region_type = "HEADER"

    def draw(self, context):

        prefs = bpy.context.preferences.addons["Plugin-Profiler"].preferences

        layout = self.layout
        row = layout.row()
        left = row.column()
        right = row.column()
        right.emboss = 'NONE'

        if (os.path.exists(TRACKER_PRESET)):
            for preset in get_trackerpresets(): 
                left.operator("plugin_profiler.load_trackerpreset", text=preset, emboss=False, ).preset_name = preset
                right.operator("plugin_profiler.remove_trackerpreset", text="", icon="REMOVE").preset_name = preset
            left.separator(factor=2)
            right.separator(factor=2)

        left.prop(prefs,"trackerpreset_name",text="")
        right.operator("plugin_profiler.add_trackerpreset", text="", icon="ADD").preset_name = prefs.trackerpreset_name

        return None