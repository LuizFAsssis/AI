from functions.get_file_content import get_file_content as gfc

def main():
  working_directory = "calculator"
  result = gfc(working_directory, "lorem.txt")
  print(result)
  result = gfc("calculator", "main.py")
  print(result)
  result = gfc("calculator", "pkg/calculator.py")
  print(result)
  result = gfc("calculator", "/bin/cat")
  print(result)
  result = gfc("calculator", "pkg/does_not_exist.py")
  print(result)

main()