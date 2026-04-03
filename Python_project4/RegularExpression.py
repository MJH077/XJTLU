"""
正则表达式：又叫做规则表达式，是使用单个字符串来描述、匹配某个句法规则的字符串，常用来被检索、替换那些符合某个模式（规则）的文本
如果不使用正则，使用if else来对字符串做判断就很困难了
使用re模块，并基于该模块中的三个基础方法来做正则匹配：match、search、findall
1. re.match(匹配规则，被匹配字符串)
   从被匹配字符串开头进行匹配，匹配成功返回匹配对象（包含匹配的信息），匹配不成功返回空
2. re.search(匹配规则，被匹配字符串)
   搜索整个字符串，找出匹配的。从前向后，找到第一个后就停止，不会继续向后
3. re.findall(匹配规则，被匹配字符串)
   匹配整个字符串，找出全部匹配项
"""
import re
s = "python java python"
result = re.match("python", s)
print(result)
print(result.span())
print(result.group())
# 如果开头为不是“python”，则剩下的字符串都不会去检测了，输出为None
s1 = "python6666python"
result1 = re.search("python", s1)
print(result1)
print(result1.span())
print(result1.group())
s2 = "java python python"
result2 = re.findall("python", s2)
print(result2)
# 找不到则返回空列表list：[]

r"""
元字符匹配（单字符匹配）：
. 匹配任意一个字符（除了\n），\.匹配的是点本身
[] 匹配[]中列举的字符
\d 匹配数字，即0-9
\D 匹配非数字
\s 匹配空白，即空格、tab键
\S 匹配非空白
\w 匹配单词字符，即a-z、A-Z、0-9、_
\W 匹配非单词字符
"""
a = "javapython @##9000:77uuiiio"
result3 = re.findall(r'\d', a)  # 字符串前带r的标记意思是字符串内转义字符无效，就是普通字符的意思
print(result3)
result4 = re.findall(r'\w', a)
print(result4)
result5 = re.findall(r'[5-9]', a)
print(result5)

r"""
元字符匹配（数量匹配）：
* 匹配前一个规则的字符出现至少0到无数次
+ 匹配前一个规则的字符出现1到无数次
? 匹配前一个规则的字符出现0或者1次
{m} 匹配前一个规则的字符出现m次
{m,} 匹配前一个规则的字符出现最少m次
{m, n} 匹配前一个规则的字符出现m到n次

边界匹配：
^ 匹配字符串开头
$ 匹配字符串结尾
\b 匹配一个单词的边界
\B 匹配非单词边界

分组匹配：
| 匹配左右任意一个表达式
() 将括号中的字符作为一个分组
"""
# 匹配账号，只能有数字与字母组成，长度为6-10位
r = '^[0-9a-zA-Z]{6,10}$'  # 注意：正则里面不要轻易写空格
s = '12345678'
print(re.findall(r, s))
# 匹配QQ号，要求纯数字，长度5-11位，第一位不为0
r1 = '^[1-9][0-9]{4,10}$'
s1 = '12345678'
print(re.findall(r1, s1))
# 匹配邮箱地址，只允许QQ、163、gmail三种邮箱地址
r2 = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s2 = 'abc.efg.dow@qq.com'
s3 = '1234567.dow@gmial.cn'
print(re.match(r2, s2))
print(re.match(r2, s3))


