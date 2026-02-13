import os 

def get_files_info(working_directory, directory=None):
  abs_working_dir = os.path.abspath(working_directory)
  if directory is None:
    directory = working_directory
  abs_directory = os.path.abspath(directory)
  target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
  # Will be True or False
  valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
  
  if not valid_target_dir:
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  
  if not abs_directory.startswith(abs_working_dir):
    return f'Error: "{directory}" is not a directory'
  
  final_response = ""
  contents = os.listdir(abs_directory)
  for content in contents:
    content_path = os.path.join(abs_directory, content)
    is_dir = os.path.isdir(content_path)
    size = os.path.getsize(content_path)
    final_response += f'-{content}: filze_size={size}, is_dir={is_dir}'
  return final_response