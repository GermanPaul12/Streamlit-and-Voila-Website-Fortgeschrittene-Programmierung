import random
nums = [i for i in range(100)]
ops = ["+", '-', '*', '/']
with open(r"Streamlit/data/calc_csv.csv", 'a+') as f:
    for i in range(100):
        num1 = random.choice(nums)
        num2 = random.choice(nums)
        op = random.choice(ops)
        f.write(f"{num1},{num2},{op}\n")
       
    