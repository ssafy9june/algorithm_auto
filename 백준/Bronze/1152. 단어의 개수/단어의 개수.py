ipt = input()
print(ipt.rstrip(' ').lstrip(' ').count(' ')+1 if ipt!=' ' else 0)