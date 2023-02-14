"""
5. Напиши функцию на Python, выполняющую сравнение версий. Условия:
- Return -1 if version A is older than version B
- Return 0 if version A and B are equivalent
- Return 1 if version A is newer than version B
- Each subsection is supposed to be interpreted as a number,
therefore 1.10 > 1.1.
"""
import re


def compare(a, b):
    """
    Сравнение версий с исходными типами int, float, str
    с учетом любого разделителя (.,-)
    """
    new_a, new_b = str(a), str(b)
    len_a, len_b = len(re.split(r'\D', str(a))), len(re.split(r'\D', str(b)))
    zero_insert = abs(len_a - len_b)
    if len_a < len_b:
        new_a += '.0' * zero_insert
    else:
        new_b += '.0' * zero_insert
    version_a, version_b = re.split(r'\D', new_a), re.split(r'\D', new_b)
    for i in range(len(version_a)):
        if int(version_a[i]) < int(version_b[i]):
            return -1
        if int(version_a[i]) > int(version_b[i]):
            return 1
    return 0


assert compare(1.11, 1.12) == -1, 'A is older than B'
assert compare(1.11, 1.11) == 0, 'A equivalent B'
assert compare(1.12, 1.11) == 1, 'A is newer than B'
assert compare('1.0.1.2', '1.0.3') == -1, 'A is older than B'
assert compare('1.0.1.2', '1.0.1.2') == 0, 'A equivalent B'
assert compare('1.0.2.2', '1.0.1') == 1, 'A is newer than B'
assert compare('1-2021', '1-2021') == 0, 'A equivalent B'
assert compare('2,023, 2,023') == 0, 'A equivalent B'
