import os
hostname = "10.10.21.9" #example
response = os.system("ping -n 1 " + hostname)
print(response)
#and then check the response...
if response == 0:
  print(f"{hostname} is up!")
else:
  print(f"{hostname} is down!")