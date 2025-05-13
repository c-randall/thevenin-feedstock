import thevenin as thev

sim = thev.Simulation()

expr = thev.Experiment()
expr.add_step('current_C', 1., (3600., 1.), limits=('voltage_V', 3.))

soln = sim.run(expr)
soln.plot('time_h', 'voltage_V')

print("\n\n")
print(soln)
print("\n\n")

assert all(soln.success)
