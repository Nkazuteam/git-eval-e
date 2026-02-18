def fizzbuzz(n):
    results = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            results.append("fizzbuzz")
        elif i % 3 == 0:
            results.append("fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results


def main():
    results = fizzbuzz(30)
    for item in results:
        print(item)


if __name__ == "__main__":
    main()
