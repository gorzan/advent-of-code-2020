import math
import numpy as np
input_text = open('input.txt').read().split('\n')
ts = int(input_text[0])
buses = input_text[1].split(',')


def when(bus, ts):
    trips = math.floor(ts / bus)
    next = (trips + 1) * bus if trips*bus < ts else trips*bus
    return next - ts


def part_one(ts, buses):
    wait = 10000
    next_bus = None
    for bus in buses:
        if bus.isdigit():
            bus = int(bus)
            bus_wait = when(bus, ts)
            if bus_wait < wait:
                wait = bus_wait
                next_bus = bus
    print(f'Part One: Next bus is {next_bus} in {wait} minutes. Result: {int(next_bus) * int(wait)}')


def check_ts(ts, buses):
    for index, bus in enumerate(buses):
        if bus != 'x':
            if (ts + index) % int(bus) > 0:
                return False
    return True


part_one(ts, buses)


# Had to steal from mortenlj again
def part_two(buses):
    buses = np.array([int(v) if v!='x' else 1 for v in buses])
    ts = buses[0]
    ts_series = np.arange(ts, ts + len(buses))
    mods = np.mod(ts_series, buses) == 0
    while not np.all(mods):
        valid = buses[mods]
        ts += np.multiply.reduce(valid)
        ts_series = np.arange(ts, ts + len(buses))
        mods = np.mod(ts_series, buses) == 0
    print(f"Part Two: The first possible timestamp is {ts}")


part_two(buses)
