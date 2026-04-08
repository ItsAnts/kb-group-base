def simple_generate(val):
    while val > 0:
        val -= 1
        yield val
    
gen_iter = simple_generate(5)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
