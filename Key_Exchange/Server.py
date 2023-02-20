import socket
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def receiveKey(): #Returns x -> Initial Conditions, r -> rate control parameter

    # Generate RSA key pair
    key = RSA.generate(2048)
    # Create a cipher object using the private key
    cipher = PKCS1_OAEP.new(key)
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get the local machine name
    host = socket.gethostname()
    # Reserve a port for your service
    port = 9999
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    # Listen for incoming connections
    server_socket.listen(1)
    print('Server is listening on {}:{}'.format(host, port))
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)
    # Send the public key to the client
    public_key = key.publickey().export_key()
    client_socket.send(public_key)
    # Receive the encrypted message from the client
    encrypted_message = client_socket.recv(1024)
    # Decrypt the message using the private key
    x = cipher.decrypt(encrypted_message)
    # Convert the decrypted message from bytes to decimal
    x_decimal_value = float(x.decode())
    
    encrypted_message = client_socket.recv(1024)
    # Decrypt the message using the private key
    r = cipher.decrypt(encrypted_message)
    # Convert the decrypted message from bytes to decimal
    r_decimal_value = float(r.decode())

    # Close the connection
    client_socket.close()

    return x_decimal_value, r_decimal_value

x, r = receiveKey()
print('Received x = ', x, '& r = ', r)