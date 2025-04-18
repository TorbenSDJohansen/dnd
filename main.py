from inventory import INVENTORY


def main():
    for key, value in INVENTORY.__dict__.items():
        print(key, value)


if __name__ == '__main__':
    main()
