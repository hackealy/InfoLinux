import os
import sys
import platform

# Consulta o nome de usuário atual
print(os.getlogin())

# Consulta informações sobre a plataforma
print(platform.system())
print(platform.release())

# Consulta informações do sistema
print(sys.version_info)
print(os.cpu_count())
