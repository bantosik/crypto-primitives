'''
Created on 28-01-2013

@author: bartek
'''
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def strxorhex(a, b):
	return strxor(a.decode("hex"), b.decode("hex")).encode("hex")


if __name__ == "__main__":
    print strxor("Pay Bob 100$","Pay Bob 500$").encode("hex")