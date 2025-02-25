import numpy as np
from sympy import symbols, Eq, solve
from scipy.optimize import fsolve
def prob1():
    m_min = [26,26,32,42,51,61,67,66,60,49,39,31]
    m_max = [40,41,48,60,69,77,83,82,75,64,54,45]
    m_avg = [33,34,40,51,60,69,75,74,67,56,47,38]
    m_avg_days = [16+31*t for t in range(12)]
    print(m_avg_days)
    res = 0
    x = symbols('x')
    b = np.array([val for val in m_avg])
    A = np.array([[1, t, t**2, t**3] for t in m_avg_days]) #quad fit
    A_t = A.transpose() #get A transposed
    left_side = np.matmul(A_t,A) #mimics A^T * A
    right_side = np.matmul(A_t,b) #mimics A^T * b
    print("A^T * A: \n", left_side)
    print("A^T * B: \n", right_side)
    c_values = np.linalg.solve(left_side,right_side) #solves Ax=b
    print(f"c0: {c_values[0]}, c1: {c_values[1]}, c2: {c_values[2]}, c3: {c_values[3]}")
    for i in range(len(c_values)): #plug in our t for our quadratic formula
        res += c_values[i] * x ** i
    print("Formula: ", res)
    return res

#each month 31 days
#avg for a month is 16th day
def calculate(poly):
    days = [4+31*5, 25+31*11] #june 4th and dec 25th
    x = symbols('x')
    res = [poly.subs(x, day) for day in days]
    print(f"Prediction for June 4th: {res[0]:.2f} F, \nPrediction for Dec 25th: {res[1]:.2f} F")

def find_days_at_temperature(poly, target_temp):
    x = symbols('x')
    # Define a function that will be zero when P3(t) = target_temp
    poly = poly - 64.89
    print(poly)
    

if __name__ == '__main__':
    polynomial = prob1()
    calculate(polynomial)
    target_temp = 64.89
    find_days_at_temperature(polynomial, target_temp)