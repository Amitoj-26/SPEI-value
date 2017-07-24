import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from datetime import datetime
from statistics import mean
from statistics import stdev
np.seterr(divide='ignore', invalid='ignore')
read_file = pd.read_csv('/home/amitoj/Documents/drought.csv',  usecols = ['Date','DayPrecip','DayAsceEto'])
# print(read_file)
read_file['Date'] = pd.to_datetime(read_file['Date'])
# print(read_file['Date'])
# print(read_file['Date'].dtypes)
read_file['year'], read_file['month'] = read_file['Date'].apply(lambda x: x.year), read_file['Date'].apply(lambda x: x.month)
# print(read_file)
read_file = read_file.drop('Date', 1)
# print(read_file)
a=pd.pivot_table(read_file,index=["year","month"],values=["DayPrecip","DayAsceEto"],aggfunc=np.mean)
# print(a)
new_a= a[['DayPrecip']].sub(a['DayAsceEto'], axis=0)
new_a = new_a.rename(columns={'DayPrecip':'Difference month wise'})
# new_a= new_a.abs()
# print(new_a)
new_a1 = new_a.replace({"Difference month wise":{0.000000:0.000001}})
new_a1 = new_a.replace({"Difference month wise":{0.: 0.000001}})
# print(new_a1)
new_a2 = new_a1.values
# x1 =new_a1.drop('year',1)
# print(new_a2)
x = new_a2
# # print(x)
# # # print (len(x))
# # caculation of the alpha beta and gamma parameter
N = len(x)
# # sum = 0
# # for i in range(0,len(x)):
# #     F = (i-0.35)/(N)
# #     w1 = (1-F)*(x[i])
# #     # print(w1)
# #     sum = w1+sum
# # # print(sum)
# # W1 =(sum/N)import
# # print(W1)
# #
# # sum2 = 0
# # for j in range(0,len(x)):
# #     F = (j-0.35)/(N)
# #     w2 = ((1-F)**2) *(x[j])
# #     # print(w1)
# #     sum2 = w2+sum2
# # # print(sum2)
# # W2 =(sum2/N)
# # print(W2)
# #
# # sum3 = 0
# # for k in range(0,len(x)):
# #     w0 =x[k]*1
# #     # print(w1)
# #     sum3 = w0+sum3
# # # print(sum3)
# # W0 = (sum3/N)
# # print(W0)
# #
sum=0
for i in range(0,len(x)):
     w1 =((N-i)*x[i])
     W_1 = (w1)/((N-1)/(1))
     # print(w_1)
     sum = W_1+sum
     # print(sum)
W1 =(sum/N)
print(W1)
# calculation of w2
sum2= 0
for j in range(0,len(x)):
     w2 =((N-j/(2))*x[j])
     W_2 = (w2)/((N-1)/(2))
     # print(w_2)
     sum2 = W_2+sum2
     # print(sum2)
W2= (sum2/N)
print(W2)
W0 =0
# # calculation of alpha,beta and gamma
# Beta = (2*W1-W0)/(6*W1-W0-6*W2)
# # np.round(Beta,2)
# print(Beta)
# # print(Beta)
# = 6.283185
# alpha_numerator = (W0-2*W1)*Beta
# alpha_denominator =  *(1+(1/Beta))*(1-(1/Beta))
# Alpha = (alpha_numerator/alpha_denominator)
# print(Alpha)
# Gamma = (W0-Alpha *)*(1+(1/Beta))*(1-(1/Beta))
# print(Gamma)
# for i in range(0,len(x)):
#     pdf= (Alpha)/(x[i]-Gamma)**Beta
#     print(pdf)
# value=[]
# for i in range(0,len(x)):
#     values = (Alpha/(x[i]-Gamma))
#     value.append(values)
#     for i in range(0,len(x)):
#         exponnet = value[i]**Beta
#         print(exponnet)
    # print(np.round(values,2))
    # print(values)
    # value= math.pow(values,Beta)
    # print(value)
#  Expression =[]
# # # calculation of probability density function of log logistic distribution
# for i in range(0,len(x)):
#     expression=((Alpha/(x[i]-Gamma))** Beta)
#     Expression.append(expression)
# print(Expression)
# # calculation of w1 & w2 for alpha and beta and gamma functio

# calculation of parameter beta
beta = (2 * W1)/((6*W1)-(6*W2))
beta =-0.7612514+0j
# # calculation of parameter alpha
alpha_denominator = (1+(1/beta))*(1-(1/beta))
# print(beta_2)
τ = 6.283185
alpha_denominator1 = τ * alpha_denominator
alpha_numerator  = (-2*W1)* (beta)
alpha = (alpha_numerator)/(alpha_denominator)
print(alpha.real)
gamma = (-alpha) * (alpha_denominator)
print(gamma.real)
# # calculation of probability density function
Pdf = [ ]
for i in range(0,len(x)):
    denom =((alpha)/(x[i]-gamma))
    denom2 =denom**beta
    # print(denom2.real)
    f_pdf = (1/(1+denom2))
    # print(f_pdf.real)
    Pdf.append(f_pdf.real)
# print(Pdf)
# numerator_pdf = alpha
# partial_expression_of_pdf = alpha/denominator
# print(partial_expression_of_pdf)
# expression1 = partial_expression_of_pdf ** beta
# print(expression1)
# f_pdf = (1/(1+ expression1))
# print
Probability_value=[]
for i in range(len(Pdf)):
    Pdf[i] -= 1
    # print(Pdf[i])
    Probability_value.append(Pdf[i])
# print (Probability_value)
Probability_values= [abs(k) for k in Probability_value]
# print(Probability_values)
w_1=[ ]
w_2=[ ]
for x in Probability_values:
    if x < 0.5:
        W = (-2 * (math.log(x)))
        # print(W)
        w_1.append(W)
    # print(w_1)
else:
    w = (2 *(math.log(x)))
        # print(w)
    w_2.append(w)
print(len(w_1))
print(len(w_2))
C0=2.515517
C1=0.802853
C2=0.010328
d1=1.432788
d2=0.189269
d3=0.001308
SPEI =[]
Spei =[]
# for w1 in w_1:
#     spei =(w1-(C0)+(C1*w1)+(C2*w1*w1)/(1+(d1*w1)+(d2*w1*w1)+(d3*w1*w1*w1)))
#     SPEI.append(spei)
# # print(SPEI)
# for w2 in w_2:
#     spei1 = (w2-(C0 +(C1*w2)+(C2 *w2*w2)/(1+(d1*w2)+(d2*w2*w2)+(d3*w2*w2*w2))))
#     Spei.append(spei1)
# # print(Spei)
# SPEI_value =SPEI + Spei
# print("SPEI Values for each month from year 1997-2007=" + str (SPEI_value))
# SPEI_Value = [round(x,3) for x in SPEI_value]
# print(SPEI_Value)
