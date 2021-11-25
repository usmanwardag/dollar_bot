import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] // 2, y[i], ha='center')


def visualize(total_text, monthly_budget):

    total_text_split = [line for line in total_text.split('\n') if line.strip() != '']
    monthly_budget_str= ""
    for key, value in monthly_budget.items():
        monthly_budget_str += str(key) + " $" + str(value) + "\n"
    monthly_budget_split = [line for line in monthly_budget_str.split('\n') if line.strip() != '']
    categ_val = {}
    for i in total_text_split:
        a = i.split(' ')
        a[1] = a[1].replace("$", "")
        categ_val[a[0]] = float(a[1])

    monthly_budget_categ_val = {}
    for j in monthly_budget_split:
        x = j.split(' ')
        x[1] = x[1].replace("$", "")
        monthly_budget_categ_val[x[0]] = float(x[1])

    x = list(categ_val.keys())
    y = list(categ_val.values())

    plt.bar(categ_val.keys(), categ_val.values(), color=[(1.00, 0, 0, 0.6), (0.2, 0.4, 0.6, 0.6), (0, 1.00, 0, 0.6), (1.00, 1.00, 0, 1.00)], edgecolor='blue')
    plt.bar(monthly_budget_categ_val.keys(), monthly_budget_categ_val.values())
    addlabels(x, y)

    plt.ylabel("Expenditure")
    plt.xlabel("Categories")
    plt.xticks(rotation=90)

    plt.savefig('expenditure.png', bbox_inches='tight')
