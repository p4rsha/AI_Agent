from google.genai import types

from functions.get_files_info import schema_get_files_info , get_files_info
from functions.get_file_content import schema_get_file_content , get_file_content
from functions.write_file import schema_write_file , write_file
from functions.run_python_file import schema_run_python_file , run_python_file

available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],
)


def call_function(function_call, verbose=False):

    # Print to console the operation that is about to happen with the call_function function
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")

    else:
        print(f" - Calling function: {function_call.name}")

    # determine which of the four functions to call (if any)
    function_map = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "write_file": write_file,
    "run_python_file": run_python_file
    }

    # Failsafe : Function name could be None
    function_name = function_call.name or ""

    # Return a type object that tells Gemini the details of the error if the function name it passed to call_function has no match in the map
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    #now, take the function_call.args , add working directory to it so we can pass the correct inputs to our functions. Also, we use shallow copy here so 
    # our program does not crash if .args is fucked AND we can mutate the args without messing up the AI .args input
   
    args = dict(function_call.args) if function_call.args else {}

    args["working_directory"] = "./calculator"

    # Call the function and save its output in a variable -- remember, we need to give Gemini the response back in string! Also, use **args to unpack dict into keyword args!

    func_call_result = function_map[function_name](**args)

    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": func_call_result},
                )
            ],
        )