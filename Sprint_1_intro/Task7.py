def Cipher_Zeroes(N):
    ZEROS = {'0': 1, '6': 1, '9': 1, '8': 2}
    gift = 0
    for n in str(N):
        gift += ZEROS.get(n, 0)

    if gift % 2 == 0 and gift > 0:
        gift -= 1

    elif gift % 2 == 1:
        gift += 1

    return bin(gift)[2:]
