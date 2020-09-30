from os.path import isdir


def tenet(input_file_path: str, output_file_path: str) -> None:
    if input_file_path == output_file_path:
        raise ValueError("The output matches the input")
    if isdir(input_file_path):
        raise ValueError(input_file_path + " is a directory")
    input_file = open(input_file_path, "r")
    output_file = open(output_file_path, "w")
    for s in input_file.readlines():
        output_file.write((s.strip('\n'))[::-1] + '\n')


if __name__ == '__main__':
    tenet("tenet.in", "tenet.out")
