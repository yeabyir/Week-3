total_sum = 0
count_three = 0
count_five = 0
for num in range(1, 51):
    if num % 2 == 0:
        if num % 3 == 0:
            print("Three")
            count_three += 1
        elif num % 5 == 0:
            print("Five")
            count_five += 1
        else:
            total_sum += num
            print(num)
    else:
        print(num)
print("\nTotal Sum:", total_sum)
print("Count of 'Three':", count_three)
print("Count of 'Five':", count_five)
