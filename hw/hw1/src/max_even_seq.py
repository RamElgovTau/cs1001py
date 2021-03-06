def max_even_seq(n):
    """
    finds the the maximal length of an even subsequence of digits,
    that's included in n's decimal representation.
    :param n: a non-negative integer.
    :return: max length of the sub sequence
    """

    max_even = 0
    current_even_seq = 0  # counter for the current even sequence length.

    for i in str(n):
        if int(i) % 2 == 0:
            current_even_seq = current_even_seq + 1
        else:
            current_even_seq = 0  # prepare to count another even sequence
        if current_even_seq > max_even:  # reached the end of the current even sequence. update max_even if needed.
            max_even = current_even_seq

    return max_even


def test():
    if max_even_seq(23300247524689) != 4:
        print("Error in test 1")
    else:
        print(max_even_seq(23300247524689))
    if max_even_seq(0) != 1:
        print("Error in test 2")
    else:
        print(max_even_seq(0))
    if max_even_seq(13579751) != 0:
        print("Error in test 3")
    else:
        print(max_even_seq(13579751))
    if max_even_seq(2468645) != 6:
        print("Error in test 4")
    else:
        print(max_even_seq(2468645))
    if max_even_seq(12121212) != 1:
        print("Error in test 5")
    else:
        print(max_even_seq(12121212))
    if max_even_seq(808988) != 3:
        print("Error in test 6")
    else:
        print(max_even_seq(808988))
    if max_even_seq(2) != 1:
        print("Error in test 7")
    else:
        print(max_even_seq(2))
    if max_even_seq(7) != 0:
        print("Error in test 8")
    else:
        print(max_even_seq(7))


