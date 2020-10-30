from os import strerror as strerr
from pprint import pprint
srcname = input("Source file name?: ")
try:
    f_table = {}
    src = open(srcname, 'rb')
    s = src.read()
    f_table = {chr(char) : s.count(char) for char in set(s)}
    src.close()
    sort_f_table = sorted(f_table.items(), key=lambda x: x[1], reverse=True)
    pprint(sort_f_table)

except IOError as e:
    print("Cannot open source file: ", strerr(e.errno))
    exit(e.errno)
dstname = input("Destination file name?: ")
# try:
#     dst = open(dstname, 'wb')
# except Exception as e:
#     print("Cannot create destination file: ", strerr(e.errno))
#     src.close()


#     exit(e.errno)
#
# buffer = bytearray(1)
# total = 0
# try:
#     readin = src.readinto(buffer)
#     while readin > 0:
#         written = dst.write(buffer[:readin])
#         total += written
#         readin = src.readinto(buffer)
# except IOError as e:
#     print("Cannot create destination file: ", strerr(e.errno))
#     exit(e.errno)

# print(total, 'byte(s) succesfully written')
# src.close()
# dst.close()