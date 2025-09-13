from ftplib import *

ftp = FTP("test.rebex.net")
print(ftp.getwelcome())

ftp.quit() 
