import os
from PIL import Image
from imagehash import average_hash

def remove_duplicates(directory):
    image_hashes = {}  # Dictionary to store image hashes

    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            image_path = os.path.join(directory, filename)
            with Image.open(image_path) as img:
                # Calculate the hash of the image
                img_hash = str(average_hash(img))
            
            # Check if the hash is already in the dictionary (duplicate)
            if img_hash in image_hashes:
                print(f"Removing duplicate: {filename}")
                os.remove(image_path)
            else:
                # Add the hash to the dictionary
                image_hashes[img_hash] = filename

if __name__ == "__main__":
    image_directory = "1986imgs"  # Replace with your image directory
    remove_duplicates(image_directory)
