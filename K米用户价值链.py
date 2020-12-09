'''
Description

K米作为中国最大的KTV聚会娱乐增值服务运营商。通过帮助KTV商家进行业务转型与升级，让KTV没有难做的生意；以乐享欢聚为主旨，提供多种娱乐形态，为消费者带来全新的聚会娱乐内容和体验。

为了更好的为商家和用户服务，K米公司经常从多种维度研究KTV商家和用户，并根据其特征推出精准的解决方案来解决商家经营和用户娱乐的痛点。

用户的研究既有通过数据智能分析实现，也有通过面对面交流、客服平台、电话沟通等进行调研。

进行用户调研时，为了得到更好的调研效果，K米客服调研团队希望K米大数据团队能为其提供用户价值比较高的用户信息以提升其调研效率和产出。

现在K米大数据团队手上有如下的一些用户及其关系信息，您能帮他们找出最大的用户调研价值链给K米客服调研团队吗？

通过构建用户画像，产生用户价值评估模型，给出了每个用户的预估调研价值。
通过分析用户是否在同场娱乐等信息，给出用户之间关系信息，调研用户A后可以再去调研用户B会产生有意义的价值。
从调研一个用户开始，如果有后续用户可调研；则可以选择他/她的后续可调研用户中的一个进行继续调研，直至所选调研用户没有后续用户可调研为止；把选择的调研用户连起来形成用户调研价值链。
一条用户调研价值链的价值是指链上所有用户预估的调研价值之和。
比如系统里有6个用户，编号从1到6的用户的预估调研价值分别为8, 14, 2, 17, 9, 26。用户后续可调研关系如下。

E62DF154-0381-4c9e-BD23-0F15AF288D9D.png

调研完1 可调研 3 和 4
调研完2 可调研3
调研完3 可调研4 和 6
调研完5 可调研6
用户调研价值链（2->3->6）的调研价值为（14+2+26=42）是能取到的最大的用户调研价值链。

★每个用户后续可调研的用户关系不多，有些甚至是空的， -_-。


Input
第一行为一个正整数 n. (1≤n≤100 000).表示K米大数据手上的用户数量；

第二行包含n个正整数分别表示第1个到第n个用户的预估调研价值；

第三行是一个正整数m(1≤m≤200 000)，表示有m个可后续调研的用户关系；

接下来m行  每行包含 两个正整数 b 和 e 表示调研完用户b后可以调研用户e(1≤b<e≤n)。


Output
输出包括两行

第一行包含一个整数；表示价值最大的用户调研价值链的价值。

第二行输出若干个用户id用"->"连起来表示价值最大的用户调研链的用户顺序（如果存在多个，取序号较小的， 比如 2->4  和 3->4 两个链都具有最大调研价值；则取  2->4）


Sample Input 1 

6
8 14 2 17 9 26
6
1 3
1 4
2 3
3 4 
3 6
5 6
Sample Output 1

42
2->3->6
'''


# values = {'1': 8, '2': 14, '3': 2, '4': 17, '5': 9, '6': 26}
# users = {'1': ['3', '4'], '2': ['3'], '3': ['4', '6'], '5': ['6']}


# def deep(node):
#     all = []
#     print('node :', node)
#     if node not in users or not users[node]:
#         return [node]
#     if len(users[node]) == 1:
#         return [node]+deep(node)
#     if len(users[node]) > 1:
#         for i in range(len(users[node])):
#             print(users[node][i])
#             tmp = deep(users[node][i])
#             tmp2 = [node]+tmp
#             all.append(tmp2)
#     print(all)


# deep('1')


# try:
#     while True:
#         n = int(input())
#         value = list(map(int, input().split()))
#         values = {}
#         for i in range(n):
#             values[str(i+1)] = value[i]
#         m = int(input())
#         users = {}
#         for _ in range(m):
#             tmp = input().split()
#             if tmp[0] not in users:
#                 users[tmp[0]] = []
#             if tmp[1] not in users[tmp[0]]:
#                 users[tmp[0]].append(tmp[1])
#         res = 0
#         print('values:',values)
#         print('users\n',users)
#         print(deep(1))
# except EOFError:
#     pass


# try:
#     while True:
#         line = input().split()
#         N, M = int(line[0]), int(line[1])
#         matches = []
#         songs = []
#         for _ in range(N):
#             matches.append(input())
#         for _ in range(M):
#             songs.append(input())
#         for i in range(len(songs)):
#             print(matcher(songs[i]))
# except EOFError:
#     pass


def matcher(song, matches):
    res = []
    for i in range(len(matches)):
        string = matches[i]
        if ismatch(song, string):
            res.append(i)
        else:
            continue
    if not res:
        return 'Not match'
    else:
        return ' '.join(res)


def ismatch(songname, matchname):
    cur1, cur2 = 0, 0
    while cur1 < len(songname) or cur2 < len(matchname):
        if songname[cur1] == matchname[cur2] or matchname[cur2] == '?':
            if cur1 < len(songname)-1:
                cur1 += 1
            if cur2 < len(matchname)-1:
                cur2 += 1
        elif matchname[cur2] == '*':
            if cur2+1<len(matchname) and matchname[cur2+1] == songname[cur1]:
                if ismatch(songname[cur1:], matchname[cur2+1:]):
                    return True
                else:
                    cur1+=1
            else:
                cur1 += 1
        elif songname[cur1] != matchname[cur2]:
            return False

print(ismatch('ktvme','ktv*'))