num=9669
# To maximize the number, change the first 6 from the left into 9.
# Why? Because the leftmost digit has the highest place value.
digits=list(str(num))

for i in range(len(digits)):
  if digits[i]=="6":
    digits[i]="9"
    break

print(int(''.join(digits)))



# or else in  one-line

print(int(str(num).replace("6","9",1)))

    
  
    
  