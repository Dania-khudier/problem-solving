# Missing number :


numbers = [1, 2, 4, 5]
n = 5  
# // :قسمة بدون باقي
expected_sum = n * (n + 1) // 2 #المجموع الفعلي 
actual_sum = sum(numbers) # مجموع الارقام الموجودة

missing_number = expected_sum - actual_sum

print( missing_number)
    

    