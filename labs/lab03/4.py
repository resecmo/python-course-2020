import argparse
import tempfile
from os.path import isdir, getsize, getmtime, dirname, abspath
from shutil import disk_usage


def tenet(input_file_path: str, output_file_path: str = None) -> str:
    if input_file_path == output_file_path:
        raise ValueError("The output matches the input")
    if isdir(input_file_path):
        raise ValueError(input_file_path + " is a directory")

    if output_file_path is None:
        output_file = tempfile.NamedTemporaryFile("w", delete=False)
        output_file_path = output_file.name
    else:
        output_file = open(output_file_path, "w")
    if getsize(input_file_path) > disk_usage(dirname(abspath(output_file_path))).free:
        raise MemoryError("Not enough disk space")

    with open(input_file_path, "r") as input_file:
        time1 = getmtime(input_file_path)  # don't even know how to test it, but i hope it works
        for s in input_file:
            output_file.write((s.strip('\n'))[::-1] + '\n')
        time2 = getmtime(input_file_path)
        if time1 != time2:
            raise RuntimeError("Input file was changed during runtime")

    output_file.close()

    return output_file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str, nargs='?')
    args = parser.parse_args()

    print(tenet(args.input, args.output))
