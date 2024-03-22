import socket
import os
import time

# Server IP address (change to match server IP)
SERVER_ADDRESS = ("localhost", 5000)

# Folder to save received images
SAVE_FOLDER = "received_images"

# Function to receive and save file
def receive_file(sock, filename):
  # Create a filename with numbering for duplicates
  i = 1
  while os.path.exists(os.path.join(SAVE_FOLDER, filename)):
    filename = f"{filename[:-4]}_{i}.png"
    i += 1

  filepath = os.path.join(SAVE_FOLDER, filename)
  
  # Create the folder if it doesn't exist
  os.makedirs(SAVE_FOLDER, exist_ok=True)

  # Open the file in binary write mode
  with open(filepath, "wb") as f:
    data = sock.recv(1024)
    while data:
      f.write(data)
      data = sock.recv(1024)

def main():
  # Create a TCP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


  # Connect to the server
  sock.connect(SERVER_ADDRESS)

  print("Connected to server!")

  while True:
    # Receive the image file
    receive_file(sock, "reese.png")
    print("Image received and saved!")
    time.sleep(4)

if __name__ == "__main__":
  main()