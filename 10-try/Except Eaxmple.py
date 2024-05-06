

text = "23"
txtfilename = 'text_file.txt'


try:
    f = open(txtfilename)
    print("your age is", str(int(text)))
except FileNotFoundError:
    print("FileName not correct")
except ValueError:
    print("text must be integer")
except Exception as e:
    print(e)
else:
    print(f.read())
finally:
    f.close()
    
    
    
#! FileNotFoundError #
#! ValueError #