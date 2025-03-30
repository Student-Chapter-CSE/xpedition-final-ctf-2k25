# Challenge

## Title

The Hydra Archive

## Description

Hydra has developed a new way to bury their secrets—deep inside a recursive archive that seems to go on forever.
S.H.I.E.L.D. intercepted a mysterious ZIP file, but every time they extract it, another ZIP file appears, like cutting off one head of Hydra only for two more to take its place.

Agent Coulson suspects that at the very core of this endless compression lies a hidden flag. But will you have the patience to reach it?

## Files

- `archive_999.zip` - A ZIP file that contains another ZIP file, and so on, up to 999 levels deep.

## Solution

To solve this challenge, we need to extract the ZIP file recursively until we reach the innermost file that contains the flag. The process involves the following steps:

1. **Extract the ZIP file**: Use a ZIP extraction tool or library to extract the contents of `archive_999.zip`.
2. **Check for another ZIP file**: After extracting, check if the extracted contents include another ZIP file. If so, repeat the extraction process on that file.
3. **Continue until no more ZIP files**: Keep extracting until you reach a file that does not contain another ZIP file.

We can use a python script to automate this process. The script will open the ZIP file, extract its contents, and check for any nested ZIP files until it finds the final file containing the flag.

```python
import zipfile
import os
import shutil

def unzip_recursive(zip_path, output_dir):
    current_zip = zip_path
    iteration = 0

    while True:
        extract_path = os.path.join(output_dir, f"temp_extracted")

        with zipfile.ZipFile(current_zip, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        os.remove(current_zip)
        print(f"Extracted and deleted: {current_zip}")
        
        next_zip = None
        for root, _, files in os.walk(extract_path):
            for file in files:
                if file.endswith(".zip"):
                    next_zip = os.path.join(root, file)
                    break

        if not next_zip:
            print(f"Final extraction completed in: {extract_path}")
            break 

        next_zip_dest = os.path.join(output_dir, f"archive_{iteration}.zip")
        shutil.move(next_zip, next_zip_dest)
        current_zip = next_zip_dest
        iteration += 1

        shutil.rmtree(extract_path)
        os.makedirs(extract_path, exist_ok=True)

zip_path = "archive_999.zip"
output_dir = "unzipped_data"
os.makedirs(output_dir, exist_ok=True)

unzip_recursive(zip_path, output_dir)
```

## Flag

```text
gnosis{h34ds_k33p_c0m1ng_unz1p_f0r3v3r}
```
