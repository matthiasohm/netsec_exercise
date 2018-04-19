# from ascii to value
import math

from bitstring import BitArray

from pgp.extendedEuclideanAlgorithm import calcAlgorithm

data = "NetSeC"
e = 7
# Modulus
n = 585209
s_strich = 357672

# test calc Extended Euclidean algorithm
print('test calc Extended Euclidean algorithm >>')
calcAlgorithm(17, 2)
print('<< test calc Extended Euclidean algorithm')


# 7 bit ascii to int value
def intvaluefromstring(iptdata):
    value = '0'
    value2 = 0
    x = 0
    for s in iptdata:
        value += "{0:b}".format(ord(s))
        value2 = value2 * x * 2 ** 7 + ord(s)
        x += 1
    print('val  string:' + value)
    value3 = BitArray(bin=value)
    print('val3 string:' + str(value3.uint))
    # print(str(int(value, "2")))
    print('val2 string:' + str(value2))
    print('val2 bin   :' + bin(value2))
    return value3.uint


m = intvaluefromstring(data)

print("m mod n: " + str(m % n))

s_strich_hoch_e = s_strich**e % n
print("s'^e mod n: " + str(s_strich_hoch_e))



print("gcd(" + str((m - (s_strich_hoch_e))) +", "+ str(585209) + ")")
p = math.gcd((m - (s_strich**e)), n)
print("p: " + str(p))


result0 = calcAlgorithm(m - s_strich**e, n)



q = n/p
print("q: " + str(q))


# calc phi(n)
phi_n = (p-1) * (q-1)
print("phi_n: " + str(phi_n))


result = calcAlgorithm(phi_n, e)

d = result['inverse']
d_p = d % (p-1)
d_q = d % (q-1)

print("d: " + str(d))
print("d_p: " + str(d_p))
print("d_q: " + str(d_q))

result2 = calcAlgorithm(p, q)


print("a: " + str(result2['a_end']))
print("b: " + str(result2['b_end']))

print("valid signature sig: " + str(int(m)**int(d) % int(n)))

print("finished")
