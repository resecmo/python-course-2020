from os.path import isdir
import tempfile
import argparse


def tenet(input_file_path: str, output_file_path: str = None) -> str:
    if input_file_path == output_file_path:
        raise ValueError("The output matches the input")
    if isdir(input_file_path):
        raise ValueError(input_file_path + " is a directory")

    input_file = open(input_file_path, "r")

    if output_file_path is None:
        output_file = tempfile.NamedTemporaryFile("w", delete=False)
        output_file_path = output_file.name
    else:
        output_file = open(output_file_path, "w")

    for s in input_file:
        output_file.write((s.strip('\n'))[::-1] + '\n')

    input_file.close()
    output_file.close()

    return output_file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str, nargs='?')
    args = parser.parse_args()
    print(tenet(args.input, args.output))
