import functools

# I made this recipe to address a frequent
# problem I have with multiprocessing `Process`
# objects, and I need to hit different functions

def multimap(functions, fargs):
    partials = [
            functools.partial(f)
            for f in functions
    ]
    combined = zip(partials, fargs)
    return combined

if __name__ == '__main__':
    import multiprocessing, time, random
    import threading
    # Placeholder functions
    a = lambda thing: print('a:', random.choice((True, False)))
    b = lambda thing: print('b:', True)
    c = lambda thing: print('c:', False)
    A, B, C = (1, 'a', {"This": "Not This"})
    
    multi_targets = multimap((a, b, c, a, b, c, a, b, c), (A, B, C, A, B, C, A, B, C ))
    jobs = []
    for target in multi_targets:
        p = threading.Thread(target=target[0], args=(target[1],))
        jobs.append(p)
        p.start()
    for index, thread in enumerate(jobs):
        thread.join()
