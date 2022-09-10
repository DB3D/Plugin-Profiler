
import bpy 
import os


class PLUGINPROFILER_PR_exectracker_modules_ignore(bpy.types.PropertyGroup):
    name : bpy.props.StringProperty()

class PLUGINPROFILER_PR_exectracker_modules_only(bpy.types.PropertyGroup):
    name : bpy.props.StringProperty()

class PLUGINPROFILER_PR_exectracker_functions_ignore(bpy.types.PropertyGroup):
    name : bpy.props.StringProperty()

class PLUGINPROFILER_PR_exectracker_functions_only(bpy.types.PropertyGroup):
    name : bpy.props.StringProperty()


class PLUGINPROFILER_AddonPref(bpy.types.AddonPreferences):
    """prefs = bpy.context.preferences.addons["Plugin-Profiler"].preferences"""
    
    bl_idname = "Plugin-Profiler"
        
    exectracker_module_path : bpy.props.StringProperty(
        subtype="DIR_PATH",
        default=os.path.join(bpy.utils.resource_path("USER"),"scripts","addons"),
        )
    
    exectracker_modules_ignore : bpy.props.CollectionProperty(
        type=PLUGINPROFILER_PR_exectracker_modules_ignore,
        )
    exectracker_modules_ignore_idx : bpy.props.IntProperty(
        default=0,
        )
    
    exectracker_modules_only : bpy.props.CollectionProperty(
        type=PLUGINPROFILER_PR_exectracker_modules_only,
        )
    exectracker_modules_only_idx : bpy.props.IntProperty(
        default=0,
        )
    
    exectracker_functions_ignore : bpy.props.CollectionProperty(
        type=PLUGINPROFILER_PR_exectracker_functions_ignore,
        )
    exectracker_functions_ignore_idx : bpy.props.IntProperty(
        default=0,
        )
    exectracker_functions_ignore_proxy : bpy.props.BoolProperty(
        default=False,
        )
    
    exectracker_functions_only : bpy.props.CollectionProperty(
        type=PLUGINPROFILER_PR_exectracker_functions_only,
        )
    exectracker_functions_only_idx : bpy.props.IntProperty(
        default=0,
        )
    exectracker_functions_only_proxy : bpy.props.BoolProperty(
        default=False,
        )

    exectracker_print_funcname : bpy.props.BoolProperty(
        default=True,
        )
    exectracker_print_funcdepth : bpy.props.IntProperty(
        default=2,
        min=0,
        soft_max=7,
        )
    exectracker_print_sourcepath : bpy.props.BoolProperty(
        default=False,
        )
    exectracker_print_datetime : bpy.props.BoolProperty(
        default=False,
        )
    exectracker_print_functime : bpy.props.BoolProperty(
        default=True,
        )
    exectracker_ignore_listcomp : bpy.props.BoolProperty(
        default=True,
        )

    def draw(self,context):

        from . interface import draw_interface
        draw_interface(self.layout)