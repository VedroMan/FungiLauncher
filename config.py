# minecraft launcher configuration file
# Fungi minecraft launcher
# made by @blackbucket007

import os
import sys

# определение пути к minecraft в зависимости от OS
if sys.platform == "win32": # windows
    MINECRAFT_DIR = os.path.expanduser("~/AppData/Roaming/.minecraft")
elif sys.platform == "darwin": # macOS
    MINECRAFT_DIR = os.path.expanduser("~/Library/Application Support/minecraft")
else:
    MINECRAFT_DIR = os.path.expanduser("~/.minecraft")

""" Основные настройки для minecraft """

MINECRAFT_VERSION = "OptiFine 1.21.1" # версия
JAVA_PATH = "java" # путь к java
RAM_USED = "4G" # Количество оперативной памяти

""" Пути к важным директориям """

VERSIONS_DIR = os.path.join(MINECRAFT_DIR, "versions")
MODS_DIR = os.path.join(MINECRAFT_DIR, "mods")
JAR_PATH = os.path.join(VERSIONS_DIR, MINECRAFT_VERSION, f"{MINECRAFT_VERSION}.jar") # путь к jar-файлам
