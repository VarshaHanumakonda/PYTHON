'''import csv
customer=[]
with open('customers.csv','r') as f:
    read=csv.DictReader(f)
    for i in read:
        print(i)
        customer.append(i)
        print(customer)
for i in customer:
    print(i['Name'])    '''


         