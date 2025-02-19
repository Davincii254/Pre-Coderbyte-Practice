def StringChanges(strParam):
    result = []
    i = 0
    while i < len(strParam):
         if strParam[i] == 'M':
            if result:
               result.append(result[-1])
         elif strParam[i] == 'N':
            i += 1
         else:
            result.append(strParam[i])
         i += 1
    strParam = ''.join(result)
    return strParam

# keep this function call here 
print(StringChanges(input()))