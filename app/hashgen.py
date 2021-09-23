import hashlib


class Hash_Genrator:

    def __init__(self,str_input):
        self.hash_str = str_input 
    def md5(self):
        return hashlib.md5(self.hash_str.encode('utf-8')).hexdigest()
    def sha1(self):
        return hashlib.sha1(self.hash_str.encode('utf-8')).hexdigest()
    def sha224(self):
        return hashlib.sha224(self.hash_str.encode('utf-8')).hexdigest()
    def sha256(self):
        return hashlib.sha256(self.hash_str.encode('utf-8')).hexdigest()
    def sha384(self):
        return hashlib.sha384(self.hash_str.encode('utf-8')).hexdigest()
    def sha512(self):
        return hashlib.sha512(self.hash_str.encode('utf-8')).hexdigest()
    def blake2b(self):
        return hashlib.blake2b(self.hash_str.encode('utf-8')).hexdigest()
    def blake2s(self):
        return hashlib.blake2s(self.hash_str.encode('utf-8')).hexdigest()


