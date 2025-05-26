# items1 = [35, 12, 99, 68, 55, 35, 87]
# items2 = ['Python', 'Java', 'Go', 'Kotlin']
# items3 = [100, 12.3, 'Python', True]
# print(items1)  # [35, 12, 99, 68, 55, 35, 87]
# print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
# print(items3)  # [100, 12.3, 'Python', True]


# items4 = list(range(1, 10))
# items5 = list('hello')
# print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(items5)  # ['h', 'e', 'l', 'l', 'o']
#
#
# 列表的运算
# 我们可以使用运算符实现两个列表的拼接，拼接运算会将两个列表中的元素连接起来放到一个列表中，代码如下所示。+
#
# items5 = [35, 12, 99, 45, 66]
# items6 = [45, 58, 29]
# items7 = ['Python', 'Java', 'JavaScript']
# print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
# print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
# items5 += items6
# print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]


# 我们可以使用运算符实现列表的重复运算，运算符会将列表元素重复指定的次数，我们在上面的代码中增加两行，如下所示。**
# print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
# print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']
# 我们可以使用或运算符判断一个元素在不在列表中，我们在上面的代码代码中再增加两行，如下所示。innot in
# print(29 in items6)  # True
# print(99 in items6)  # False
# print('C++' not in items7)     # True
# print('Python' not in items7)  # False

# 由于列表中有多个元素，而且元素是按照特定顺序放在列表中的，所以当我们想操作列表中的某个元素时，可以使用[]运算符，通过在[]中指定元素的位置来访问该元素，这种运算称为索引运算。需要说明的是，[]的元素位置可以是0到N - 1的整数，也可以是-1到-N的整数，分别称为正向索引和反向索引，其中N代表列表元素的个数。对于正向索引，[0]可以访问列表中的第一个元素，[N - 1]可以访问最后一个元素；对于反向索引，[-1]可以访问列表中的最后一个元素，[-N]可以访问第一个元素，代码如下所示。
#
# items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
# print(items8[0])   # apple
# print(items8[2])   # pitaya
# print(items8[4])   # watermelon
# items8[2] = 'durian'
# print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
# print(items8[-5])  # 'apple'
# print(items8[-4])  # 'waxberry'
# print(items8[-1])  # watermelon
# items8[-4] = 'strawberry'
# print(items8)      # ['apple', 'strawberry', '666',durian', 'peach', 'watermelon'] 666

# items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']

# #遍历
# # print(items8[0:5:2])  #  'waxberry', 'pitaya'
# languages = ['Python', 'Java', 'C++', 'Kotlin']
# for index in range(len(languages)):
#     print(languages[index])
#
# languages = ['Python', 'Java', 'C++', 'Kotlin']
# for language in languages:
#     print(language)


# 添加和删除元素
# 列表是一种可变容器，可变容器指的是我们可以向容器中添加元素、可以从容器移除元素，也可以修改现有容器中的元素。我们可以使用列表的append方法向列表中追加元素，使用insert方法向列表中插入元素。追加指的是将元素添加到列表的末尾，而插入则是在指定的位置添加新元素，大家可以看看下面的代码。

# languages = ['Python', 'Java', 'C++']
# languages.append('JavaScript')
# print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
# languages.insert(1, 'SQL')
# print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']