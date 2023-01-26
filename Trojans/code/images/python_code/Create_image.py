import shutil,sys

def create_file(original,output,data: str):
    shutil.copyfile(original, output)
    with open(output,'ab') as jpg:
        byte_data = data.encode()
        jpg.write(byte_data)

def read_file_bytes(file):
    with open(file,'rb') as jpg:
        f = jpg.read()
        print(f)

def read_file(file):
    with open(file, 'rb') as jpg:
        content = jpg.read()
        offset = content.index(b'\xff\xd9')
        data = content[offset + 2:].decode()
        print(data)

if __name__=='__main__':
    if sys.argv[1] == 'read_all':
        read_file_bytes('output.jpg')
    elif sys.argv[1]== 'read_message':
        read_file('output.jpg')





        
    else:
        create_file('image.jpg', 'output.jpg', data=str(sys.argv[1]))

