import numpy as np
from scipy.optimize import curve_fit

x1 = np.array([1, 2, 3, 4, 5, 6, 7])
x2 = np.array([1689926, 625904, 232488, 102177, 59636, 27945, 1844])
y = np.array([142185, 44415, 9614, 8626, 7476, 3366, 279])

def custom_func(X, a, b, c, d):
    x1, x2 = X
    return a * x1**4 + b * np.log(x2) + c * x1 + d

popt, pcov = curve_fit(custom_func, (x1, x2), y)

print("Optimized parameters:", popt)
y_pred = custom_func((x1, x2), *popt)

print("\nActual vs Predicted with Error Percentage:")
print("{:<10} {:<10} {:<15} {:<15} {:<15}".format("Index", "x1", "x2", "Y_actual", "Y_predicted"))

for i, (actual, pred) in enumerate(zip(y, y_pred)):
    print("{:<10} {:<10} {:<15} {:<15.2f} {:<15.2f}".format(
        i + 1, x1[i], x2[i], actual, pred))
