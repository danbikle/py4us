# fnc_demo.py

my_l = [0,1,2,3,4]

def my_f(ur_l):
  for row in ur_l:
      yield row

for arow in my_f(my_l):
    print(arow)
    
