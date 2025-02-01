bsal = int(input("Enter basic salary in Rs. "))
if bsal < 10000:
    hra = 0.67 * bsal
    da = 0.73 * bsal
elif bsal < 20000:
    hra = 0.69 * bsal
    da = 0.76 * bsal
else:
    hra = 0.73 * bsal
    da = 0.89 * bsal
gs = hra + da + bsal
print("Gross salary is", gs, "/")
