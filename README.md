# ru-essay-checker

<img src="https://github.com/OtryvnoyKalendar/ru-essay-checker/blob/main/screenshots/screenshot%201.png" height="350" >

### Общее описание
ИИ-клиент, который проверяет сочинения `ЕГЭ`. Может быть использован для других целей. Для доступа вы должны получить свой api-ключ.

### Установка
1. Установите и проверьте наличие `git`
```sh
git --version
```
2. Установите и проверьте наличие `uv`
```sh
uv --version
```
- Установка на `Unix`:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
- Установка на `Windows`:  
Используйте `irm` для загрузки скрипта и выполнения его с помощью `iex`:
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Изменение политики выполнения позволяет запускать скрипт из Интернета.
Запросите конкретную версию, указав ее в URL-адресе:
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.6.12/install.ps1 | iex"
```
3. Установите библиотеку tk, если требуется  
На некоторых linux дистрибутивах она не входит в пакет вместе с python  
- На `Arch-based`:
```sh
sudo pacman -S tk
```
- На `Debian-based`:
```sh
sudo apt install libtk-dev
```
4. Откройте консоль в папке с проектом
5. Установка программы
```sh
uv sync
```
6. Запуск программы
```sh
uv run rchecker
```
