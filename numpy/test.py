n=["['akash', 'abhishek', 'Shirt', '4', '12', 48]", "['akash', 'abhishek', 'Pant', '4', '10', 40]", "['akash', 'abhishek', 'Coat Pant', '1', '20', 20]"]
print(n)
for i in n:
    print('iii',i)
    res=i.strip('][').split(',')
    print(type(res),res,"]]]]]]]]]]")
    for y in res:
        print(y)

