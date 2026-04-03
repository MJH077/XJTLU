"""
HTML:定义网页的结构和信息
CSS：定义网页的样式
JavaScript：定义用户和网页的交互逻辑

<html>: 没有斜杠开头的是起始标签，表示开始
</html>: 有斜杠开头的是闭合标签，表示结束
这两者可以被看做一个HTML元素，<html>标签是HTML文档的根，所有的其他元素都要被放到这个元素里面，也就是起始标签和闭合标签之间

<!DOCTYPE HTML>
<html>
    <body>
        <h1> 标题 </h1>
        <p> 文字 </p>
    </body>
</html>
h1 和 p 都是body元素的子元素，而且处于同一层级所以互为兄弟元素

浏览器点击右键，选择“显示网页源代码”，就可以看到当前网页的HTML源代码是什么样的
"""

"""
1. 标题文本被起始标签和闭合标签包围，数字越小表示标题层级越大
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>

2. 文本是p，不同的p之间会默认进行换行以表示不同段落。
   如果手动在起始和闭合标签之间换行，并不会显示而是多了一个空格
   如果嫌麻烦的话可以在想换行的地方插入<br>进行换行
<p></p>
<p></p>

3. 用b来包围文本进行加粗
<p>xxx<b>xx</b>xxx</p>

4. 用i来包围文本进行斜体处理
<p>xxx<i>xx</i>xxx</p>

5. 用u来包围文本进行下划线处理
<p>xxx<u>xx</u>xxx</p>

6. 用<img>来加入图片（src是source，值可以是图片的链接也可以是路径）
<img src="http://movie.oduban.com/top250">

7. 链接（在起始和闭合标签之间放上链接对应的文字，hrf的值就是目标要跳转的URL地址）
<a href="http://movie.douban.com/top250">我的主页</a>

8. <ol>表示有序列表,即ordered list；里面的元素要用<li>标签，即list item；无序列表用<ul>标签，即unordered list
<ol>
  <li>语文</li>
  <li>数学</li>
</ol>
<ul>
  <li>语文</li>
  <li>数学</li>
</ul>

9. 表格
<table>用来定义表格的标签，里面一般会嵌套一些和表格相关的元素
<thead>表示表格的头部，一般是指表格得第一行（table head）
<tbody>表示表格的主体（table body）
<tr>表示表格行，一般放在<thead><tbody>中（table row）
<td>表示单元格，代表着一项一项的数据（table data）
<table>
    <thead>
        <tr>
           <td> 表头1 </td>
           <td> 表头2 </td>
        </tr>
    </thead>
    <tbody>
        <tr>
           <td> 数据1 </td>
           <td> 数据2 </td>
        </tr>
        <tr>
           <td> 数据3 </td>
           <td> 数据4 </td>
        </tr>
    </tbody>
</table>
网页样式：
表头1表头2
数据1数据2
数据3数据4
"""

"""
<!DOCTYPE html>
<html>
    <head>
        <title>标题</title>
    </head>
    <body>
        <div style="background-color:azure;">
            <h1>山丘</h1>
            <h2><span style="background-color:beige;">李宗盛</span></h2>
            <p>想说却还没说的</p>
            <p>还很多</p>
            <p>攒着是因为<br>想写成歌</p>
            <p>让人<b>轻轻地</b>唱着，<i>淡淡地</i>记着 </p>
            <p>就算<u>终于</u>忘了</p>
            <p>也值了</p>
        </div>
        <img src=https://pic.sogou.com/d?query=%E6%9D%8E%E5%AE%97%E7%9B%9B%E5%9B%BE%E7%89%87&st=255&from=vr&did=2&phu=http%3A%2F%2Fp0.ifengimg.com%2Fpmop%2F2017%2F0822%2F106081F6BF349438CB6D402BBADE351632AF4DBE_size91_w1280_h848.jpeg&rawQuery=%E6%9D%8E%E5%AE%97%E7%9B%9B%E5%9B%BE%E7%89%87&vrExpId=&vrAdParams= width="500px">
        <a href="http://www.baidu.com" target="_blank">百度链接</a>
    </body>
</html>
"""

