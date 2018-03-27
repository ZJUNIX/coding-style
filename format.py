from codecs import open
from pathlib import Path
from subprocess import run
from argparse import ArgumentParser
from sys import argv


def load_config() -> str:
    config_file = Path(argv[0]).parent / 'coding-style'
    config = '\"{'
    with open(config_file, 'r', 'utf-8') as f:
        for line in f:
            config += line.rstrip()
            config += ','
    config = config.rstrip(',') + '}\"'
    return config


def run_format(config: str, src_path: str):
    src_files = ''
    for file_name in Path(src_path).rglob('*.[ch]'):
        src_files += str(file_name.resolve()) + ' '
        print('FORMAT ' + str(file_name))
    cmd = ' '.join(['clang-format', '-i', src_files, '-style', config])
    run(cmd, shell=True)


def main():
    # read args
    parser = ArgumentParser(description='Format source files.')
    parser.add_argument('path', default='.',
                        help='Path of code.')
    args = parser.parse_args()

    # run format
    config = load_config()
    run_format(config, args.path)


if __name__ == '__main__':
    main()
