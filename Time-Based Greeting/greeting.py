import time

t = time.strftime('%H:%M:%S')
print(t)
hours = int(time.strftime('%H'))

minits = int(time.strftime('%M'))

sec = int(time.strftime('%S'))


if(hours >=0 and hours<12):
  print('Good Morning')
elif(hours >=12 and hours <18):
  print ('good afternoon')
elif(hours <=18 and hours<21):
  print ('good evening')
else:
  print('good night')
