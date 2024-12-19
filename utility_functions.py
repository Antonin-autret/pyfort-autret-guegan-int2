def key2(n):
    line=["   @@@@%           ","  @     @@@@@@@@@@@","  @      @    @@ @ ","   @@@@%           "]
    for i in range(4):
        for j in range(n):
            print(line[i],end='')
        print('')