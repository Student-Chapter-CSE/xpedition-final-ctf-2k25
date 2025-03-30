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
