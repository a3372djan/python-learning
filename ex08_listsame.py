# Adding list items too list
sum=0
my_subjects=["sst","math","eng","urdu","islamyat"]
my_marks=[10,12,14,19,23]
          
for i in range(0,4):
    print(f"{my_subjects[i]}  {my_marks[i]}")
    sum=sum+my_marks[i]
print(f"{sum}")
