# on terminal type: python transfer_script.py aims cnd/book/website

import os
import shutil
import argparse

def transfer_files(source_dir, dest_dir):
    # Ensure directories exist
    if not os.path.exists(source_dir) or not os.path.exists(dest_dir):
        print("Error: One or both directories do not exist.")
        return

    # List of items to transfer
    items_to_transfer = [
        ('foreword', ''),
        ('_static', '_static'),
        ('project-design', 'project-design'),
        ('scripts', 'scripts'),
        ('index.md', 'index.md'),
        ('_config.yml', 'config.yml')
    ]

    for source_item, dest_item in items_to_transfer:
        source_path = os.path.join(source_dir, source_item)
        dest_path = os.path.join(dest_dir, dest_item if dest_item else source_item)

        if not os.path.exists(source_path):
            print(f"Warning: {source_path} does not exist. Skipping.")
            continue

        try:
            if os.path.isdir(source_path):
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
                shutil.copytree(source_path, dest_path)
            else:
                shutil.copy2(source_path, dest_path)
            print(f"Transferred: {source_path} -> {dest_path}")
        except Exception as e:
            print(f"Error transferring {source_path}: {str(e)}")

    print("Transfer process completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transfer files and folders between projects.")
    parser.add_argument("source", help="Source directory path")
    parser.add_argument("destination", help="Destination directory path")
    args = parser.parse_args()

    transfer_files(args.source, args.destination)