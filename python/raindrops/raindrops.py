def convert(num: int) -> str:
    # Output response used for joining in the comprehension.
    resp = ''
    # Divisors to be used in the calculation (key) with the
    # corresponding result string (value).
    divs = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
    }

    # Comprehension for determining result.
    res = [resp + divs[i] for i in divs if num % i == 0]

    # Return result unless unable to divide by any divisor and
    # else return the initial integer in string format.
    if len(res) > 0: return ''.join(res)
    return str(num)

