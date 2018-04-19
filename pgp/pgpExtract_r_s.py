from pgpdump import AsciiData


file = open('AliceMsgtxt.asc','rb')
asc_data = file.read()
data = AsciiData(asc_data)
packets = list(data.packets())

datastr = str(packets[0].sig_data)

databytes = packets[0].data

x = ''

# for byte_s in databytes:
#     print(''.join('{:02x}'.format(byte_s)))
#     x += ''.join('{:02x}'.format(byte_s))
#
# print(len(databytes))
r = '0x'
s = '0x'

for i in range(len(databytes)):
    # print(i)
    # print(''.join('{:02x}'.format(databytes[i])))
    x += ''.join('{:02x}'.format(databytes[i]))
    if i > 39 and i <= 59:
        r += ''.join('{:02x}'.format(databytes[i]))
    if i > 61:
        s += ''.join('{:02x}'.format(databytes[i]))

print('x:' + x)
print('r:' + r)
print('s:' + s)
solve_r = int(r, 16) % 0xb0b
solve_s = int(s, 16) % 0xb0b

print('Loesung fuer r:' + hex(solve_r))
print('Loesung fuer s:' + hex(solve_s))
