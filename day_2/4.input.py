가격 = float(input('가격?'))
부가가치세율 = 0.1
부가가치세 = 가격*부가가치세율
print(부가가치세)
열린파일 = open("results.txt", 'a')
열린파일.write(str(부가가치세)+'\n')
열린파일.close()