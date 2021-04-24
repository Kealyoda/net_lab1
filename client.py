import pickle
from make_error import *
sock = socket.socket()
host_name = host_name_by_addr[2]
sock.connect((host_name[0], port))

print('connected to ', host_name[0], ':', port, 'ready to get your text with', chuck_lenght, '-length word')

data = input('enter sample: ')
encoded_data = str(encode_to_hamming(data))

encoded_with_err = encoded_data

encoded_with_err = make_error(encoded_with_err, 2)
indexes = list_different_index(encoded_data, encoded_with_err)
print('{0}'.format(indexes))
sock.send(encoded_with_err.encode())
data = pickle.loads(sock.recv(40960))
data1 = pickle.loads(sock.recv(40960))

sock.close()
right = 0
for count in range(len(encoded_data) // chuck_lenght):

    if data1[count * chuck_lenght:(count + 1) * chuck_lenght] == encoded_data[
                                                                 count * chuck_lenght:(count + 1) * chuck_lenght]:
        right += 1
if data1[len(encoded_data) // chuck_lenght - 1:len(encoded_data)] == encoded_data[
                                                                     len(encoded_data) // chuck_lenght - 1:len(
                                                                             encoded_data)]:
    right += 1
print('-----------------------------------')
print("number of corrections: ", len(data))
print("number of words ", len(encoded_data) // chuck_lenght + 1)
print("correctly delivered", right)
print("not correctly delivered", len(encoded_data) // chuck_lenght + 1 - right)
