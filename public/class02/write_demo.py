"""
write_demo.py
"""

my_l = ['hello','world','1','two','3']

with open ('/tmp/helloworld.txt','w') as fh:
    for line in my_l:
        fh.write(line+"\n")
        
