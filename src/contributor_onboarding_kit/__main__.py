from .summary import format_summary


def main() -> None:
    print(format_summary("new contributor", ["reviewed docs"]))


if __name__ == "__main__":
    main()
