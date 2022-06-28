tests='B4A1D3'

# OP:ABD134
alphabets=[]
num=[]
for ch in tests:
    # print(sorted(i))
    if ch.isalpha:
        alphabets.append(ch)
    else:
        num.append(ch)

print(''.join(sorted(alphabets)+sorted(num)))

