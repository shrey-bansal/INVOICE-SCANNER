from veryfi import Client
import argparse
parse = argparse.ArgumentParser()
parse.add_argument('--filename', type=str, default='test')
args = parse.parse_args()

client_id = 'vrfBgla0hBlmrWbJ0MFmA1ZV58tL4Sr74uytgdj'
client_secret = 'gvEfnhDhxe8vgPkUoBMgVJRaEXTeBUIDHr5Ctwz9YhVb7RGwBo2vsbtIl6CzByKVfgUcIk01B8uV43kMrzf07E2djtD0YwIsNIMIr3wlbmbrEBSiJeirvsIlXwLvmnk5'
username = 'chat2shrey'
api_key = 'e7bd34c21945521e13d2806c1c3dc702'
# categories = ['Grocery', 'Utilities', 'Travel']
file_path = 'upload/'
file_path += args.filename

veryfi_client = Client(client_id, client_secret, username, api_key)
response = veryfi_client.process_document(file_path)
# print(response)
f = open("results.txt","w")
for i in response:
	answer = str(i) + "->" + str(response[i]) + "\n"
	f.write(answer)
f.close()