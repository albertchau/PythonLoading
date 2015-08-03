__author__ = 'achau1'

import zipfile
from pathlib import Path
import shutil

# fh = open('test.zip', 'rb')
# z = zipfile.ZipFile(fh)
# for name in z.namelist():
# outpath = "C:\\"
#     z.extract(name, outpath)
# fh.close()

# given /<path>

# create a matching directory called /<path>-extracted

# for every file in <path> ->
# check if file
# create a file with the same repository structure

def optionseod(p):
    path = Path(p)

    if not path.exists() and not path.is_dir():
        raise BrokenPipeError("can't find path yo or not a good path yo")

    extracted_path = path.parent / (path.name + "_extracted")

    if extracted_path.exists():
        shutil.rmtree(str(extracted_path))

    extracted_path.mkdir()

    path_stack = []
    for child in path.iterdir():
        path_stack.append(child)

    while path_stack:
        cur_path = path_stack.pop()
        if cur_path.is_dir():
            for child in cur_path.iterdir():
                path_stack.append(child)
        elif cur_path.is_file():
            if cur_path.name.endswith('zip'):
                file = open(str(cur_path), 'rb')
                zip_file = zipfile.ZipFile(file)
                for file_name in zip_file.namelist():
                    zip_file.extract(file_name, str(extracted_path))
                file.close()
        else:
            print("???")
            # check if it is a zip file
            # if it is -> extract it to extracted path
            # is a file


optionseod('options-eod')
optionseod('options-eod-calcs')
optionseod('options-eod-ivindex')
