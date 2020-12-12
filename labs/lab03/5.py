from os.path import isdir, getsize, getmtime, dirname, abspath
from shutil import disk_usage
import tempfile
import argparse


def tenet(input_file_path: str, output_file_path: str = None) -> str:
    if isdir(input_file_path):
        raise ValueError(input_file_path + " is a directory")

    with open(input_file_path, "r") as input_file:
        time1 = getmtime(input_file_path)  # don't even know how to test it, but i hope it works
        lines = input_file.readlines()
        time2 = getmtime(input_file_path)
        if time1 != time2:
            raise RuntimeError("Input file was changed during runtime")

    if output_file_path is None:
        output_file = tempfile.NamedTemporaryFile("w", delete=False)
        output_file_path = output_file.name
    else:
        output_file = open(output_file_path, "w")
    if getsize(input_file_path) > disk_usage(dirname(abspath(output_file_path))).free:
        raise MemoryError("Not enough disk space")

    for s in lines:
        output_file.write((s.strip('\n'))[::-1] + '\n')

    return output_file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str, nargs='?')
    args = parser.parse_args()

    print(tenet(args.input, args.output))
