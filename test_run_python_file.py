from functions.run_python_file import run_python_file as rpf

def main():
  working_directory = "calculator"
  print(rpf("calculator", "main.py")) # (should print the calculator's usage instructions)
  print(rpf("calculator", "main.py", ["3 + 5"])) # (should run the calculator... which gives a kinda nasty rendered result)
  print(rpf("calculator", "tests.py")) # (should run the calculator's tests successfully)
  print(rpf("calculator", "../main.py")) # (this should return an error)
  print(rpf("calculator", "nonexistent.py")) # (this should return an error)
  print(rpf("calculator", "lorem.txt")) # (this should return an error)  

main()