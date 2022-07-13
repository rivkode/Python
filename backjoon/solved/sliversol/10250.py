num = int(input())
i = 0
while i < num:
    h, w, n = map(int, input().split())
    f = 0
    ho = 0
    if n%h == 0:
        f = h*100
        ho = n//h
    else:
        f = n%h*100 # 층수
        ho = n//h +1 #호수

    # print("{}{}".format(f,ho))
    print(f+ho)
    i += 1