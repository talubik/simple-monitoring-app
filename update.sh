#!/bin/bash

# Копируем файлы приложения и скрипта мониторинга в /opt/myapp
mkdir -p /opt/myapp
cp hello_world_app.py /opt/myapp/hello_world_app.py
cp monitoring_script.py /opt/myapp/monitoring_script.py

# Устанавливаем необходимые зависимости
cp monitor.service /etc/systemd/system/
# Перезагружаем демон systemd и запускаем сервис мониторинга
systemctl daemon-reload 
systemctl enable monitor.service
systemctl restart monitor.service

echo "Initialization complete."