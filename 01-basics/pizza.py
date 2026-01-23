from math import sqrt
from area import circle

def is_prime(n):
    """Returns True if n is prime."""
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def pizza_rate(size, price):
    """Calculates the value of a pizza coupon.

    Args:
        size (int): Diameter of the pizza in inches.
        price (float): Advertised price of the pizza.

    Returns:
        float: The pizza's price per square inch.
    """
    return price / circle(size / 2)

if __name__ == "__main__":

    # Test the is_prime function
    for n in range(10):
        if is_prime(n):
            print(n, "is prime")
        else:
            print(n, "is NOT prime")

    # Test the pizza_rate function
    print()
    print("  Small for $4.99:", pizza_rate(10, 4.99))
    print(" Medium for $5.99:", pizza_rate(12, 5.99))
    print("  Large for $7.99:", pizza_rate(14, 7.99))
    print("X-Large for $9.99:", pizza_rate(16, 9.99))
