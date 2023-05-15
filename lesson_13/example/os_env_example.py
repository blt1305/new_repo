import os

print(os.environ) # напечатать переменные окружения

print(f"tms env variable {os.environ.get('tms')}") # вывести переменную окружения

os.environ["tms"] = "example"
print(f"tms env variable {os.environ.get('tms')} (after set)") # вывести переменную окружения
