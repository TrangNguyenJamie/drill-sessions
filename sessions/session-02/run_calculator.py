# TODO: import your function here
from calculator.variadic.mul import prod     # NICE TRICK!
from calculator.add import add

if __name__ == "__main__":
    # TODO 1: import the function of adding two integers and compute a + b 
    a, b = 1, 2
    result_add = add(a,b)
    print(f"{a} + {b} = {result_add}")

    # TODO 2: import the function of multiplying multiple integers and calculate c * d * e * f * g in a single line
    c, d, e, f, g = 1, 2, 3, 4, 5
    result_mul = prod(c,d,e,f,g)
    print(f"{c} * {d} * {e} * {f} * {g} = {result_mul}")
