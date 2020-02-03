import functools

# I made this recipe to address a frequent
# problem I have with multiprocessing `Process`
# objects, and I need to hit different functions

def multimap(functions, fargs):
    partials = [
            functools.partial(f)
            for f in functions
    ]
    combined = list(zip(partials, fargs))
    return combined

if __name__ == '__main__':
    import multiprocessing, time
    
    # Placeholder functions
    a = lambda thing: random.choice((True, False))
    b = lambda thing: True
    c = lambda thing: False
    A, B, C = (1, 'a', {"This": "Not This"})
    
    multi_targets = multimap((a, b, c), (A, B, C))
    jobs = []
    for target in multi_targets:
        p = multiprocessing.Process(target=target[0], args=(target[1],)
        jobs.append(p)
        p.start()
