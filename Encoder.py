from __future__ import print_function
import sys


def keyGen(left, right):

    leftKey = format(int("0x" + left, 16), '016b')
    rightKey = format(int("0x" + right, 16), '016b')

    leftKey1 = leftKey[1:] + leftKey[0]
    leftKey2 = leftKey1[1:] + leftKey1[0]
    leftKey3 = leftKey2[1:] + leftKey2[0]
    leftKey4 = leftKey3[1:] + leftKey3[0]
    leftKey5 = leftKey4[1:] + leftKey4[0]
    leftKey6 = leftKey5[1:] + leftKey5[0]
    leftKey7 = leftKey6[1:] + leftKey6[0]
    leftKey8 = leftKey7[1:] + leftKey7[0]
    leftKey9 = leftKey8[1:] + leftKey8[0]
    leftKey10 = leftKey9[1:] + leftKey9[0]

    rightKey1 = rightKey[1:] + rightKey[0]
    rightKey2 = rightKey1[1:] + rightKey1[0]
    rightKey3 = rightKey2[1:] + rightKey2[0]
    rightKey4 = rightKey3[1:] + rightKey3[0]
    rightKey5 = rightKey4[1:] + rightKey4[0]
    rightKey6 = rightKey5[1:] + rightKey5[0]
    rightKey7 = rightKey6[1:] + rightKey6[0]
    rightKey8 = rightKey7[1:] + rightKey7[0]
    rightKey9 = rightKey8[1:] + rightKey8[0]
    rightKey10 = rightKey9[1:] + rightKey9[0]

    subKey1 = leftKey1 + rightKey1          # 0010 0000 0000 0001  0000 0001 0000 0010
    subKey2 = leftKey2 + rightKey2          # 0100 0000 0000 0010  0000 0010 0000 0100
    subKey3 = leftKey3 + rightKey3          # 1000 0000 0000 0100  0000 0100 0000 1000
    subKey4 = leftKey4 + rightKey4          # 0000 0000 0000 1001  0000 1000 0001 0000
    subKey5 = leftKey5 + rightKey5          # 0000 0000 0001 0010  0001 0000 0010 0000
    subKey6 = leftKey6 + rightKey6          # 0000 0000 0010 0100  0010 0000 0100 0000
    subKey7 = leftKey7 + rightKey7          # 0000 0000 0100 1000  0100 0000 1000 0000
    subKey8 = leftKey8 + rightKey8          # 0000 0000 1001 0000  1000 0001 0000 0000
    subKey9 = leftKey9 + rightKey9          # 0000 0001 0010 0000  0000 0010 0000 0001
    subKey10 = leftKey10 + rightKey10       # 0000 0010 0100 0000  0000 0100 0000 0010

    return [subKey1, subKey2, subKey3, subKey4, subKey5, subKey6, subKey7, subKey8, subKey9, subKey10]


def feistel(rightText, subKey):
    intermediate1 = xor32(rightText, subKey)         # 0010 0000 0000 0001  0000 0001 0000 0010
    s1_1 = intermediate1[0:4]
    s2_1 = intermediate1[4:8]
    s1_2 = intermediate1[8:12]
    s2_2 = intermediate1[12:16]
    s1_3 = intermediate1[16:20]
    s2_3 = intermediate1[20:24]
    s1_4 = intermediate1[24:28]
    s2_4 = intermediate1[28:32]

    # s-box
    s1_1 = sbox1(s1_1)
    s1_2 = sbox1(s1_2)
    s1_3 = sbox1(s1_3)
    s1_4 = sbox1(s1_4)

    s2_1 = sbox2(s2_1)
    s2_2 = sbox2(s2_2)
    s2_3 = sbox2(s2_3)
    s2_4 = sbox2(s2_4)

    intermediate2 = s1_1 + s2_1 + s1_2 + s2_2 + s1_3 + s2_3 + s1_4 + s2_4

    # permute
    result = ""
    result += intermediate2[21]
    result += intermediate2[1]
    result += intermediate2[14]
    result += intermediate2[24]
    result += intermediate2[9]
    result += intermediate2[26]
    result += intermediate2[7]
    result += intermediate2[28]
    result += intermediate2[3]
    result += intermediate2[18]
    result += intermediate2[17]
    result += intermediate2[27]
    result += intermediate2[10]
    result += intermediate2[20]
    result += intermediate2[29]
    result += intermediate2[23]
    result += intermediate2[31]
    result += intermediate2[2]
    result += intermediate2[8]
    result += intermediate2[11]
    result += intermediate2[15]
    result += intermediate2[12]
    result += intermediate2[5]
    result += intermediate2[22]
    result += intermediate2[30]
    result += intermediate2[19]
    result += intermediate2[13]
    result += intermediate2[25]
    result += intermediate2[6]
    result += intermediate2[0]
    result += intermediate2[4]
    result += intermediate2[16]

    return result


def sbox1(word):
    if word == '0000':        # 0 -> E
        word = '1110'
    elif word == '0001':      # 1 -> 4
        word = '0100'
    elif word == '0010':      # 2 -> D
        word = '1101'
    elif word == '0011':      # 3 -> 1
        word = '0001'
    elif word == '0100':      # 4 -> 2
        word = '0010'
    elif word == '0101':      # 5 -> F
        word = '1111'
    elif word == '0110':      # 6 -> B
        word = '1011'
    elif word == '0111':      # 7 -> 8
        word = '1000'
    elif word == '1000':      # 8 -> 3
        word = '0011'
    elif word == '1001':      # 9 -> A
        word = '1010'
    elif word == '1010':      # A -> 6
        word = '0110'
    elif word == '1011':      # B -> C
        word = '1100'
    elif word == '1100':      # C -> 5
        word = '0101'
    elif word == '1101':      # D -> 9
        word = '1001'
    elif word == '1110':      # E -> 0
        word = '0000'
    elif word == '1111':      # F -> 7
        word = '0111'

    return word


