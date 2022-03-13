## 一、意义：让百度收录我们的博客园文章
博客园的文章不会被百度自动收录，因为我们的的链接是https://www.cnblogs.com/painter-sec 这种格式的，百度只会收录子域名，所以我们可以将我们的博客园地址改为：https://painter-sec.cnblogs.com ，然后将我们的博客文章的文章链接也转换成这种格式，发表到CSDN或其他平台上，这样我们的文章就可以被收录了

## 二、检查我们的文章是否被收录
百度中输入： site:www.cnblogs.com inurl:painter-sec
谷歌中 输入： site:www.cnblogs.com inurl:painter-sec

## 三、解决方法
将我们的博客园的文章的地址转换格式后，全部发表到该文章页面，可以手工，也可以自己写python脚本自动化执行。
## 四、脚本实现思路
### 1、爬虫获取博客园的所有文章
### 2、爬虫获取csdn的专门seo的文章
### 3、对博客园的文章和csdn的文章进行比对，对于csdn中没有的url添加到列表
### 4、手工登录csdn
### 5、获取csdn的cookie，存储到本地，后续直接用cookie自动登录
### 6、登录csdn后，使用selenium模拟修改文章

## 五、脚本使用方法
### 0、前提：本脚本用到了selenium，所以需要下载对应的浏览器驱动，我这里用的是谷歌浏览器，所以需要下载对应的谷歌浏览器驱动(驱动版本和浏览器版本一致)，然后将驱动放到python的script目录下即可，驱动下载地址：http://chromedriver.storage.googleapis.com/index.html
### 1、打开config.py 文件，修改里面对应自己的url
  博客园的主页地址示例：https://www.cnblogs.com/painter-sec/
  csdn_article  的url如图片
![](https://img2022.cnblogs.com/blog/2349369/202203/2349369-20220313121754857-124661289.png)
 
  csdn_edit_url   的url如图片
  ![](https://img2022.cnblogs.com/blog/2349369/202203/2349369-20220313122233081-759851686.png)

  csdn_manage_url 的url如图片
![](https://img2022.cnblogs.com/blog/2349369/202203/2349369-20220313122351090-1884697871.png)

### 2、在当前脚本目录下执行：python3 博客园文章收录.py 
  提示：第一次需要手工登录CSDN，登录完成后，在执行命令的窗口按下回车，即可成功获取cookie，有了cookie，下次就不用手工登录了
### 3、脚本运行示例：
![](https://img2022.cnblogs.com/blog/2349369/202203/2349369-20220313123043440-2032462168.png)
4、实际效果：
![](https://img2022.cnblogs.com/blog/2349369/202203/2349369-20220313123401764-1681195492.png)

## 六、脚本下载地址
https://github.com/lishang520/cnblogsSEO



  
