
# Dear Sir i am using Python in this Quiz.

"""
Write a program for an Internet café billing N customers. Read minutes used for each. 
Charge 4 per minute. If minutes > 120 apply 8% discount for that customer. 
Print bill per customer and total. 
Use variables, IO, loops, if/else. Push to GitHub and paste repository URL.
"""


n = int(input("Enter Number of Customer: "))
totat_revenue = 0

for i in range(n):
    min_taken_Each_Customer = int(input(f"Enter time taken in minute of customer # {i + 1}: "))
    bill_per_customer = min_taken_Each_Customer * 4

    # Applying Discount
    if min_taken_Each_Customer > 120:
        bill_per_customer = (min_taken_Each_Customer * 4) * (1 - 0.08)
        print(f"Bill of Customer # {i + 1} is PKR {bill_per_customer:.2f}/- Also 8% is off for you. ")
    else:
        print(f"Bill of Customer # {i + 1} is PKR {bill_per_customer:.2f}/-")

    totat_revenue += bill_per_customer
    

print(f"Total Revenue from all customer is PKR {totat_revenue:.2f} ")
