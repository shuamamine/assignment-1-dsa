def shighest(a):
   fhighest = a[0]
   s_highest = a[0]
   for num in a[1:]:
       if num > fhighest:
          s_highest = fhighest
          fhighest = num
       elif num > s_highest and num!=fhighest:
            s_highest = num
   return s_highest
