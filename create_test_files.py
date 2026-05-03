with open('test_valid.pdf', 'wb') as f:
    f.write(b'%%PDF-1.4\n1 0 obj\n<<>>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF')

with open('test_invalid.txt', 'w') as f:
    f.write('This is not a PDF')

with open('test_large.pdf', 'wb') as f:
    f.seek(11 * 1024 * 1024)
    f.write(b'%%PDF-1.4\n1 0 obj\n<<>>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF')
