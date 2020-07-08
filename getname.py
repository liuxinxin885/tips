import inspect, re
#一个变量
bianliang='你猜猜'
print(bianliang)
# print(namestr(bianliang))
# print(name)
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
print(namestr(bianliang,globals())[0],'\n',)
def varname(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      return m.group(1)
print(varname(bianliang))
