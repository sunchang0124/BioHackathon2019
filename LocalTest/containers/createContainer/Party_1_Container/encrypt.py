import time
start_time = time.time()

import requests
import json

####################################
# encryption part
####################################
from PQencryption.pub_key.pk_signature.quantum_vulnerable import signing_Curve25519_PyNaCl
from PQencryption.pub_key.pk_encryption.quantum_vulnerable import encryption_Curve25519_PyNaCl
from PQencryption.symmetric_encryption import salsa20_256_PyNaCl
from PQencryption import utilities
import nacl.encoding
import base64


#create signing key
signing_key, verify_key = signing_Curve25519_PyNaCl.key_gen()

verifyBase64 = verify_key.encode(encoder=nacl.encoding.Base64Encoder)

#create symmetrical encryption key
encryption_key = salsa20_256_PyNaCl.key_gen()
encryptionKeyBase64 = base64.b64encode(encryption_key)

#read file
with open('input.json', 'r') as f:
    input = json.load(f)
fileStr = input['party_name']

myStr = open("/data/encrypted_%s.csv" %(fileStr), 'rb').read()

#sign->encrypt->sign procedure
signed_encrypted_signed_message = utilities.sign_encrypt_sign(myStr, signing_key, encryption_key)

#save encrypted file temporarily
text_file = open("/data/%s.enc" %(fileStr), "wb")
text_file.write(signed_encrypted_signed_message)
text_file.close()

#########################################################
# data sending
#########################################################

# requests.get(url='http://dockerhost:5001')
### send file to TTP service
res = requests.post(url='http://dockerhost:5001/addFile',
    files={"fileObj": open('/data/%s.enc' %(fileStr), 'rb')})

#get the uuid of the stored file at TTP
resultJson = json.loads(res.text.encode("utf-8"))

#print output
print("Stored encrypted file as %s" % (resultJson["status"]))
print("UUID: %s" % resultJson["uuid"])

result = {
    "%sfileUUID" %(fileStr): resultJson["uuid"],
    "%sencryptKey" %(fileStr): encryptionKeyBase64.decode('ascii'),
    "%sverifyKey" %(fileStr): verifyBase64.decode('ascii')
}


with open('encryption/%s_keys.json' %(fileStr), 'w') as fp:
    json.dump(result, fp)

print("My encryption program took", time.time() - start_time, "to run")