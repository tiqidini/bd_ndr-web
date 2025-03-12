import sqlite3
import json

# Подключаемся к базе данных
connection = sqlite3.connect('ndrs.db')
cursor = connection.cursor()

# Выполняем запрос — замените "table_name" на название вашей таблицы
cursor.execute("SELECT * FROM ndrs")
rows = cursor.fetchall()

# Получаем названия столбцов
column_names = [description[0] for description in cursor.description]

# Формируем список словарей: каждая запись представлена как dict
data = [dict(zip(column_names, row)) for row in rows]

# Сохраняем в JSON файл
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

connection.close() 