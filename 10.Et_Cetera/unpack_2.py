def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)

def g(*args, **kwargs):
    print("Named:", kwargs)

g(galleons=100, sickles=50, knuts=25)

