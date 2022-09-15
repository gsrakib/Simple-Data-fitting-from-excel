# Npre 451 data decay constant calcualtion data fitting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# put the excel file in the directory
excel = "Lab2.xlsx" 
# mention the sheet name to use
df = pd.read_excel(excel,sheet_name = "Exp3")
# input x columns as list
xdata1 = list(df['Time'])
# rewrite the list as an array which is less robust compare to list, if you print they look like same
xdata = np.asarray(xdata1)
# input x columns as list
ydata1 = list (df['Counts'])
ydata = np.asarray(ydata1)
# define exponential function
def expon(x,A,B):
    y = A*np.exp(-1*B*x)
    return y
# curvefit to optimize and fit 
from scipy.optimize import curve_fit
# make an intial guess to fit 
guess = [1000, 0.00001]
parameters, covariance = curve_fit(expon, xdata, ydata, p0 = guess)
fit_A = parameters[0]
fit_B = parameters[1]
print(fit_A)
print(fit_B)
fit_y = expon(xdata,fit_A, fit_B)
plt.plot(xdata, ydata, "o", label = "data")
plt.plot(xdata,fit_y, "-", label ="fit")
plt.xlabel('Time (s)')
plt.ylabel('Counts')
plt.title("In-116m decay data")
plt.show()