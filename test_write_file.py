from functions.write_file import write_file as wf

def main():
  working_directory = "calculator"
  print(wf("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
  print(wf("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
  print(wf("calculator", "/tmp/temp.txt", "this should not be allowed"))
  
main()