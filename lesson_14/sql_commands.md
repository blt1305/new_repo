# Основные команды для работы с БД

#### Работа с БД

- Создать БД
``CREATE DATABASE test
``

- Вывести список доступных БД
``SHOW DATABASES;``

- Удалить БД
``DROP DATABASE test;``

#### Создать таблицу 

```
CREATE TABLE persons (
    person_id int  NOT NULL AUTO_INCREMENT,
    last_name varchar(255),
    first_name varchar(255) NOT NULL,
    address varchar(255),
    city varchar(255),
    PRIMARY KEY (person_id)
);
```

#### Добавить поле в таблицу

```ALTER TABLE persons ADD email varchar(128);```

#### Удалить поле из таблицы

```ALTER TABLE persons DROP COLUMN email;```


#### Другие команды для работы с таблицами

- Показать список таблиц
```
USE test;
SHOW tables;
```

- Удалить таблицу
```DROP TABLE persons;```

#### Типы данных (основные)

[какие типы данных есть в sql](https://www.w3schools.com/sql/sql_datatypes.asp)

```
- person_id int  NOT NULL
- last_name varchar(255)
- is_active bool default 0
- created_at datetime 
```

#### Вставка в таблицу

```commandline
INSERT INTO persons (first_name,last_name,created_at) VALUES ('Egor','Melnik', NOW());
INSERT INTO persons (first_name,last_name,created_at,address) VALUES ('Igor','Bubenchik', NOW(), 'Minsk');
INSERT INTO persons (first_name,last_name,created_at,address, age) VALUES ('Alex','Novak', NOW(), 'Paris', 31);
INSERT INTO persons (first_name,last_name,created_at,address, age) VALUES ('Kirill','Petrov', NOW(), 'Warsaw', 35);
```

### Получение данных из таблицы

- Получить все поля со всеми данными
```SELECT * FROM persons;```

- Получить некоторые поля
```SELECT last_name, first_name FROM persons;```

- Получить только первые 2 записи
```SELECT * FROM persons LIMIT 2;```

- Отсортировать по полю
```SELECT * FROM persons ORDER BY created_at``` - по возрастанию
```SELECT * FROM persons ORDER BY created_at DESC``` - по убыванию

таже тут может быть перечислено несколько полей через запятую

### Фильтрация данных
Общий синтаксис:

``WHERE (условие 1) AND/OR (условие 2) AND/OR (условие 3)``

Примеры:

```commandline
SELECT * FROM persons WHERE last_name='Bubenchik';
SELECT * FROM persons WHERE person_id=1;
SELECT * FROM persons WHERE last_name='Melnik' AND first_name='Egor';
SELECT * FROM persons WHERE last_name='Melnik' AND first_name='Egor' AND age > 35;
SELECT * FROM persons WHERE age > 35 OR age < 5;
SELECT * FROM persons WHERE age BETWEEN 10 AND 20;
SELECT * FROM persons WHERE age IN (4, 18);
SELECT * FROM persons WHERE age NOT IN (4, 18);
```

Вывести уникальные фамилии:
```SELECT DISTINCT last_name FROM persons;```

Частичное сранение строки:

[знакомство с оператором LIKE](https://www.w3schools.com/sql/sql_like.asp)
```SELECT * FROM persons WHERE last_name LIKE 'Petrov%'```

### GROUP BY - группировка по полю

- SUM - сумма чисел
- MIN/MAX - минимальное или максимальное значение
- COUNT - количество
- AVG - среднее значение

Количество представителей каждой фамилии:
```commandline
SELECT last_name, count(*)
FROM persons
GROUP BY last_name
```

Количество Петровых:
```
SELECT count(*)
FROM persons
WHERE last_name LIKE 'Petrov%'
 ```

Средний возраст:
```
SELECT avg(age) FROM persons
```

Минимальный возраст:
```
SELECT min(age) AS min_age FROM persons
 ```

### Удаление и апдейт записей

```DELETE FROM persons WHERE id=1;```

```
UPDATE persons
SET age=19, sex='male'
WHERE age=18;
```




