import base64


def to_picture(img_encoded, full_path_file_name):
    content_decoded = base64.decodestring(
        img_encoded)  # Just pass over the method the bytes array resulting of reading the file

    foo = open(full_path_file_name, 'wb')
    foo.write(content_decoded)  # And write the decoded content to a file with a picture extension

    # TODO: Check extension in json file for correct saving.
    foo.close()
