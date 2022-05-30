import random
import argparse


EXCHANGER_RANGE = (10.17, 10.22)
COVER_RANGE = (2.38, 2.44)
DEPTH_TOLERANCE_RANGE = (0.09, 0.12)


def generate_set() -> list:
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

    return [exch_depth, cover_depth, total_depth]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Amount of values per sheet
    parser.add_argument("amount", help="Amount of values per sheet.")
    # Number of sheets
    parser.add_argument("-c", "--count", help="Number of sheets generated.")
    # Include 'OK' value
    parser.add_argument("-k", action="store_true", help="Whether or not to include the 'OK' value. (default=True)")

    args = parser.parse_args()
    try:
        amount = int(args.amount)
    except ValueError:
        raise Exception("Argument 'amount' must be a whole number!")

    try:
        sheet_count = int(args.count) if args.count else 1
    except (ValueError, TypeError):
        raise Exception("Argument 'count' must be a whole number!")

    include_k = args.k

    # Loop through amount of sheets required
    for step in range(1, sheet_count+1):

        # Start the .csv file
        with open(f"{step}_{amount}.csv", "w") as f:

            # Loop through number of required values
            for _ in range(amount):

                # Generates values and converts them to string format with 2 digits following the decimal point
                generated_values = ["{:0.2f}".format(value) for value in generate_set()]

                # Add 'OK' value if required
                if include_k:
                    generated_values.append("OK")

                # Write the line into the file
                f.write(",".join(generated_values))
                f.write("\n")

