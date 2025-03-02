# ru-essay-checker

<img src="https://github.com/OtryvnoyKalendar/ru-essay-checker/blob/main/screenshots/screenshot%201.png" height="350" >

### Общее описание
ИИ-клиент, который проверяет сочинения `ЕГЭ`. Может быть использован для других целей. Для доступа вы должны получить свой api-ключ.

### Зависимости
В вашей системе должен быть установлен `python 3.9` и библиотека `tkinter`.  
Установка на `Debian-based` дистрибутивах:  
```sh
sudo apt-get install python3-tk python-pandas python3-openpyxl
```
Установка на `Arch-based` дистрибутивах:  
```sh
sudo pacman -S python-pandas python-openpyxl python-openai
yay -S python-mistralai # можно поставить и другим способом
```
Установка с помощью `pip`:
```sh
pip install mistralai openai
```
Пакеты нейросетей можно поставить во всю систему сразу:
```sh
# если не уверены, что делаете, не рискуйте
pip install --break-system-packages ai-package-name
```

### Как пользоваться 
Откройте терминал в `src` и выполните команду:  
```sh
python3 main.py
```

