import random

EXCHANGER = 10
EXCHANGER_RANGE = (0.17, 0.22)

COVER = 2
COVER_RANGE = (0.38, 0.44)

DEPTH_TOLERANCE_RANGE = (0.09, 0.12)


def generate_set() -> tuple:
    """
    Generates set of 3 numbers.
    (depth of exchanger,
    dept of cover,
    sum of both depths with deviation)
    """
    exch_depth = round(float(EXCHANGER) + random.uniform(*EXCHANGER_RANGE), 2)
    cover_depth = round(float(COVER) + random.uniform(*COVER_RANGE), 2)

    depth_sum = exch_depth + cover_depth

    total_depth = round(depth_sum + random.uniform(*DEPTH_TOLERANCE_RANGE), 2)

    dev = round(total_depth - depth_sum, 2)

    msg = f"Exchanger depth: {exch_depth}\n" \
          f"Cover depth: {cover_depth}\n" \
          f"Depth sum: {depth_sum}\n" \
          f"Total depth: {total_depth}\n" \
          f"Deviation: {dev}"

    output = exch_depth, cover_depth, total_depth

    return output


if __name__ == '__main__':
    for _ in range(9):
        print(generate_set())
