import random

EXCHANGER_RANGE = (10.17, 10.22)
COVER_RANGE = (2.38, 2.44)
DEPTH_TOLERANCE_RANGE = (0.09, 0.12)


def generate_set() -> tuple:
    """
    Generates set of 3 numbers.
    (depth of exchanger,
    dept of cover,
    sum of both depths with deviation)
    """
    exch_depth = round(random.uniform(*EXCHANGER_RANGE), 2)
    cover_depth = round(random.uniform(*COVER_RANGE), 2)

    depth_sum = exch_depth + cover_depth

    total_depth = round(depth_sum + random.uniform(*DEPTH_TOLERANCE_RANGE), 2)

    dev = round(total_depth - depth_sum, 2)

    msg = f"Exchanger depth: {exch_depth}\n" \
          f"Cover depth: {cover_depth}\n" \
          f"Depth sum: {depth_sum}\n" \
          f"Total depth: {total_depth}\n" \
          f"Deviation: {dev}"

    assert dev < 0.2, "Deviation exceeded 0.2mm! Check the DEPTH_TOLERANCE_RANGE."

    return exch_depth, cover_depth, total_depth


if __name__ == '__main__':
    for _ in range(9):
        print(generate_set())
