import pulp

# Створення проблеми лінійного програмування
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості вироблених продуктів
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Об'єктивна функція: максимізація загальної кількості продуктів
model += lemonade + fruit_juice, "Total Products"

# Обмеження ресурсів
model += 2 * lemonade + fruit_juice <= 100  # Вода
model += 1 * lemonade <= 50  # Цукор
model += 1 * lemonade <= 30  # Лимонний сік
model += 2 * fruit_juice <= 40  # Фруктове пюре

# Розв'язання задачі
model.solve()

# Отримання результатів
lemonade_count = pulp.value(lemonade)
fruit_juice_count = pulp.value(fruit_juice)

print(f"Lemonade: {lemonade_count}, Fruit Juice: {fruit_juice_count}")
