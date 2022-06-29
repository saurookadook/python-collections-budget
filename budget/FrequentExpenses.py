import collections
import matplotlib.plt as plt

from pprint import pprint as pp
from . import Expense


expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
pp(spending_counter)

top5 = spending_counter.most_common(5)

categories, count = zip(*top5)

# fig = Figure (top-level container for graph)
# ax = Axes (contains actual figure elements)
fig, ax = plt.subplots()

ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()
