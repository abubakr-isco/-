# Учебный блог Django

Реализация задания «Урок 50. Работа с шаблонами и формами»: общий шаблон с меню и подвалом, список и просмотр статей, создание и редактирование через `ModelForm`, проверка заголовка, форма обратной связи и сообщения об успехе. Bootstrap подключён через CDN.

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте http://127.0.0.1:8000/. Статью можно создать по адресу `/articles/new/`, отредактировать по `/articles/<id>/edit/`, сообщение отправить по `/feedback/`.

## Проверка

```bash
python manage.py test
```

Для просмотра записей в панели администратора создайте пользователя командой `python manage.py createsuperuser`, затем откройте `/admin/`.
