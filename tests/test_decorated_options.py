from decorated_options import Options, optioned

def test_options():
    opts = Options(a=10, b=0.1)
    assert opts.a == 10
    assert opts.b == 0.1

    assert opts.get('a') == 10
    assert opts.get('b') == 0.1

    new_opts = opts.set(a=20)

    assert new_opts.a == 20
    assert new_opts.b == 0.1

    new_opts = new_opts.set('b', 100)

    assert new_opts.get('b') == 100

    new_opts = new_opts.set(a=1, b=1)

    assert new_opts.a == 1
    assert new_opts.b == 1

    assert 'b' in new_opts
    assert 'a' in new_opts.keys()

# TODO: Add a test for immutability


def test_optioned():
    def foo(a, b=1):
        return a, b

    bar = optioned('opts')(foo)

    assert bar(opts=Options(a=10)) == (10, 1)
    assert bar(opts=Options(a=10, b=None)) == (10, None)
    assert bar(opts=Options(), a=10, b=2) == (10, 2)
    assert bar(10, opts=Options(b=10)) == (10, 10)
    assert bar(10) == (10, 1)
    assert bar(10, 100) == (10, 100)

    def baz(a, sim_opts):
        return a, sim_opts.b

    bar = optioned('sim_opts')(baz)

    assert bar(10, sim_opts=Options(b=10)) == (10, 10)
    assert bar(sim_opts=Options(a=20, b=20)) == (20, 20)

    # TODO: Add functions which take **kwargs or **args arguments.
