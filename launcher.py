# minecraft launcher starter file
# Fungi minecraft launcher
# made by @blackbucket007

import subprocess
import os

from config import JAR_PATH, JAVA_PATH, RAM_USED

def start_minecraft(player_name):
    """Запуск minecraft c указанным в run_minecraft ником"""
    if not player_name:
        return "Ошибка: Поле ввода никнейма не может быть пустым.\nВведите никнейм!"
    
    if not os.path.exists(JAR_PATH):
        return f"Ошибка: Файл {JAR_PATH} не найден. Проверь путь и версию.\nНаписать разработчику: tg@blackbucket007"
        
    minecraft_command = [
        JAVA_PATH,
        f"-Xmx{RAM_USED}", # ограничение по памяти
        "-jar", JAR_PATH,
        "--username", player_name
    ]
    
    try:
        subprocess.run(minecraft_command)
        return f"{player_name} minecraft запущен успешно!"
    except Exception as en:
        return f"Ошибка запуска: {en}"