def sockMerchant(n, ar):
  #dic to store n socks, at the end there'll be left only odd socks
  rout={}
  #var to store num of pair found on array
  num=0
  #iterate through array
  for i in range(n):
  #compare if element is in "Rout"
      if ar[i] in rout:
      #if number is in Rout, pop it and count+1
          rout.pop(ar[i]) 
          #if exists in Rout then current element+existing is?= the pair
          num+=1
      else:
          #insert current element in Rout
          rout[ar[i]]=1
  #print(num) #verification purposes
  return num
