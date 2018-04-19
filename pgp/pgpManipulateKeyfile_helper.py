
def calculateCheckSum(valueOf_x, prefixOf_x):
    summ = 0
    count = 0

    # Testcalculation of Checksum
    while count < len(valueOf_x):
        val = valueOf_x[count] + valueOf_x[count + 1]
        count += 2
        summ = summ + int(val, 16)

    summ = summ + int(prefixOf_x[0] + prefixOf_x[1], 16)
    summ = summ + int(prefixOf_x[2] + prefixOf_x[3], 16)
    return summ


# Analyzes the DSA key paket and prints all relevant data
# If Checksum doesn't fit the conditions there will be a new one calculated and returned
def printDSAKeyPaket(keydatabytes):
    print(
        '------------------------------------------------------------------------------------------------------------')
    print(
        '------------------------------------------------------------------------------------------------------------')
    print(
        '------------------------------------------------------------------------------------------------------------')

    privatekeypaket = ''
    versionnumber = ''
    creationtime = ''
    algorithm_dsa = ''
    length_p = ''
    prime_p = ''
    length_q = ''
    prime_q = ''
    length_g = ''
    number_g = ''
    length_y = ''
    pubkey_y = ''
    stringToKeyUsage = ''
    prefixOf_x = ''
    valueOf_x = ''
    checksum = ''

    for k in range(len(keydatabytes)):
        privatekeypaket += ''.join('{:02x}'.format(keydatabytes[k]))
        if k == 0:
            versionnumber += ''.join('{:02x}'.format(keydatabytes[k]))
        if 1 <= k <= 4:
            creationtime += ''.join('{:02x}'.format(keydatabytes[k]))
        if 5 <= k <= 5:
            algorithm_dsa += ''.join('{:02x}'.format(keydatabytes[k]))
        if 6 <= k <= 7:
            length_p += ''.join('{:02x}'.format(keydatabytes[k]))
        if 8 <= k <= 7+128:
            prime_p += ''.join('{:02x}'.format(keydatabytes[k]))
        if 136 <= k <= 137:
            length_q += ''.join('{:02x}'.format(keydatabytes[k]))
        if 138 <= k <= 137+20:
            prime_q += ''.join('{:02x}'.format(keydatabytes[k]))
        if 158 <= k <= 159:
            length_g += ''.join('{:02x}'.format(keydatabytes[k]))
        if 160 <= k <= 159+128:
            number_g += ''.join('{:02x}'.format(keydatabytes[k]))
        if 288 <= k <= 289:
            length_y += ''.join('{:02x}'.format(keydatabytes[k]))
        if 290 <= k <= 289+128:
            pubkey_y += ''.join('{:02x}'.format(keydatabytes[k]))
        if 418 <= k <= 418:
            stringToKeyUsage += ''.join('{:02x}'.format(keydatabytes[k]))
        #     ------Private Key
        if 419 <= k <= 420:
            prefixOf_x += ''.join('{:02x}'.format(keydatabytes[k]))
        if 421 <= k <= 440:
            valueOf_x += ''.join('{:02x}'.format(keydatabytes[k]))
        if 441 <= k <= 442:
            checksum += ''.join('{:02x}'.format(keydatabytes[k]))

    print('keydatabytes: ' + privatekeypaket)

    print('versionnumber:' + versionnumber)
    print('creationtime:' + creationtime)
    print('algorithm_dsa:' + algorithm_dsa)
    print('length_p :' + length_p)
    print('prime_p :' + prime_p)
    print('length_q :' + length_q)
    print('prime_q :' + prime_q)
    print('length_g :' + length_g)
    print('number_g :' + number_g)
    print('length_y :' + length_y)
    print('pubkey_y :' + pubkey_y)
    print('stringToKeyUsage :' + stringToKeyUsage)
    print('prefixOf_x :' + prefixOf_x)
    print('valueOf_x :' + valueOf_x)
    print('checksum :' + checksum)

    calculatedCheckSum = calculateCheckSum(valueOf_x, prefixOf_x)
    oldCheckSum = hex(int(checksum, 16))
    if oldCheckSum != hex(calculatedCheckSum):
        print('another checksum calculated: ' + hex(calculatedCheckSum))
        return calculatedCheckSum