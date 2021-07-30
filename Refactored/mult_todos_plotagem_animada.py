from matplotlib import pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)

for i in [1, 2, 4, 8, 7, 5]:
    plt.plot([i] * 11)
    camera.snap()

animation = camera.animate()
animation.save('celluloid_minimal.gif', writer='imagemagick')
