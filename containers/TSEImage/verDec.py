import time
start_time = time.time()

import requests
import shutil
import json

#read input file
with open('security_input.json') as data_file:    
    inputJson = json.load(data_file)
parties = inputJson['parties']

for p in parties:
    url = 'http://dockerhost:5001/file/%s' % inputJson["%sfileUUID" %(p)]
    response = requests.get(url, stream=True)
    with open('/data/%sData.enc' %(p), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

####################################
# decryption part
####################################
from PQencryption.pub_key.pk_signature.quantum_vulnerable import signing_Curve25519_PyNaCl
from PQencryption.pub_key.pk_encryption.quantum_vulnerable import encryption_Curve25519_PyNaCl
from PQencryption.symmetric_encryption import salsa20_256_PyNaCl
from PQencryption import utilities
import nacl.encoding
import base64

def verify_and_decrypt(verifyBase64, decryptKey, encFile, newFile):
    #create signing key
    verify_key = nacl.signing.VerifyKey(verifyBase64, encoder=nacl.encoding.Base64Encoder)

    #create symmetrical encryption key
    encryption_key= base64.b64decode(decryptKey)

    #read encrypted data
    myStr = open(encFile, 'rb').read()

    #verify-decrypt-verify
    verified_decrypted_verified_message = utilities.verify_decrypt_verify(myStr, verify_key, encryption_key)

    #save encrypted file temporarily
    text_file = open(newFile, "wb")
    text_file.write(verified_decrypted_verified_message)
    text_file.close()

#run decryption and verify

for p in parties:
    print('Verifying %s' %p)
    verify_and_decrypt(inputJson["%sverifyKey" %(p)], inputJson["%sencryptKey" %(p)], '/data/%sData.enc' %(p), "/data/encrypted_%s.csv" %(p) )

print("Your signiture is verified and datasets are decrypted!")
print("Verification and decryption took ", time.time() - start_time, "to run")
