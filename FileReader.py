from os.path import isfile

file_path = 'housing.data'

if isfile(file_path):

    # To read a file using python we'll use the method `open`
    my_file = open(file_path)

    for line in my_file.readlines():
        # Strip will remove any `extra` characters that might be misinterpreted when reading a string
        stripped_line = line.strip()
        #print(stripped_line)
        print(list(stripped_line.split(" ")))

    # It's important to close files after they've been used to avoid a `resources leak` on the os
    my_file.close()

else:
    print('Please provide a valid file!')


