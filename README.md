# ru-essay-checker

<img src="https://github.com/OtryvnoyKalendar/ru-essay-checker/blob/main/screenshots/screenshot%201.png" height="350" >

### Общее описание
ИИ-клиент, который проверяет сочинения `ЕГЭ`. Может быть использован для других целей. Для доступа вы должны получить свой api-ключ. В вашей системе должен быть установлен `python` не ниже `3.11`.

### Установка с помощью виртуальной среды
Откройте консоль в папке с проектом  
Действия на `Unix`:  
```sh
python -m venv checkerenv
source checkerenv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
python ./src/main.py
```
Действия на `Windows`:  
```sh
python -m venv checkerenv
checkerenv\Scripts\activate
pip install -r requirements.txt
pip install --upgrade pip
python src\main.py
```
Если какого-то модуля не хватает, то добавьте его имя в `requirements.txt` и заново используйте команду `pip install -r ...`  
Для повторного запуска:  
`Unix`:  
```sh
source checkerenv/bin/activate
python ./src/main.py
```
`Windows`:  
```sh
checkerenv\Scripts\activate
python src\main.py
```
Чтобы выйти из виртуальной среды:  
```sh
deactivate
```

### Установка зависимостей в систему на Linux 
Эти пакеты нейросетей можно поставить во всю систему сразу:
```sh
# Не рискуйте, если не уверены в том, что делаете
pip install --break-system-packages mistralai gigachat
```
Установка на `Debian-based` дистрибутивах:  
```sh
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
sudo apt update
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.13.2/Python-3.13.2.tgz
sudo tar xzf Python-3...
cd Python-3...
sudo ./configure
sudo make altinstall
python3.13 -V # проверка установился ли python
```
Системные пакеты: (у меня не работали)
```sh
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.13
sudo apt-get install python python3 python-is-python3 python3-pip
sudo apt-get install python3.13-venv python3.13-tk
sudo apt-get install python3-openpyxl python3-mistralclient python3-openai python3-markdown
# gigachat tkhtmlview - хз как установить в систему
```
   
Установка на `Arch-based` дистрибутивах:  
```sh
sudo pacman -S python-openpyxl python-openai python-markdown
# gigachat tkhtmlview - хз как установить в систему
# Этот пакет из неофициальных репозиториев
yay -S python-mistralai
```

