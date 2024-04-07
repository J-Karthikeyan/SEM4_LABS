def f(x):
    return x**2 + 5*x + 6

def HillClimbSearch(func, domain, step = 0.002, max_iter = 10000):
    x = 0
    minimum, maximum  = domain
    for i in range(max_iter):
        if x > minimum and x < maximum:
            x = max(x - step, x, x + step, key = func)
            y = func(x)
        else:
            break
        if i%50 == 0:
            print(f"iter {i} : x = {x} f(x) = {y}")
    print(f"Final value of x (iter {i}) = {x} f(x) = {y}")
        
if __name__ == "__main__":
    x = HillClimbSearch(f,(-10,10))
