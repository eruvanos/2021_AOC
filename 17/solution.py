# fmt: off
import sys

from utils.vector import Vec2, get_max_y

sys.path.append("..")


# fmt: on

def simulate(velocity: Vec2, target):
    pos = Vec2(0, 0)
    velocity = Vec2(*velocity)
    min_x, max_x, min_y, max_y = target

    dx = velocity.x / velocity.x if velocity.x else 0

    trajectory = [pos]
    while True:
        pos += velocity
        velocity = velocity - Vec2(dx if velocity.x > 0 else 0, 1)
        trajectory.append(pos)

        # end because hit
        if min_x <= pos.x <= max_x and min_y <= pos.y <= max_y:
            return True, trajectory

        # end because overshoot
        if pos.x > max_x or pos.y < min_y:
            return False, trajectory



def part_1(data):
    vx, vy = 0, 0

    # collect simulation data
    simulations = {}
    while True:
        test_v = Vec2(vx, vy)
        hit, trajectory = simulate(test_v, target=data)

        print(f"{'HIT ' if hit else 'MISS'} {test_v}: {get_max_y(trajectory)}")

        if hit:
            simulations[test_v] = trajectory

        # guess better trajectory
        vx += 1
        if vx > 100:
            vy += 1
            vx = 1
        if vy > 110:
            break

    # get highes path
    max_y = 0
    for v, trajectory in simulations.items():
        max_y = max(max_y, get_max_y(trajectory))

    return max_y


def part_2(data):
    vx, vy = 0, -200

    # collect simulation data
    simulations = {}
    while True:
        test_v = Vec2(vx, vy)
        hit, trajectory = simulate(test_v, target=data)

        # print(f"{'HIT ' if hit else 'MISS'} {test_v}: {get_max_y(trajectory)}")

        if hit:
            simulations[test_v] = trajectory

        # guess better trajectory
        vx += 1
        if vx > 300:
            vy += 1
            vx = 1
        if vy > 200:
            break

    return len(simulations)


def parse(lines):
    # target area: x=20..30, y=-10..-5
    line = lines[0]
    x_range, y_range = line.replace("target area: ", "").split(", ")
    x_start, x_end = x_range[2:].split("..")
    x_start = int(x_start)
    x_end = int(x_end)

    y_start, y_end = y_range[2:].split("..")
    y_start = int(y_start)
    y_end = int(y_end)

    return x_start, x_end, y_start, y_end


def main(puzzle_input_f):
    lines = [l.strip() for l in puzzle_input_f.readlines() if l]
    print("Part 1: ", part_1(parse(lines[:])))
    print("Part 2: ", part_2(parse(lines[:])))


if __name__ == "__main__":
    import os
    from aocpy import input_cli

    base_dir = os.path.dirname(__file__)
    with input_cli(base_dir) as f:
        main(f)
