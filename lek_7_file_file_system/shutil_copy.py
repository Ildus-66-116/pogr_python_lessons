import shutil

shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir')      # копирует еще методанные

shutil.copytree('dir', 'one_more_dir')

shutil.rmtree('dir')    # удаляет все и то что внутри
