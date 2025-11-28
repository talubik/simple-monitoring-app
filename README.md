# Application + Monitor Service

## Описание

Репозиторий содержит:
- `hello_world_app.py` — простое Flask-приложение.
- `monitoring_script.py` — скрипт мониторинга и автоматического перезапуска приложения.
- `monitor.service` — systemd-unit для автозапуска мониторинга.
- `update.sh` — скрипт установки и обновления.

---

## Установка

```bash
chmod +x update.sh
sudo ./update.sh
