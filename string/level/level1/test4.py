

s='gfg'
# print(s)
# st=set()
# if s not in st:
#     st.add(s)
# print(st)

# li=list(s).copy()
# print(li)
# for i in range(len(s)):
#     t=list(s).copy()
    
for i in range(len(s)):
    # print(s)
    # print(list(s))
    t=list(s).copy()
    print("firstt",t)
    t.remove(s[i])
    print("secondt",t)
    # print("firstt",t)
    t=''.join(t)
    print(t)