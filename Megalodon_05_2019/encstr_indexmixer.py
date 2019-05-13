def str_index_mixer(int_0):
    #num3=0 #int
    #num5=0 #int
    #num6=0 #int
    #num7=0 #int
    #num8=0 #int
    bendloop1 = False
    while not bendloop1:
        #IL_139:
        num = 365213348 #uint
        while True:
            num2 = to32(num ^ 203317953) #uint
            if (num2 % 10) == 0:
                num3 -= 831
                num3 = to32(num3)
                num = to32(num2 * 863100670 ^ 95654114)
                continue
            if (num2 % 10) == 1:            
                if True: #if (Assembly.GetExecutingAssembly() == Assembly.GetCallingAssembly())
                    num = to32(num2 * 3526061210 ^ 423182235)
                    continue
                break
            if (num2 % 10) == 2:
                num3 = 0
                num4 = 3
                num = to32(num2 * 3610101611 ^ 1048724017)
                continue
            if (num2 % 10) == 4:
                num3 >>= num4
                num3 = to32(num3)
                num = to32(num2 * 4268729055 ^ 537298066)
                continue
            if (num2 % 10) == 5:
                break
            if (num2 % 10) == 6:
                num = to32(num2 * 2312782642 ^ 849234393)
                continue
            if (num2 % 10) == 7:
                bendloop1 = True #goto IL_146
                break
            if (num2 % 10) == 8:
                num7 = 5
                num8 = 532
                num9 = 6642
                num3 = int_0
                num = to32(num2 * 3044488424 ^ 431371981)
                continue
            if (num2 % 10) == 9:
                num3 = to32(num3 - num7 + num8 - 34553)
                num3 = to32(num3 ^ num8 ^ num9)
                num = to32(num2 * 3096292149 ^ 1966593296)
                continue
            return None
    num3 = to32((num3 - num8) / num7)
    return num3



