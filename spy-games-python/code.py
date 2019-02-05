# --------------
##File path for the file 
file_path 


#Code starts here
def read_file(path):
    file = open(file_path, mode='r')
    sentence = file.readline()
    file.close()
    return sentence


sample_message = read_file(file_path)
print(sample_message)


# --------------
#Code starts here
file1 = open(file_path_1, mode='r')
message_1 = file1.readline()
file1.close()

file2 = open(file_path_2, mode='r')
message_2 = file2.readline()
file2.close()

def fuse_msg(message_a, message_b):
    quotient = int(message_b) // int(message_a)
    return str(quotient)

secret_msg_1 = fuse_msg(message_1,message_2)
print(secret_msg_1)


# --------------
#Code starts here
file = open(file_path_3, mode='r')
message_3 = file.read()
print(message_3)

def substitute_msg(message_c):
    sub = ''
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    
    return sub

secret_msg_2 = substitute_msg(message_3)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
file4 = open(file_path_4, mode='r')
message_4 = file4.read()
file4.close()

file5 = open(file_path_5, mode='r')
message_5 = file5.read()
file5.close()

print(message_4)
print(message_5)

def compare_msg(message_d, message_e):
    a_list = message_d.split()
    b_list = message_e.split()

    c_list = [i for i in a_list if i not in b_list]
    final_msg = " ".join(c_list)
    return final_msg

secret_msg_3 = compare_msg(message_4, message_5)





# --------------
#Code starts here
file6 = open(file_path_6, mode='r')
message_6 = file6.read()
print(message_6)

def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x : len(x)%2==0
    b_list = list(filter(even_word, a_list))
    final_msg = " ".join(b_list)
    return final_msg

secret_msg_4 = extract_msg(message_6)



# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg = " ".join(message_parts)

def write_file(secret_msg, path):
    file = open(path, mode='a+')
    file.write(secret_msg)
    file.close()

f = write_file(secret_msg, final_path)
print(f)


