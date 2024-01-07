#!/usr/bin/env python
# coding: utf-8

import numpy as np
import cv2

def encrypt_image(image_path):
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    image_bytes = img.tobytes()

    key = np.random.randint(0, 256, len(image_bytes), dtype=np.uint8)
    key = key.reshape((height, width, 3))

    encrypted_data = np.bitwise_xor(np.frombuffer(image_bytes, dtype=np.uint8), key.flatten())
    encrypted_img = encrypted_data.reshape((height, width, 3))

    cv2.imwrite("terenkripsi_ikan.jpeg", encrypted_img)

    print("Gambar berhasil dienkripsi.")
    return encrypted_data, key

def decrypt_image(encrypted_data, key, height, width):
    decrypted_data = np.bitwise_xor(encrypted_data, key.flatten())
    decrypted_img = decrypted_data.reshape((height, width, 3))

    cv2.imwrite("terdekripsi_ikan.jpeg", decrypted_img)

    print("Gambar berhasil didekripsi.")
    return decrypted_data

if __name__ == "__main__":
    image_path = "D:\SEMESTER 3 D-3 TEKNIK INFORMATIKA UNS\Sistem Keamanan Data\RSA Gambar\ikan.jpeg"

    encrypted_data, key = encrypt_image(image_path)

    img_dimensions = cv2.imread(image_path).shape[:2]
    decrypted_data = decrypt_image(encrypted_data, key, *img_dimensions)
