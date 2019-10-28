import subprocess

import sys

# 1. Сетевые интерфейсы
result = subprocess.call(["ip", "a"])
print("ip a: ", result)

# 2. Маршрут по умолчанию
result = subprocess.call(["ip", "к"])
print("ip r: ", result)

# 3. Информацию о состоянии процессора
result = subprocess.call(["ps", "ax"])
print("ps ax: ", result)

# 4. Информацию о процессе
result = subprocess.call(["ps", "-o", "user,args,group", "-C", "python"])
print("ps -o user,args,group -C python: ", result)

# 5. Список всех процессов
result = subprocess.call(["ps", "-A"])
print("ps -A: ", result)

# 6. Статистику работы сетевых интерфейсов
result = subprocess.call(["iftop"])
print("iftop: ", result)

# 7. Статус работы какого либо сервиса
result = subprocess.call(["service", "docker", "status"])
print("status docker: ", result)

# 8. Состояние сетевого порта на сервере (TCP или UDP)
result = subprocess.call(["netstat", "-ltp"])
print("status docker: ", result)

# 9. Версию пакета (имя пакета передается как аргумент)
package_name = sys.argv[1]
result = subprocess.call([package_name, "--version"])
print("{} --version: {}".format(package_name, result))

# 10. Список в файлов в директории (указать директорию)
directory = sys.argv[1]
result = subprocess.call(["ls", directory])
print("ls {}: {}".format(directory, result))

# 11. Текущую директорию
result = subprocess.call(["ls"])
print("ls: {}".format(result))

# 12. Версию ядра
result = subprocess.call(["uname", "-r"])
print("uname -r: {}".format(result))

# 13. Версию операционной системы
result = subprocess.call(["lsb_release ", "-ф"])
print("lsb_release  -ф: {}".format(result))
