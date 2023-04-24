bl_info = {
    "name": "Gather and Save Latest Version",
    "description": "Addon to gather latest file from specified path and save new version to same path",
    "author": "Vamps(Swapnil Nare)",
    "version": (1, 1),
    "blender": (3, 5, 0),
    "location": "View3D > Tool",
    "category": "Object"
}

import bpy
import os

class OBJECT_OT_gather_latest_version_operator(bpy.types.Operator):
    """Operator to gather latest version of specified file"""
    bl_idname = "object.gather_latest_version_operator"
    bl_label = "Gather Latest Version"

    file_path: bpy.props.StringProperty(name="File Path")

    def execute(self, context):
        # Get directory and file name from file path
        directory = os.path.dirname(self.file_path)
        file_name = os.path.basename(self.file_path)

        # Get list of all files in directory that match file name format (e.g. "file_v001.blend")
        files = [f for f in os.listdir(directory) if f.startswith(file_name[:-7]) and f.endswith(".blend")]

        if not files:
            # If no matching files found, do nothing
            return {'CANCELLED'}
        else:
            # Otherwise, get latest version number
            latest_version = 0
            for f in files:
                try:
                    version = int(f[-7:-6])
                    latest_version = max(latest_version, version)
                except ValueError:
                    pass


        # Create file path for latest version
        latest_file_name = f"{file_name[:-7]}_v{latest_version:03}.blend"
        latest_file_path = os.path.join(directory, latest_file_name)

        # Open latest version of file
        bpy.ops.wm.open_mainfile(filepath=latest_file_path)

        return {'FINISHED'}

class OBJECT_OT_save_new_version_operator(bpy.types.Operator):
    """Operator to save new version of specified file"""
    bl_idname = "object.save_new_version_operator"
    bl_label = "Save New Version"

    file_path: bpy.props.StringProperty(name="File Path")

    def execute(self, context):
        # Get directory and file name from file path
        directory = os.path.dirname(self.file_path)
        file_name = os.path.basename(self.file_path)

        # Get list of all files in directory that match file name format (e.g. "file_v001.blend")
        files = [f for f in os.listdir(directory) if f.startswith(file_name[:-7]) and f.endswith(".blend")]

        if not files:
            # If no matching files found, save new file as version 001
            new_version = 1
        else:
            # Otherwise, get latest version number and increment by 1
            latest_version = max([int(f[-7:-6]) for f in files])
            new_version = latest_version + 1

        # Create new file name with updated version number
        new_file_name = f"{file_name[:-7]}_v{new_version:03}.blend"
        new_file_path = os.path.join(directory, new_file_name)

        # Save copy of current Blender file as new version
        bpy.ops.wm.save_as_mainfile(filepath=new_file_path)

        return {'FINISHED'}

class OBJECT_PT_gather_and_save_latest_version_panel(bpy.types.Panel):
    """Panel for Gather and Save Latest Version addon"""
    bl_idname = "OBJECT_PT_gather_and_save_latest_version_panel"
    bl_label = "Gather and Save Latest Version"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Gather and Save"
    bl_order = 0

    def draw(self, context):
        layout = self.layout

        # Create text box for file path
        layout.prop(context.scene, "file_path")

        # Create button to gather latest version
        layout.operator("object.gather_latest_version_operator", text="Gather Latest Version").file_path = context.scene.file_path

        # Create button to save new version
        layout.operator("object.save_new_version_operator", text="Save New Version").file_path = context.scene.file_path

def register():
    bpy.utils.register_class(OBJECT_PT_gather_and_save_latest_version_panel)
    bpy.utils.register_class(OBJECT_OT_gather_latest_version_operator)
    bpy.utils.register_class(OBJECT_OT_save_new_version_operator)
    bpy.types.Scene.file_path = bpy.props.StringProperty(name="File Path")

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_gather_and_save_latest_version_panel)
    bpy.utils.unregister_class(OBJECT_OT_gather_latest_version_operator)
    bpy.utils.unregister_class(OBJECT_OT_save_new_version_operator)
    del bpy.types.Scene.file_path

if __name__ == "__main__":
    register()

