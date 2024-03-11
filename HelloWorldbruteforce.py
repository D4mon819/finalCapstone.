import time

message = "Hello World"
alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(message)):
    for j in range(len(alphabet)):
        current_message = message[:i] + alphabet[j]
        if message[i] == alphabet[j]:
            print(current_message)
            break
        print(current_message)
        time.sleep(0.05)