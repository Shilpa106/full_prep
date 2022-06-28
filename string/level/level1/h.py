# hex_string = "11"[2:]
# # Slice string to remove leading `0x`


# bytes_object = bytes.fromhex(hex_string)
# # Convert to bytes object


# ascii_string = bytes_object.decode("ASCII")
# # Convert to ASCII representation

# print(ascii_string)
# print(hex(11)[2:])

a = ["geeksforgeeks", "geeks",
					"geek", "geezer"]
# print(a)
# a.sort()
# print(a)
size=len(a)
print(size)
# end = min(len(a[0]), len(a[size - 1]))
a.sort()
print(a)
print(len(a[0]))
print(len(a[size - 1]))
end=min(len(a[0]), len(a[size - 1]))
print(end)