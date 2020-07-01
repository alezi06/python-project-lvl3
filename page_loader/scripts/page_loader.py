import logging
import page_loader.logging  # noqa: F401
from page_loader.cli import parse_args
from page_loader.load import load_page


def main():
    logger = logging.getLogger()
    args = parse_args()
    logger.setLevel(args.log.upper())
    logger.info('Load started')
    load_page(args.url, args.output)
    logger.info('Load finished')


if __name__ == '__main__':
    main()
