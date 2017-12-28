from collections import defaultdict

# Dirty solution, should have used equations

# P(t) = p0 + v0 * t + ((t * (t + 1)) / 2) * a0

class Particle:
    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc
    
    def tick(self):
        for i in range(3):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]

particles = defaultdict(list)

with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        splitted = line.rstrip('\n').split()
        pos = [int(num) for num in splitted[0][3:-2].split(',')]
        vel = [int(num) for num in splitted[1][3:-2].split(',')]
        acc = [int(num) for num in splitted[2][3:-1].split(',')]
        
        particles[tuple(pos)].append(Particle(pos, vel, acc))

n = 1000

# Run n times
for _ in range(n):
    particles_temp = defaultdict(list)
    for pos, particle_list in particles.items():
        if len(particle_list) == 1:
            p = particle_list[0]
            p.tick()
            particles_temp[tuple(p.pos)].append(p)

    particles = particles_temp

print(len(particles))
