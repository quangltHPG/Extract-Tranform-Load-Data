from datetime import datetime
start = datetime.now()
a = 0
for i in range(1000000000):
    a = a + i
print (datetime.now() - start)