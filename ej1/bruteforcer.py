import hashlib 
import json
import subprocess

address = 0x0804866c
digest = "d740a5dc607f78fbffe520efc7caebd2137940ddb26c30c2fd37ed743b77038d326a9c7e7e80"
counter = 0
while address < 0xFFFFFFFF:
  counter += 1
  out = subprocess.Popen(['./random', str(address)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  stdout,stderr = out.communicate()
  randoms = json.loads(stdout)
  rdo = ""
  for i in range(len(randoms)):
    digChar = int(digest[i*2:i*2+1], 16)
    tmp = digChar ^ randoms[i]
    rdo += chr(tmp)
    print(rdo)
  try:
    rdo = rdo.encode('ascii')
    print(rdo)
    if hashlib.md5(bytes(rdo)) == "080d5caaed95af9ab072c41de3a73c24":
      print(f"El secreto es {rdo}")
  except:
    pass
  address += 0x1000
  if counter % 100 == 0:
    print(counter)
