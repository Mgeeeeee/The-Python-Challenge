'''
#我的代码
fake = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

real = ''

for i in fake:
    if i >= 'a' and i <= 'x':
        i = chr(int(ord(i)) + 2)
    elif i == 'y':
        i = 'a'
    elif i == 'z':
        i = 'b'

    real += i

print(real)
'''
#maketrans()和translate()函数
fake = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
key = 'map'

intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
trantab = fake.maketrans(intab,outtab)

print(fake.translate(trantab))
print(key.translate(trantab))