"""
<!DOCTYPE html>
<!感叹号回车自动弹出HTML基本框架，上行为文档类型声明>
<html>
    <head>
        <meta charset="UTF-8">
        <!UTF-8是一种编译语言>
        <title>我的网页</title>
    </head>
    <body>
        <h1 align="center">我的缪斯</h1>
        <h2 align="left">蓄势待发</h2>
        <h3>理想未眠</h3>
        <!align表示为对齐，有左中右三种情况，默认情况下为靠左对齐>
        <h4></h4>
        <h5></h5>
        <h6></h6>
        <!h表示标题标签，只有1-6级标签，字体随层级增大而减小，但是字体大小与层级无关。快速生成的方法：h$*3（生成三个标题标签）>
        <p>当世界嘈杂到没有分贝能够逃出</p>
        <p>当宇宙安静至没有尘埃再次飘扬<br>一切也并不会因此而改变</p>
        <!p表示段落标签，换行可以另开p标签，也可以插入br标签>
        <hr color="black" width="1000px" size="10px">
        <hr color="gold" width="500px" size="50px" align="left">
        <hr color="silver" width="500px" size="50px" align="right">
        <!hr表示水平分割线，默认情况下居中对齐，width表示横宽，size表示纵长>
        <img src="picture/微信图片_20221110215612.jpg" alt="图片无法显示" width="400px" height="300px" title="小白">
        <img src="C:\Users\ASUS\Pictures\Saved Pictures\微信图片_20230414220518.jpg" width="300px" height="300px" title="小马">
        <!img表示图像，src放入绝对路径或相对路径的地址，alt即当照片无法加载出来时显示的内容，title表示当鼠标悬停在图片上时出现的内容>
         <br><a href="http://sso.xjtlu.edu.cn">XJTLU</a>
        <br><a href="http://sso.xjtlu.edu.cn">
            <img src="picture/屏幕截图 2024-04-25 223325.png" width="200px" height="200px">
        </a>
        <!a表示超链接，href代表网址，可以选择点击文字或者图片进入网站>
        <br><em>理想三旬</em>
        <b>行歌</b>
        <i>生活何处</i>
        <strong>步履不停</strong>
        <del>火烧云</del>
        <span>年少模样</span>
        <!em表示定义着重文字，b表示定义粗体文字，i表示定义斜体文字，strong表示定义加重语气，del表示定义删除字，span表示元素没有特定的含义>
        <ol>
            <li>first</li>
            <li>second</li>
        </ol>
        <ol type="1">
            <li>first</li>
            <li>second</li>
        </ol>
        <ol type="a">
            <li>first</li>
            <li>second</li>
        </ol>
        <ol type="A">
            <li>first</li>
            <li>second</li>
        </ol>
        <ol type="I">
            <li>first</li>
            <li>second</li>
        </ol>
        <ol type="i">
            <li>first
                <ol>
                    <li>1-1</li>
                    <li>1-2</li>
                </ol>
            </li>
            <li>second
                <ol>
                    <li>2-1</li>
                    <li>2-2</li>
                </ol>
            </li>
        </ol>
        <!ol表示有序列表order list，li大小写字母，大小罗马字母，数字五种排序编号，默认为数字。列表中可以进行嵌套。快速生成列表：ol乘n大于li乘n（生成n个各个内含n项的有序列表）>
        <ul>
            <li>abc</li>
            <li>ABC</li>
        </ul>
        <ul type="disc">
            <li>abc</li>
            <li>ABC</li>
        </ul>
        <ul type="circle">
            <li>abc</li>
            <li>ABC</li>
        </ul>
        <ul type="square">
            <li>abc</li>
            <li>ABC</li>
        </ul>
        <ul type="none">
            <li>abc</li>
            <li>ABC</li>
        </ul>
        <ul>
            <li>abc
                <ul>
                    <li>a</li>
                    <li>b</li>
                </ul>
            </li>
            <li>ABC
                <ul>
                    <li>A</li>
                    <li>B</li>
                </ul>
            </li>
        </ul>
        <!ul代表无需标签，有disc实心圆，circle空心圆，square实心方块，none没有四种，默认为实心圆。列表中可以嵌套。>
        <table border="1"  width="200px" height="200px">
            <tr>
                <td>name</td>
                <td>sex</td>
                <td>age</td>
            </tr>
            <tr>
                <td>m</td>
                <td>f</td>
                <td>12</td>
            </tr>
            <tr>
                <td>l</td>
                <td>m</td>
                <td>20</td>
            </tr>
        </table>
        <!table代表着表格，border即加入边框，tr为行，td为每一行的数据。快速生成表格：table乘n大于tr乘n大于td乘n{n}（生成n个每个有n行每行有n个格每格数据为n的表格）>
        <table border="1" width="500px" height="500px" >
            <tr>
                <td colspan="2"></td>
                <td></td>
                <td></td>
                <td</td>
            </tr>
            <tr>
                <td></td>
                <td></td>
                <td></td>
                <td rowspan="2"></td>
            </tr>
            <tr>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </table>
        <!colspan代表向右合并单元格，rowspan代表向下合并单元格，数字是几就合并几个。原始点位不动，删掉被合并单元格的td标签即可>
        <form>
            <input type="text">
            <input type="submit">
            <input type="text">
            <button>submit</button>
        </form>
        <form>
            First name: <input type="text">
            Password: <input type="password">
            <input type="submit" value="登录">
        </form>
        <!form代表着表单，input的类型为text就是输入，submit就是提交的点击按钮，submit也可以用button标签代替。>
        <!当input的类型为password时，输入的内容不可视。而且提交按钮上的文字也可以通过value更改。>

        <! 块级元素：块元素会在页面中独占一行（自上而下垂直排列），可以设置width，height属性，一般块级元素可以包含行内元素和其他块级元素，例如div，form，h1-h6，hr，p，table，ul等>
        <! 内联元素：行内元素不会独占页面的一行，只占自身的大小，行内元素设置width，height属性无效，一般内联元素包含内联元素而不包含块级元素，例如a，b，em，span，strong等>
        <! 行内块元素：button，img，input等>
        <div>主导航：这里是图片区
            <br><img src="picture/微信图片_20221110215612.jpg" width="400px" height="300px">
        </div>
        <div>副导航：这里是文字区
           <br><span>牛奶皮肤白梦妍</span>
        </div>
        <div id="header"></div>
        <div id="nav"></div>
        <div id="article">
            <div id="section"></div>
        </div>
        <div id="silder"></div>
        <div id="footer"></div>
        <header></header>
        <nav></nav>
        <article>
            <section></section>
        </article>
        <aside></aside>
        <footer></footer>
        <! header：头部；nav：导航；section：定义文档中的节，比如章节、页眉、页脚；aside：侧边栏；footer：脚部；article：代表一个独立的、完整地相关内容块，例如一篇完整的帖子等>
    </body>
</html>
"""