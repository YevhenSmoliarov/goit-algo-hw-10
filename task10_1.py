!pip install pulp

from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Створення моделі
model = LpProblem(name="optimize_production", sense=LpMaximize)

# Змінні для кількості вироблених продуктів
lemonade = LpVariable(name="lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

# Обмеження на ресурси
model += (2 * lemonade + 1 * fruit_juice <= 100, "water_constraint")
model += (1 * lemonade <= 50, "sugar_constraint")
model += (1 * lemonade <= 30, "lemon_juice_constraint")
model += (2 * fruit_juice <= 40, "fruit_puree_constraint")

# Цільова функція
model += lpSum([lemonade, fruit_juice]), "Objective"

# Розв'язання моделі
model.solve()

# Отримання результатів
lemonade_qty = value(lemonade)
fruit_juice_qty = value(fruit_juice)

print(f"Optimal quantity of Lemonade: {lemonade_qty}")
print(f"Optimal quantity of Fruit Juice: {fruit_juice_qty}")