import os
from google.genai import types

def write_file(working_directory, file_path, content):
  abs_working_dir = os.path.abspath(working_directory)
  target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

  valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

  if not valid_target_file:
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
  
  if os.path.isdir(target_file):
    return f'Error: Cannot write to "{file_path}" as it is a directory'
  
  if not os.path.isfile(target_file): 
    parent_dir = os.path.dirname(target_file) 
    
    try:
      os.makedirs(parent_dir, exist_ok=True)
    except Exception as e:
      return f'Error creating directories for "{file_path}": {str(e)}'
  
  try:
    with open(target_file, 'w') as f:
      f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  
  except Exception as e:
    return f'Error writing to file "{file_path}": {str(e)}'
  
schema_write_file = types.FunctionDeclaration(
  name="write_file",
  description="Writes if the file doesn't exist or overwrites content to a file in the working directory",
  parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
          "file_path": types.Schema(
              type=types.Type.STRING,
              description="Path to the file to be written, relative to the working directory is a required field",
          ),
          "content": types.Schema(
            type=types.Type.STRING,
            description="Content to write to the file is a required field",
          )
      },
  ),
)