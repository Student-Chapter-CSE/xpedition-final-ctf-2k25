from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load the private key from privkey.pem
with open('privkey.pem', 'rb') as key_file:
  private_key = RSA.import_key(key_file.read())

# Load the encrypted message from secret.bin
with open('secret.bin', 'rb') as encrypted_file:
  encrypted_message = encrypted_file.read()

# Decrypt the message
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(encrypted_message)

# Print the decrypted message
print(decrypted_message.decode('utf-8'))