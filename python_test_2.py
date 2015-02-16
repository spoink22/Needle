import sys, zipfile

#Later in the code I have the program printing out a file size. At first it was in bytes, but I thought that looked ugly, so this shows the bytes in KB, MB, etc.
def humanReadable(num):
    #return str(num)
    for unit in [' bytes','KB','MB','GB','TB']:
        if abs(num) < 1000.0:
            return "%.1f%s" % (num, unit)
        num /= 1000.0
    return "%d%s" % (num, unit)

filename = sys.argv[1]
#test to make sure it's a real zip file
if not zipfile.is_zipfile(filename):
    print "Supplied file is not a .zip file, or is not found!"
    exit()
zipFile = zipfile.ZipFile(filename)
for item in zipFile.infolist():
    #The instructions said to print the file names and sizes, but it didn't say which size (compressed/uncompressed). I went with compressed as that is the size they are currently taking up.
    print item.filename + "\t" + str(humanReadable(item.compress_size))
