#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PyPDF2 import PdfWriter, PdfReader

# buat objek pdf writer
out = PdfWriter()

# buka file pdf asli
file_path = r"D:\SEMESTER 3 D-3 TEKNIK INFORMATIKA UNS\Sistem Keamanan Data\RSA File\Jurnal.pdf"
file = PdfReader(file_path)

# identifikasi total halaman file
num = len(file.pages)

# program membaca setiap halaman file sesuai halaman yang diidentifikasi
for idx in range(num):
    # dapatkan halaman
    page = file.pages[idx]

    # tambahkan halaman ke objek PdfWriter
    out.add_page(page)

# masukkan password enkripsi (gunakan parameter user dan owner)
password = "123456"
out.encrypt(password, use_128bit=True)

# buat nama file output (file enkripsi)
output_path = r"D:\SEMESTER 3 D-3 TEKNIK INFORMATIKA UNS\Sistem Keamanan Data\RSA File\Jurnal.pdf"

# buka file enkripsi untuk ditulis (mode "wb")
with open(output_path, "wb") as f:
    # simpan objek PdfWriter yang berisi halaman-halaman terenkripsi ke file
    out.write(f)

# tambahkan pesan sukses
print(f"File {file_path} file berhasil dienkripsi {output_path}")


# In[ ]:



