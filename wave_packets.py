# Animated Gaussian wave packet
def yw(x,t): 
  dlam = 0.58
  lam0 = 10
  A1 = 1
  return A1*exp(-2*(dlam*pi*x/lam0**2)**2)* cos(2*pi*x/lam0)

fig = figure()
ax = axes(xlim=(-100, 100), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = linspace(-100,100,1000)
    for i in linspace(-100,100,1000):
      y = yw(x,i/10)
      i = i/10
    line.set_data(x, y)
    return line,    
    

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=100, blit=True)

HTML(anim.to_jshtml())
