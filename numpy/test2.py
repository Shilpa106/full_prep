# import ast
# n=["['akash', 'abhishek', 'Shirt', '4', '12', 48]", "['akash', 'abhishek', 'Pant', '4', '10', 40]", "['akash', 'abhishek', 'Coat Pant', '1', '20', 20]"]
# print(n)
# for i in n:
#     # print('iii',i,type(i))
#     res=ast.literal_eval(i)
#     print(res,type(res))
   
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x+1, sequences) 
print(list(filtered_result))