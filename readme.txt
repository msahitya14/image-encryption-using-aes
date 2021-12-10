--Image Encryption Using AES algorithm--

1. Run main.py for executing the UI and the full application.
2. Once the UI pops up, for encryption click 'encrypt', then select the image and enter the password.
3. For decryption, select the ciphertext and enter the password and click decrypt.

The output will be generated in the same folder with the name cipher.txt for encryption

The output will be generated in the same folder with the name decryptedImage.png for decryption.


Dependencies:

Language: Python3

Libraries:
PyQt5 - for UI
PIL
pycryptodome - for AES
hashlib - sha256 hashing
base64 - encoding

A sample named 'parrot.jpg' has already been provided in the folder, with the encrypted part as 
'cipher.txt' and the 'decryptedImage.png'.