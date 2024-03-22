import socket
import time
import os

# Server IP address (change to your server IP if needed)
SERVER_ADDRESS = ("localhost", 5000)

# Folder containing the image file
IMAGE_FOLDER = "images"
IMAGE_NAME = "reese.png"

# Function to send file data
def send_file(sock, filename):
  filepath = os.path.join(IMAGE_FOLDER, filename)
  if not os.path.exists(filepath):
    print(f"Error: File {filename} not found in {IMAGE_FOLDER}")
    return
  
  # Open the file in binary mode
  with open(filepath, "rb") as f:
    data = f.read()
  sock.sendall(data)

def main():
  # Create a TCP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Bind the socket to the server address
  sock.bind(SERVER_ADDRESS)

  # Listen for incoming connections
  sock.listen(1)
  print("Server listening on port:", SERVER_ADDRESS[1])

  while True:
    # Accept da connection
    conn, addr = sock.accept()
    print("Connected by", addr)

    # Send the reese every 5 seconds
    num = 1
    while True:
      send_file(conn, IMAGE_NAME)
      print("Sent da reese ",num)
      num += 1
      time.sleep(5)
  

if __name__ == "__main__":
  main()