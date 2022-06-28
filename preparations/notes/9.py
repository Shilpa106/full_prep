# remove duplicates
a=''
tests='AZZBCDABBCDABBCCCCDDEEEF'
# OP:AZBCDEF

for i in tests:
    # a.append(i)
    if i not in a:
        a+=i
print(a)
