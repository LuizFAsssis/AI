from functions.get_files_info import get_files_info as gfi
from functions.get_file_content import get_file_content as gfc

def main():
  working_directory = "calculator"
  root_contents = gfi(working_directory, ".")
  print(root_contents)
  pkg_contents = gfi(working_directory, "pkg")
  print(pkg_contents)
  pkg_contents = gfi(working_directory, "/bin")
  print(pkg_contents)
  pkg_contents = gfi(working_directory, "../")
  print(pkg_contents)
  
  
main()