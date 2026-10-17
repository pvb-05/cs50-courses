# submit50 cs50/problems/2022/python/extensions
str = input('File name: ').lower().strip()

if str[-4:] == '.gif':
    print('image/gif')
elif str[-4:] == '.jpg':
    print('image/jpeg')
elif str[-5:] == '.jpeg':
    print('image/jpeg')
elif str[-4:] == '.png':
    print('image/png')
elif str[-4:] == '.pdf':
    print('application/pdf')
elif str[-4:] == '.txt':
    print('text/plain')
elif str[-4:] == '.zip':
    print('application/zip')
else:
    print('application/octet-stream')
