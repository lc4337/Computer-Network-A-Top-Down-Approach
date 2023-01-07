from socket import * 
import time
from math import ceil


numPing = 10
server_addr = ("localhost", 12000)

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

received = 0
minimum = float("inf")
maximum = 0
sumRTT = 0

for i in range(numPing):
    time.sleep(0.2)
    start = time.time()
    message = "Ping " + str(i + 1) + " " + time.ctime(start)
    clientSocket.sendto(message.encode(), server_addr)
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
    except timeout:
        print("Request timed out")
        continue
    end = time.time()
    # print(modifiedMessage.decode())
    # print("RTT: " + str(end - start) + "s")
    timespan = end - start
    minimum = min(minimum, timespan)
    maximum = max(maximum, timespan)
    sumRTT += timespan * 1000
    print("Reply from " + serverAddress[0] + ": " + "bytes=" + str(len(modifiedMessage)) + " time=" + str(ceil((timespan) * 1000))+ "ms")
    received += 1
print()
print("Ping statistics for " + serverAddress[0] + ":")
print("\tPackets: Sent = " + str(numPing) + ", Received = " + str(received) + ", Lost = " + str(numPing - received) + " (" + str((numPing - received) / numPing * 100) + "% loss)")
print("Approximate round trip times in milli-seconds:")
print("\tMinimum = " + str(ceil(minimum * 1000)) + "ms, Maximum = " + str(ceil(maximum * 1000)) + "ms, Average = " + str(ceil(sumRTT / received)) + "ms")
