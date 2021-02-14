#!/bin/env python3
ftp = 290
start = ftp * .8
ramp = ftp * .1 
target = start
print("Int. Target Est'd FTP")
for interval in range(0,9):
  interval_num = interval + 1
  print(f"  {interval_num:>2} {target:>5.2f} {ftp:>9.2f}")
  target = target + ramp
  ftp = target * .75

