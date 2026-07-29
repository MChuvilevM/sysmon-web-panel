# Sysmon Web Panel

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%252B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-REST-1e4138?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/PowerShell-5.1%2B-blueviolet?style=for-the-badge&logo=powershell&logoColor=white" alt="PowerShell">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <img src="docs/demo.gif" alt="Demo GIF" width="100%">
</p>

## Описание проекта
Инструмент для сбора и отправки системных метрик (CPU, память, диск) с хостов Windows в централизованное бэкенд-приложение на базе Django REST Framework.

## Технологии
* Python / Django REST Framework
* PowerShell / CIM / WMI

## Установка и запуск

1. Склонируйте репозиторий:
   ```bash
   git clone [https://github.com/MChuvilevM/sysmon-web-panel.git](https://github.com/MChuvilevM/sysmon-web-panel.git)
   ```

2. Запустите PowerShell-скрипт сбора метрик:
 ```
.\scripts\send-metrics.ps1
