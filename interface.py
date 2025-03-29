
import bpy 


class BaseNameList(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        layout.prop(item,"name", text="", emboss=False, )

class PLUGINPROFILER_UL_name_list1(BaseNameList): 
    pass

class PLUGINPROFILER_UL_name_list2(BaseNameList): 
    pass

class PLUGINPROFILER_UL_name_list3(BaseNameList): 
    pass

class PLUGINPROFILER_UL_name_list4(BaseNameList): 
    pass

class PLUGINPROFILER_OT_uilist_actions(bpy.types.Operator):
    """add/remove elements in uilist"""

    bl_idname = "plugin_profiler.uilist_actions"
    bl_label = ""
    bl_description = ""
    bl_options = {'INTERNAL','REGISTER',}

    group : bpy.props.StringProperty()
    action : bpy.props.StringProperty()
    default_name : bpy.props.StringProperty()

    def execute(self, context):

        prefs = bpy.context.preferences.addons["Plugin-Profiler"].preferences
        if (not hasattr(prefs,self.group)):
            return {'FINISHED'}

        group = getattr(prefs, self.group)
        group_idx_api =f"{self.group}_idx"
        group_idx = getattr(prefs,group_idx_api)

        if (self.action=="ADD"):
            s = group.add()
            s.name = self.default_name
            setattr(prefs,group_idx_api,len(group)-1)

        elif (self.action=="REMOVE"):
            group.remove(group_idx)
            if (group_idx>=len(group)):
                setattr(prefs,group_idx_api,len(group)-1)

        return {'FINISHED'}

def draw_interface(layout,):

    prefs = bpy.context.preferences.addons["Plugin-Profiler"].preferences
    uiwin = bpy.context.window_manager.plugin_profiler

    #draw exec tracker interface

    from . exectracker import PLUGINPROFILER_OT_exectracker
    is_running, op_txt, op_icon = PLUGINPROFILER_OT_exectracker.get_infos()

    boxalign = layout.column(align=True)

    box = boxalign.box()

    title = box.row()
    title.prop(uiwin,"ui_bool_exectracker", text="Execution Tracker", icon="CONSOLE", emboss=False,)
    title_preset = title.row()
    title_preset.emboss = "NONE"
    title_preset.popover(panel="PLUGINPROFILER_PT_trackerpreset_panel", text="", icon="PRESET")

    txt = box.column()
    txt.scale_y = 0.7
    txt.label(text="Print every functions executions happening in the background in your blender console")
    txt.label(text="You can choose to only consider/ignore some modules/functions below")
    
    box.separator(factor=0.1)

    if uiwin.ui_bool_exectracker:

        box = boxalign.box()
        
        prop = box.column(align=True)
        prop.label(text="Console Information:",)
        row = prop.row(align=True)
        row.prop(prefs, "exectracker_print_funcname", text="FctName", icon="BLANK1")
        row.prop(prefs, "exectracker_print_sourcepath", text="FilePath", icon="BLANK1")
        row.prop(prefs, "exectracker_print_datetime", text="CallTime", icon="BLANK1")
        row.prop(prefs, "exectracker_print_functime", text="ExecTime", icon="BLANK1")

        if prefs.exectracker_print_funcname:
          prop.prop(prefs, "exectracker_print_funcdepth", text="FctName Path Depth")

        box.separator(factor=0.2)

        prop = box.column(align=True)
        prop.label(text="Only Listen to Module:",)
        prop.prop(prefs, "exectracker_module_path", text="")

        box.separator(factor=0.2)

        row = box.row()

        col = row.column(align=True)
        col.label(text="Ignore Sub-Modules:",)
        ui_list = col.row()
        ui_list.template_list("PLUGINPROFILER_UL_name_list1", "", prefs, "exectracker_modules_ignore", prefs, "exectracker_modules_ignore_idx", type="DEFAULT", rows=6,)
        ui_list_op = ui_list.column(align=True)
        op = ui_list_op.operator("plugin_profiler.uilist_actions", text="", icon="ADD") ; op.group = "exectracker_modules_ignore" ; op.action = "ADD" ; op.default_name = "my_module_name"
        op = ui_list_op.operator("plugin_profiler.uilist_actions", text="", icon="REMOVE") ; op.group = "exectracker_modules_ignore" ; op.action = "REMOVE"

        col = row.column(align=True)
        col.label(text="Only Listen to Sub-Modules:",)
        ui_list = col.row()
        ui_list.template_list("PLUGINPROFILER_UL_name_list2", "", prefs, "exectracker_modules_only", prefs, "exectracker_modules_only_idx", type="DEFAULT", rows=6,)
        ui_list_op = ui_list.column(align=True)
        op = ui_list_op.operator("plugin_profiler.uilist_actions", text="", icon="ADD") ; op.group = "exectracker_modules_only" ; op.action = "ADD" ; op.default_name = "my_module_name"
        op = ui_list_op.operator("plugin_profiler.uilist_actions", text="", icon="REMOVE") ; op.group = "exectracker_modules_only" ; op.action = "REMOVE"

        row = box.row()

        col = row.column(align=True)
        col.label(text="Ignore Functions:",)
        ui_list = col.row()
        ui_list.template_list("PLUGINPROFILER_UL_name_list3", "", prefs, "exectracker_functions_ignore", prefs, "exectracker_functions_ignore_idx", type="DEFAULT", rows=6,)
        col.prop(prefs,"exectracker_functions_ignore_proxy", text="Approximative Match",)
        ui_list_op = ui_list.column(align=True)
        op = ui_list_op.operator("plugin_profiler.uilist_actions", text="", icon="ADD") ; op.group = "exectracker_functions_ignore" ; op.action = "ADD" ; op.default_name = "my_function_name"
        op = ui_list_op.operator("plugin_profiler.uilist_actions", text="", icon="REMOVE") ; op.group = "exectracker_functions_ignore" ; op.action = "REMOVE"

        col = row.column(align=True)
        col.label(text="Only Listen to Functions:",)
        ui_list = col.row()
        ui_list.template_list("PLUGINPROFILER_UL_name_list4", "", prefs, "exectracker_functions_only", prefs, "exectracker_functions_only_idx", type="DEFAULT", rows=6,)
        col.prop(prefs,"exectracker_functions_only_proxy", text="Approximative Match",)
        ui_list_op = ui_list.column(align=True)
        op = ui_list_op.operator("plugin_profiler.uilist_actions", text="", icon="ADD") ; op.group = "exectracker_functions_only" ; op.action = "ADD" ; op.default_name = "my_function_name"
        op = ui_list_op.operator("plugin_profiler.uilist_actions", text="", icon="REMOVE") ; op.group = "exectracker_functions_only" ; op.action = "REMOVE"

        box.separator(factor=0.2)

        button = box.row()
        button.scale_y = 1.2
        button.operator("pluginprofiler.exectracker", text=op_txt, icon=op_icon, depress=is_running,)

    #draw benchmarker interface 

    from . benchmarker import PLUGINPROFILER_OT_benchmarker
    is_running, op_txt, op_icon = PLUGINPROFILER_OT_benchmarker.get_infos()

    boxalign = layout.column(align=True)

    box = boxalign.box()

    title = box.row()
    title.prop(uiwin,"ui_bool_benchmarker", text="Benchmarking Tool", icon="SORTSIZE", emboss=False,)
    txt = box.column()
    txt.scale_y = 0.7
    txt.label(text="Record your python actions using the cProfile module, then generate a banchmark")
    txt.label(text="If you'd like to use the viz app, please 'pip install snakeviz' on your local console")
    txt.label(text="We'll automatically call the visualization window from the subprocess.Popen() function")
    
    box.separator(factor=0.1)

    if uiwin.ui_bool_benchmarker:

        box = boxalign.box()

        button = box.row()
        button.scale_y = 1.2
        button.operator("pluginprofiler.benchmarker", text=op_txt, icon=op_icon, depress=is_running,)
        
        box.separator(factor=0.1)

        button = box.row()
        button.operator("plugin_profiler.benchmarkops", text="Console-Print Result",).operation = "print"

        button = box.row()
        button.operator("plugin_profiler.benchmarkops", text="Run SnakeViz",).operation = "run_viz"

        button = box.row()
        button.operator("plugin_profiler.benchmarkops", text="Save Log",).operation = "save_log"

    return None 