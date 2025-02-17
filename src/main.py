import random
import time


def do_foo(a: int, b: int) -> int:
    print(f"[INFO] [{time.strftime("%Y/%m/%d %H:%M:%S")}] Doing foo")
    return ((a + b) ** 2) - (a + b)


def main():
    bar = do_foo(random.randrange(1, 10), random.randrange(10, 15))
    print(f"[INFO][{time.strftime("%Y/%m/%d %H:%M:%S")}] Result: [{bar}]")


if __name__ == "__main__":
    main()
