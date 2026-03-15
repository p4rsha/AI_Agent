import os

def get_files_info(working_directory, directory="."):

    try:

        wd_abs_path = os.path.abspath(working_directory)

        target_dir = os.path.normpath(os.path.join(wd_abs_path, directory))

        # Will be True or False
    
        valid_target_dir = os.path.commonpath([wd_abs_path, target_dir]) == wd_abs_path

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
    
        #processing the valid target dir
        dir_content = os.listdir(target_dir)

        lines = []
        for content in dir_content:
            full_path = os.path.join(target_dir, content)
            lines.append(f"- {content}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}")

        return "\n".join(lines)
    
    except Exception as e:
        return f'The program encountered the following Error : {e}'