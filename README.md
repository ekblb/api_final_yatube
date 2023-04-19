### Описание
Данный проект содержит REST API для Yatube.
Через этот интерфейс смогут работать мобильное приложение или чат-бот;
через него же можно будет передавать данные в любое приложение или на фронтенд.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```git clone https://github.com/ekblb/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
Документация в формате Redoc доступна по адресу:
[Redoc API Yatube](http://127.0.0.1:8000/redoc)

Автор проекта: Балабаева Екатерина
