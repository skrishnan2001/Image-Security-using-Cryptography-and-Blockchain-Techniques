import socket
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


# Sender's Side

def sendKey(x, r): #x -> Initial Conditions, r -> rate control parameter

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get the local machine name
    host = socket.gethostname()
    # Reserve a port for your service
    port = 9999
    # Connect to the server
    client_socket.connect((host, port))
    # Receive the public key from the server
    public_key = client_socket.recv(1024)
    # Create a cipher object using the public key
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    # Convert the decimal value to bytes and encrypt it using the public key
    message = str(x).encode()
    encrypted_message = cipher.encrypt(message)
    # Send the encrypted message to the server
    client_socket.send(encrypted_message)

    message = str(r).encode()
    encrypted_message = cipher.encrypt(message)
    # Send the encrypted message to the server
    client_socket.send(encrypted_message)
    print('Sent x = ',x, '& r = ', r)
    # Close the connection
    client_socket.close()

sendKey(0.01, 0.395) #x -> Initial Condition & r -> Rate Control Parameter


