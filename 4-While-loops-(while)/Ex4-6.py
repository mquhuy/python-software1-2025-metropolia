from random import uniform
import concurrent.futures


def is_point_in_unit_circle(point) -> bool:
    """
    Returns whether the point denotes by (x, y)
    falls into the unit circle, whose center is (0, 0)
    and radius is 1.
    """
    x, y = point
    return (x**2 + y**2) < 1


def generate_random_point_in_square(length=2.0):
    """
    Return a random point inside a square, whose
    center is (0, 0) and length provided
    """
    upper_limit = length / 2
    lower_limit = upper_limit * (-1)
    return (uniform(lower_limit, upper_limit), uniform(lower_limit, upper_limit))


def generate_random_points_and_check(n, length=2.0):
    """
    Generate n random point inside a square, whose
    center is (0, 0) and length provided, then check
    to see how many of the generated points fall into
    the unit circle.
    """
    n_points_in_circle = 0
    for _ in range(n):
        point = generate_random_point_in_square()
        n_points_in_circle += is_point_in_unit_circle(point)
    return n_points_in_circle


def generate_random_points_and_check_with_futures(n, chunk_size=10000000):
    """
    Use parallelism to increase the speed. Chunk_size needs to be adjusted
    to fit the optimal speed of a single-core process.
    On my machine, a single core could handle 1mil in less than 1s,
    so I use this number as default chunk size.
    """
    # If the number is less than chunk_size, simply use the original function
    # for optimal speed
    if n <= chunk_size:
        return generate_random_points_and_check(n)

    num_workers = n // chunk_size
    chunks = [chunk_size] * num_workers + [n % num_workers]

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        # Submit all chunks
        futures = [
            executor.submit(generate_random_points_and_check, chunk) for chunk in chunks
        ]

        # Collect results as they complete
        n_points_in_circle = 0
        for future in concurrent.futures.as_completed(futures):
            n_points_in_circle += future.result()

    return n_points_in_circle


def main():
    def get_n_points_from_input():
        while True:
            n_points_str = input(
                "Please input the number of points you want to sample: "
            )
            try:
                n_points = int(n_points_str)
                if n_points <= 0:
                    raise ValueError("Only accept positive integers")
                return n_points
            except ValueError:
                print("Only accept valid integers")

    n_points = get_n_points_from_input()
    n_points_in_circle = generate_random_points_and_check_with_futures(n_points)
    print(
        f"Approximation of pi calculated from this sample: {4 * n_points_in_circle / n_points}"
    )


if __name__ == "__main__":
    main()
