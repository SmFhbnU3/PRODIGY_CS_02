from PIL import Image

def encrypt_image(input_path, output_path, key=50):
    # Open an image file
    with Image.open(input_path) as img:
        pixels = img.load()
        width, height = img.size

        # Encrypt the image by modifying pixel values
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[x, y] = (r, g, b)
        
        # Save the encrypted image
        img.save(output_path)

def decrypt_image(input_path, output_path, key=100):
    # Open an image file
    with Image.open(input_path) as img:
        pixels = img.load()
        width, height = img.size

        # Decrypt the image by reversing the pixel value modification
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[x, y] = (r, g, b)
        
        # Save the decrypted image
        img.save(output_path)

# Get input from the user
input_path = input("Enter the path of the image to encrypt: ").strip().strip('"')
encrypted_path = input("Enter the path to save the encrypted image: ").strip().strip('"')
decrypted_path = input("Enter the path to save the decrypted image: ").strip().strip('"')

# Encrypt and decrypt the image with a fixed key value of 100
encrypt_image(input_path, encrypted_path)
decrypt_image(encrypted_path, decrypted_path)

print("Encryption and decryption completed successfully.")