n=10
a=[]
for i in range(0,n):
    elem=int(input("Enter height of student: "))
    a.append(elem)
avg=sum(a)/n
print("Average height of students is:",round(avg,2))