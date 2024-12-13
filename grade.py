p = int(input("Enter project score:"))
i = int(input("Enter internal score:"))
e = int(input("Enter external score:"))
if p >= 50 and i >= 50 and e >= 50:
    total = (p*0.7)+(i*0.1)+(e*0.2)
    if total > 90:
        print("A grade")
    elif total > 80:
        print("B grade")
    else:
        print("C grade")
else:
    if p < 50:
        print("Failed in project and score is", p)
    if i < 50:
        print("Failed in internal and score is", i)
    if e < 50:
        print("Failed in external and score is", e)
