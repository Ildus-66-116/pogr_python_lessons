import os
from pathlib import Path

print(os.getcwd())      # показывает текущий каталог
print(Path.cwd())       # показывает текущий каталог более современный

os.chdir('../../..')       # изменяет текущий каталог на две папки выше
print(Path.cwd())
