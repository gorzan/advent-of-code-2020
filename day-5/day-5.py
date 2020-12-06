boarding_passes = open('input.txt').read().split('\n')


def seat_id(row, column):
    return (row*8) + column


def get_row_part(boarding_pass):
    return boarding_pass[:7]


def get_column_part(boarding_pass):
    return boarding_pass[7:]


def row_num(boarding_pass):
    boarding_pass_row = get_row_part(boarding_pass)
    row = '0b'
    for char in boarding_pass_row:
        if char == 'F':
            row = row + '0'
        elif char == 'B':
            row = row + '1'
    row = int(row, 2)
    return row


def column_num(boarding_pass):
    boarding_pass_column = get_column_part(boarding_pass)
    column = '0b'
    for char in boarding_pass_column:
        if char == 'L':
            column = column + '0'
        elif char == 'R':
            column = column + '1'
    column = int(column, 2)
    return column


def part_one(boarding_passes):
    max_seat = 0
    for boarding_pass in boarding_passes:
        row = row_num(boarding_pass)
        col = column_num(boarding_pass)
        seat = seat_id(row, col)
        if seat > max_seat:
            max_seat = seat

    print(f'Part 1: Max Seat ID: {max_seat}')


def part_two(boarding_passes):
    seat_ids = [seat_id(row_num(boarding_pass), column_num(boarding_pass)) for boarding_pass in boarding_passes]
    min_seat = min(seat_ids)
    max_seat = max(seat_ids)
    for seat in range(min_seat, max_seat+1):
        if seat not in seat_ids:
            print(f'Part 2: Unoccupied seat: {seat}')


part_one(boarding_passes)
part_two(boarding_passes)
