import Crypto
from Crypto.Protocol import KDF
from Crypto.Cipher import AES
from Crypto import Random
import os, struct
import base64


class AESCipher(object):


    def __init__(self, key):
        self.bs = 32
        self.chunksize = 64*1024
        self.key = key
        self.salt = '10E78E282613EFF6'
        self.session_key = KDF.PBKDF2(base64.b16decode(self.key), base64.b16decode(self.salt), 32, count=1000)
        self.iv = '26FD97984B80941BD373BACE85F68DBB'
        print("Session key: {}".format(base64.b16encode(self.session_key)))

    def encrypt(self, in_file, out_file=None):
        print("Encryption started..\n")
        if not out_file:
            out_file = in_file + '_enc' + '.txt'
        print("Output file name set")

        iv = Random.new().read(AES.block_size)
        in_file_size = os.path.getsize(in_file)
        encryptor = AES.new(self.session_key, AES.MODE_CBC, iv)
        print("IV and encryptor created")
        with open(in_file, 'rb') as fin:
            with open(out_file, 'wb') as fout:
                fout.write(struct.pack('<Q', 872))
                fout.write(iv)
                while True:
                    chunk = fin.read(self.chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)
                    fout.write(encryptor.encrypt(chunk))
        print("Enrypted file uploaded")
        return self.session_key, self.salt, iv

    def decrypt(self, in_file, out_file=None):
        print("Decryption started..\n")
        if not out_file:
            out_file = os.path.splitext(in_file)[0] + '_out.txt'

        with open(in_file, 'rb') as fin:
            decryptor = AES.new(self.session_key, AES.MODE_CBC, base64.b16decode(self.iv))
            with open(out_file, 'wb') as fout:
                while True:
                    chunk = fin.read()
                    if len(chunk) == 0:
                        break
                    fout.write(decryptor.decrypt(chunk))
        print("Decryption done!!")

if __name__ == "__main__":
    input_file = '/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/text2.txt'
    output_file = '/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/text2_enc.txt'
    output_dec_file = '/Users/vs/Documents/workspace@roy/text-editor/textEditor/text_files/text2_dec.txt'
    print(AESCipher(key = '123456').encrypt(in_file=input_file, out_file=output_file))
    AESCipher(AESCipher(key = '123456').decrypt(in_file=output_file, out_file=output_dec_file))