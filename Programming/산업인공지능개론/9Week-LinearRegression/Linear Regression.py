import numpy as np
import pandas as pd
import openpyxl
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

#run_data = pd.read_csv('LowData.xlsx', delimiter=',', dtype=str, header=0)
run_data = pd.read_excel('LowData.xlsx', header=0, skipfooter=2, usecols='A:G' )

run_data.head(20)

x_data = run_data.iloc[:, 4]
y_data = run_data.iloc[:, -1]

x_time = np.array([float(x) for x in x_data])
y_yield = np.array([int(y) for y in y_data])

plt.scatter(x_time, y_yield)    # 데이터 위치의 산포도 출력
plt.title("Linear Regression")
plt.xlabel("Run Time")
plt.ylabel("Yield")
plt.axis([0, 1000, 0, 1000])

x = x_time.reshape(-1, 1)     # 입력
y = y_yield.reshape(-1, 1)     # 출력

model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)
plt.plot(x, y_pred, color='r')
plt.show()

