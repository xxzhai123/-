indent = '    '


def get_pure_yield_day(pmol, specification, work_day_year, productive_ability):
    kg = productive_ability*1000/work_day_year*specification
    kmol = kg/pmol
    print('日产纯品量为：%.2fkg, %.2fkmol' % (kg, kmol))
    return (kg, kmol)


def get_yield(yields):
    product = 1
    for a_yield in yields:
        product *= a_yield
    product_percent = product*100
    print('总为产率：%.2f%%' % product_percent)
    return product


def snA(n):
    return chr(ord('A')+n-1)+'- '


def sna(n):
    return chr(ord('a')+n-1)+'- '


def od(n):
    return '('+str(n)+') '
