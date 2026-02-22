import os 
from google.genai import types

def get_files_info(working_directory, directory=None):
  # # Digamos que você rodou: python /mnt/c/Trabalhos/AI/main.py
  # # O CWD é /mnt/c/Trabalhos/AI/

  # os.path.abspath("calculator.py")
  # # Resultado: "/mnt/c/Trabalhos/AI/calculator.py"

  # os.path.abspath("functions")
  # # Resultado: "/mnt/c/Trabalhos/AI/functions"
  abs_working_dir = os.path.abspath(working_directory)
  
  if directory is None:
    target_dir = abs_working_dir
  else:
    target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
    
  #.join é usado para construir caminhos de forma segura, evitando problemas com separadores de diretórios em diferentes sistemas operacionais. Ele simplesmente concatena os argumentos usando o separador correto para o sistema operacional.
  # os.path.join("/mnt/c/Trabalhos/AI", "functions", "get_files_info.py")
  # # Resultado: "/mnt/c/Trabalhos/AI/functions/get_files_info.py"

  # os.path.join("/mnt/c/Trabalhos/AI", "calculator.py")
  # # Resultado: "/mnt/c/Trabalhos/AI/calculator.py"

  #.normpath é usado para normalizar um caminho, removendo quaisquer partes redundantes, como "." ou "..". Ele também resolve quaisquer separadores de diretórios duplicados.
  # os.path.normpath("/mnt/c/Trabalhos/AI/functions/../calculator.py")
  # # Resultado: "/mnt/c/Trabalhos/AI/calculator.py"
  # # O "functions/.." se cancelou — subiu e desceu

  # os.path.normpath("/mnt/c/Trabalhos/AI/./main.py")
  # # Resultado: "/mnt/c/Trabalhos/AI/main.py"
  # # O "./" foi removido pois não faz nada

  
  # .commonpath é usado para encontrar o caminho comum mais longo entre uma lista de caminhos. Ele retorna a parte do caminho que é compartilhada por todos os caminhos na lista.
  # Dado uma lista de caminhos, retorna o maior caminho que todos eles compartilham:
  # pythonos.path.commonpath([
  #     "/mnt/c/Trabalhos/AI/main.py",
  #     "/mnt/c/Trabalhos/AI/functions/get_files_info.py"
  # ])
  # # Resultado: "/mnt/c/Trabalhos/AI"
  # No contexto do agente, isso é a checagem de segurança. A lógica é:
  # python# working_directory = "/mnt/c/Trabalhos/AI"
  # # O agente pede pra acessar "../../etc/passwd" (tentando escapar)

  # target_dir = normpath(join("/mnt/c/Trabalhos/AI", "../../etc/passwd"))
  # # target_dir = "/mnt/c/etc/passwd"  (fora da jaula!)

  # commonpath(["/mnt/c/Trabalhos/AI", "/mnt/c/etc/passwd"])
  # # Resultado: "/mnt/c"  ← isso NÃO é igual ao working_directory!
  # # Então: acesso negado
  # Se o agente pedir algo válido como "functions":
  # pythontarget_dir = "/mnt/c/Trabalhos/AI/functions"

  # commonpath(["/mnt/c/Trabalhos/AI", "/mnt/c/Trabalhos/AI/functions"])
  # Resultado: "/mnt/c/Trabalhos/AI"  ← igual ao working_directory!
  # Então: acesso permitido

  valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
  
  if not valid_target_dir:
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  
  if not os.path.isdir(target_dir):
    return f'Error: "{directory}" is not a directory'
  
  final_response = ""
  contents = os.listdir(target_dir)
  for content in contents:
    content_path = os.path.join(target_dir, content)
    is_dir = os.path.isdir(content_path)
    size = os.path.getsize(content_path)
    final_response += f'-{content}: file_size={size}, is_dir={is_dir}\n'
  return final_response

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)