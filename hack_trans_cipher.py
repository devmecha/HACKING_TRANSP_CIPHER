import math
import re
import dec_transposition_cipher

def hackTransp (msg):
	l = len(msg)
	for k in range(1, l):
		dec_Text = dec_transposition_cipher.trans_cipher_dec(msg, k)
		print("--- KEY : %s ==> Possible Original Message : %s ---" %(k, dec_Text+'|'))
	return dec_Text

def Main():
	print("****** HACKING THE TRANSPOSITION CIPHER *******")
	msg = input('Please Enter your Message  :')
	print('\n')
	print('the message is : ', msg)
	print('\n')
	print('Hacking now ...' )
	hackTransp(msg)
	# print("Warning ! The '|' at the end is not included")
	# print("Decrypted msg is : %s " %(res+'|'))


if __name__ == '__main__':
 	Main()