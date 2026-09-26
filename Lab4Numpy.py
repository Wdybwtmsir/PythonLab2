#Вариант 8
#Задание 2.1

import numpy as np
x = np.arange(0, 1.01, 0.01)
y = np.sqrt(x) * (np.cos(x) ** 2)
positive_mask = y > 0
x_positive = x[positive_mask]
y_positive = y[positive_mask]
print(" x    | F(x)")
print("----------------")
for xi, yi in zip(x_positive, y_positive):
    print(f"{xi:.2f} | {yi:.2f}")

#Задание 3.1
x_base = np.arange(0, 1.01, 0.01)
y_base = np.sqrt(x_base) * (np.cos(x_base) ** 2)
positive_results = y_base[y_base > 0]  # Здесь ровно 100 элементов (для x от 0.01 до 1.0)
arr1 = np.array(positive_results, dtype=int)
size = arr1.size  

arr2 = np.linspace(0.0, 10.0, num=size, dtype=float)

p_param = 0.35
arr3 = np.random.geometric(p=p_param, size=size).astype(float)

res_sum_mult = (arr1 + arr2 + arr3) * 5.0

res_sub = arr1.astype(float) - arr2

res_mult = arr1.astype(float) * arr3

arr2_safe = np.where(arr2 == 0, 1e-9, arr2)
res_div = arr1.astype(float) / arr2_safe

res_pow = arr1.astype(float) ** 3

print("Первые 5 элементов каждого массива и операций:")
print(f"Массив №1 (int):      {arr1[:5]}")
print(f"Массив №2 (float):    {arr2[:5]}")
print(f"Массив №3 (geometric): {arr3[:5]}")
print(f"Операция 1 (слож.*5):  {res_sum_mult[:5]}")
print(f"Операция 2 (вычит.):   {res_sub[:5]}")

#Задание 3.2
import io
import numpy as np

mock_csv_data = """26.09.2026,4510.0,4490.0,4530.0,4480.0
25.09.2026,4495.0,4520.0,4540.0,4490.0
24.09.2026,4530.0,4500.0,4550.0,4500.0
23.09.2026,4505.0,4480.0,4520.0,4470.0
22.09.2026,4480.0,4510.0,4515.0,4460.0
21.09.2026,4515.0,4500.0,4535.0,4495.0"""

file_object = io.StringIO(mock_csv_data.strip())

data_str = np.loadtxt(file_object, dtype=str, delimiter=",")

prices_matrix = data_str[:, [2, 4, 3, 1]].astype(float)

daily_mean = np.mean(prices_matrix, axis=1).reshape(-1, 1)

final_matrix = np.hstack((prices_matrix, daily_mean))

min_val = np.min(prices_matrix, axis=0)
max_val = np.max(prices_matrix, axis=0)
math_expectation = np.mean(prices_matrix, axis=0)
variance = np.var(prices_matrix, axis=0)
std_deviation = np.std(prices_matrix, axis=0)
root_mean_square = np.sqrt(variance)
coef_variation = root_mean_square / math_expectation


columns_names = ["Открытие", "Минимум ", "Максимум", "Закрытие"]
print("Экономико-статистические показатели акций 'Магнит':\n")
for i, name in enumerate(columns_names):
    print(f"--- {name} ---")
    print(f"Минимум:            {min_val[i]:.2f}")
    print(f"Максимум:           {max_val[i]:.2f}")
    print(f"Мат. ожидание:      {math_expectation[i]:.2f}")
    print(f"Дисперсия:          {variance[i]:.2f}")
    print(f"Станд. отклонение:  {std_deviation[i]:.2f}")
    print(f"СКО (из дисп.):     {root_mean_square[i]:.2f}")
    print(f"Коэф. вариации:     {coef_variation[i]:.4f}\n")

np.save("magnit_stats.npy", final_matrix)
print("Результирующий массив успешно сохранен в файл 'magnit_stats.npy'")
