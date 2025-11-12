def approximate_pi(n_terms):
    app_pi = 0
    for i in range(n_terms):
        app_pi += (-1)**i / (2 * i + 1)
    app_pi *= 4
    return app_pi
