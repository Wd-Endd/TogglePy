from os import path

from config import Config
from utils.toggle import toggle

file_target = path.abspath(Config.file_target)
on_state = Config.on_state
off_state = Config.off_state

with open(file_target, "r") as f:
    content = f.read()
# print(content);

modifiedContent = None
for i in range(0, len(on_state)):
    modifiedContent = toggle(content, off_state[i], on_state[i])
    content = modifiedContent

# print(modifiedContent)
if modifiedContent:
    with open(file_target, "w") as f:
        f.write(modifiedContent)
