from page_loader.cli import parse_args
from page_loader.load import load_page


def main():
    args = parse_args()
    load_page(args.url, args.output)


if __name__ == '__main__':
    main()
