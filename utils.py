
import bpy 


def list_interection(lst1, lst2):
    """return common elements of two lists"""
    return set(lst1).intersection(lst2)

def list_have_common_elements(lst1, lst2):
    """return if two lists have common elements"""
    return bool(list_interection(lst1, lst2))

class RunningOperator(bpy.types.Operator):
    """base class used by exectracker/benchmarker operators"""

    bl_idname = ""
    bl_label = ""
    bl_description = ""
    bl_options = {'INTERNAL'}
    
    is_running = False

    @classmethod
    def get_infos(cls):
        """operator ui might differ if operator is running in background or not
        return (is_running, Start/Stop name, PAUSE/PLAY icon)"""
        if cls.is_running: 
              return (cls.is_running, "Stop", "PAUSE")
        else: return (cls.is_running, "Start", "PLAY")

    @classmethod
    def running_status(cls, setter:bool=None):
        if (setter is None):
            return cls.is_running
        cls.is_running = setter
        return None

    def execute(self, context):
        
        if (self.running_status()==True):
            self.end()
            self.running_status(setter=False)
        else: 
            self.running_status(setter=True)
            self.start()

        return {'FINISHED'}

    def start(self):
        pass #children defined

    def end(self):
        pass #children defined