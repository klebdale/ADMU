"""
    Kleb Dale G. Bayaras
    217095
    ADMU MSCS
    Python 2.7

    Custom Hash Function Algo
        Pass each string to the hash function
        Take each character and convert it to their ASCII Decimal equivalent
        Multiply the ASCII Decimal equivalent by the number of their order in the string (start with 1)
        Sum it all up
        Divide it with a random big prime number
        Take the remainder and use this as hash value or index for the hash table

    Explanation
        A good hash function should:
            1) The hash value is fully determined by the data being hashed.
            2) The hash function uses all the input data.
            3) The hash function "uniformly" distributes the data across the entire set of possible hash values.
            4) The hash function generates very different hash values for similar strings.

        In relation to the custom hash function:
            1) The hash value generated is fully dependent on the value being passed to the hash_function.
            All the things needed for the computation is derived solely from the value passed and no other factors are being injected.

            2) The custom hash function uses all the input data and not just a part of it. It uses each character and its ASCII equivalent and
            it also utilizes the order of characters

            3) The custom hash function distributes it evenly with all the possible permutations and combinations based on the arrangement
            of the characters. However, to avoid 'blowing up' the numbers, it is divided by a big prime number (7919 in this case).
            This might somewhat contradict rule #1 but the prime number used is constant and is used to not produce very big values.
            I can't prove it with mathematical equations the number of possible permutations and combinations
            but based on the prime number being divided it to, it signifies the number of unique values before the hash_value clusters

            4) The custom hash function produces the same hash value for exactly the same string, it is consistent. However, it produces
            different hash value for 'similar' strings or strings with very small changes such as capitalization, shuffling of characters,
            addition of a character, whitespaces, etc.

            Note: Hash Function Formula is
             ₓ
            (∑ xnₓ ) % 7919 | where x is length of string; n is each character of the string
             ¹
            I found two strings with similar hash value by equating x+2y = a+2b ; where x=126 (~), y=33(!), a=32( ), b=80(P) ; '~!' = ' P'
            In general, it can only be equal if it can satisfy:
            n₁ + 2n₂ + ... xnₓ = m₁ + 2m₂ + ... + xmₓ or
            (n₁ - m₁) + 2(n₂ - m₂) + ... + x(nₓ - mₓ) = 0
"""


def hash_function(key):
    sum = 0
    ascii_value = 0

    for index in range(0, len(key)):
        ascii_value = ord(key[index])
        sum += (ascii_value * (index+1))

    hash_value = sum % 7919
    return hash_value


def main():
    strings = ['~!', ' P', 'Apples', 'Avocado', 'Afritada', 'afritada', 'Orange', 'Oraneg', 'Aftokrator', 'Uvuvwevwevwe', 'Uvuvwevwevwez', '1023', 'Algo', 'Al go']
    for word in strings: print(word, hash_function(word))


if __name__ == '__main__':
    main()
