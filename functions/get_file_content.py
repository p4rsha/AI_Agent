import os
from google.genai import types

from config import MAX_CHARS



def get_file_content(working_directory, file_path):
    
    try:

        working_directory_abs = os.path.abspath(working_directory)

        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

        #check if valid target path

        valid_target_file_path = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

        if not valid_target_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        #processing target file



        with open(target_file) as f:

            file_content_string = f.read(MAX_CHARS)
            
            #check if the file had more than MAX_CHARS , and if so, let the AI know!
            if f.read(1):
                file_content_string +=  f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content_string

    except Exception as e:

        return f'The program encountered the following Error : {e}'
    

# Function Schema

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the contents of a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)