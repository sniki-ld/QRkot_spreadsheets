# QRkot_spreadseets

Расширяет приложения QRKot
(благотворительный фонд поддержки котиков) возможностью формирования отчёта в гугл-таблице.
___

## О проекте
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание
нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, 
на корм оставшимся без попечения кошкам — на любые цели, 
связанные с поддержкой кошачьей популяции.
- Проекты

В Фонде QRKot может быть открыто несколько целевых проектов. 
У каждого проекта есть название, описание и сумма, которую планируется собрать. 
После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: 
все пожертвования идут в проект, открытый раньше других; 
когда этот проект набирает необходимую сумму и закрывается — 
пожертвования начинают поступать в следующий проект.
- Пожертвования

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. 
Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. 
Каждое полученное пожертвование автоматически добавляется в первый открытый проект, 
который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же 
в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. 
При создании нового проекта все неинвестированные пожертвования автоматически 
вкладываются в новый проект. 
- Отчет в гугл-таблице

Добавлена возможность отсортировать закрытые проекты, по скорости сбора средств — 
от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму и формирования отчёта в гугл-таблице.
___

## Технологии:
* [Python версии 3.9 и выше](https://www.python.org/downloads/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [FastAPI Users](https://fastapi-users.github.io/fastapi-users/10.1/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html)
* [Google Sheets](https://developers.google.com/sheets)
___

## Установка
Склонируйте проект:
   ```
   git clone https://github.com/sniki-ld/cat_charity_fund.git
   ```
Перейдите в папку с проектом:
   ```
   cd cat_charity_fund
   ```
Создайте и активируйте виртуальное окружение:
   ```
   python3 -m venv venv
   ```
   ```
   source venv/bin/activate
   ```
Обновите менеджер пакетов (pip):
   ```
   pip3 install --upgrade pip
   ```
Установите необходимые зависимости:
   ```
   pip3 install -r requirements.txt
   ```
Создайте файл с переменными окружения `.env`:
   ```
   touch .env
   ```
Опишите переменными окружения:
   ```
   APP_TITLE=<ваше название приложения>
   APP_DESCRIPTION=<ваше описание проекта>
   DATABASE_URL=<настройки подключения к БД, например: sqlite+aiosqlite:///./development.db>
   SECRET=<секретный ключ>
   FIRST_SUPERUSER_EMAIL=<email первого суперпользователя>
   FIRST_SUPERUSER_PASSWORD=<пароль первого суперпользователя>
   ```
___

## Использование
Примените миграции для создания БД:
  ```
  alembic upgrade head
  ```
  
Для запуска проекта выполните команду:
  ```
  uvicorn app.main:app --reload
  ```

_Если в файле `.env` были определены переменные
`FIRST_SUPERUSER_EMAIL` и `FIRST_SUPERUSER_PASSWORD`, 
то при первом запуске приложения в базе данных будет создан суперпользователь.
Эти данные можно использовать для авторизации._
___

## Документация API
Документация по проекту:
 - `/docs` — документация в формате Swagger;
 - `/redoc` — документация в формате ReDoc.
___

## Об авторе
Автор проекта: Елена Денисова
___