def sbox2(word):
    if word == '0000':        # 0 -> 5
        word = '0101'
    elif word == '0001':      # 1 -> 6
        word = '0110'
    elif word == '0010':      # 2 -> C
        word = '1100'
    elif word == '0011':      # 3 -> F
        word = '1111'
    elif word == '0100':      # 4 -> 8
        word = '1000'
    elif word == '0101':      # 5 -> A
        word = '1010'
    elif word == '0110':      # 6 -> 0
        word = '0000'
    elif word == '0111':      # 7 -> 4
        word = '0100'
    elif word == '1000':      # 8 -> B
        word = '1011'
    elif word == '1001':      # 9 -> 3
        word = '0011'
    elif word == '1010':      # A -> 7
        word = '0111'
    elif word == '1011':      # B -> D
        word = '1101'
    elif word == '1100':      # C -> E
        word = '1110'
    elif word == '1101':      # D -> 1
        word = '0001'
    elif word == '1110':      # E -> 2
        word = '0010'
    elif word == '1111':      # F -> 9
        word = '1001'

    return word


def xor32(a, b):
    c = ""

    for i in range(len(a)):
        if a[i] == b[i]:
            c += "0"
        elif a[i] != b[i]:
            c += "1"

    return c


def print32(word):
    word1 = word[0:8]
    word2 = word[8:16]
    word3 = word[16:24]
    word4 = word[24:32]

    print(hex(int(word1, 2))[2:].zfill(2), end=' ')
    print(hex(int(word2, 2))[2:].zfill(2), end=' ')
    print(hex(int(word3, 2))[2:].zfill(2), end=' ')
    print(hex(int(word4, 2))[2:].zfill(2))


def print64(word):
    word1 = word[0:8]
    word2 = word[8:16]
    word3 = word[16:24]
    word4 = word[24:32]
    word5 = word[32:40]
    word6 = word[40:48]
    word7 = word[48:56]
    word8 = word[56:64]

    print(hex(int(word1, 2))[2:].zfill(2), end=' ')
    print(hex(int(word2, 2))[2:].zfill(2), end=' ')
    print(hex(int(word3, 2))[2:].zfill(2), end=' ')
    print(hex(int(word4, 2))[2:].zfill(2), end=' ')
    print(hex(int(word5, 2))[2:].zfill(2), end=' ')
    print(hex(int(word6, 2))[2:].zfill(2), end=' ')
    print(hex(int(word7, 2))[2:].zfill(2), end=' ')
    print(hex(int(word8, 2))[2:].zfill(2))


def encrypt10(word, key):

    leftKey = key[0:4]
    rightKey = key[4:8]
    keyList = keyGen(leftKey, rightKey)

    leftText = format(int("0x" + word[0:8], 16), '032b')
    rightText = format(int("0x" + word[8:16], 16), '032b')

    left1 = rightText
    right1 = xor32(leftText, feistel(rightText, keyList[0]))

    left2 = right1
    right2 = xor32(left1, feistel(right1, keyList[1]))

    left3 = right2
    right3 = xor32(left2, feistel(right2, keyList[2]))

    left4 = right3
    right4 = xor32(left3, feistel(right3, keyList[3]))

    left5 = right4
    right5 = xor32(left4, feistel(right4, keyList[4]))

    left6 = right5
    right6 = xor32(left5, feistel(right5, keyList[5]))

    left7 = right6
    right7 = xor32(left6, feistel(right6, keyList[6]))

    left8 = right7
    right8 = xor32(left7, feistel(right7, keyList[7]))

    left9 = right8
    right9 = xor32(left8, feistel(right8, keyList[8]))

    left10 = right9
    right10 = xor32(left9, feistel(right9, keyList[9]))

    left11 = right10
    right11 = left10

    cipherText = left11 + right11
    print("ciphertext : %s" % (cipherText), end='    ')
    print64(cipherText)

    return cipherText


def attack(plaintext, ciphertext):

    key = 'ffffffff'
    cipher = format(int("0x" + ciphertext, 16), '064b')     # 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
    result = encrypt10(plaintext, key)                      # 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000

    while result != cipher and key != '00000000':

        key = str(hex(int("0x" + key, 16) - 1)[2:].zfill(8))
        result = encrypt10(plaintext, key)

    if result == cipher:
        print("Success!")

    return key


def main():

    while True:
        print("")
        option = int(input("What would you like to do? : 1 for Encryption, 2 for Attack, 0 for Exit : "))

        if option == 1:

            print("Enter plaintext...")
            plainText = input("What is the plaintext? (ex:770245FFBAD4173E) : ")

            print("Enter key...")
            key = input("What is the key?(ex:12345678) : ")

            print("")
            print("Encrypting...")

            cipherText = encrypt10(plainText, key)

            print("Result : ", end='')

            print64(cipherText)

        elif option == 2:

            print("Enter plaintext...")
            plainText = input("What is the plaintext? (ex:40ff24330947f610) : ")

            print("Enter ciphertext...")
            cipherText = input("What is the ciphertext? (ex:ec2de1305b5f5b02) : ")

            print("")
            print("Attacking...")

            key = attack(plainText, cipherText)

            print("Result : ", end='')
            print(key)

        elif option == 0:
            print("Bye Bye!")
            sys.exit()

        else:
            print("I don't understand...")
            continue

########################################################################


if __name__ == '__main__':
    main()
