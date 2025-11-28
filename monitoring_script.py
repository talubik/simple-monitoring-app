import requests
import subprocess
import time
from datetime import datetime
import argparse

APP_URL = 'http://127.0.0.1:5000'
LOG_FILE = '/var/log/app_monitor.log'
CHECK_INTERVAL = 10

def log(message):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.now()}: {message}\n") # Функция для логирования событий
    print(message)

def is_app_running():
    try:
        response = requests.get(APP_URL, timeout=5) # Проверка доступности приложения
        return response.status_code == 200
    except requests.RequestException:
        return False
    

def start_app():
    subprocess.Popen(['python3', args.app_path]) # Запуск Flask приложения, если оно не запущено или недоступно
    log("Flask app started.")
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Monitor and restart the Flask app if it goes down.')
    parser.add_argument('--app-path', type=str, required=True, help='Path to the Flask app script.')
    args = parser.parse_args()
    while True:
        if is_app_running():
            log("App is running.")
        else:
            log("App is down, restarting...")
            start_app()
        time.sleep(CHECK_INTERVAL)
