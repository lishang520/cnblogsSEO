一、意义：让百度收录我们的博客园文章
博客园的文章不会被百度自动收录，因为我们的的链接是https://www.cnblogs.com/painter-sec 这种格式的，百度只会收录子域名，所以我们可以将我们的博客园地址改为：https://painter-sec.cnblogs.com ，然后将我们的博客文章的文章链接也转换成这种格式，发表到CSDN或其他平台上，这样我们的文章就可以被收录了

二、检查我们的文章是否被收录
百度中输入： site:www.cnblogs.com inurl:painter-sec
谷歌中 输入： site:www.cnblogs.com inurl:painter-sec

三、解决方法
将我们的博客园的文章的地址转换格式后，全部发表到该文章页面，可以手工，也可以自己写python脚本自动化执行。下面的url都是由python脚本自动化添加。

四、脚本使用教程
1、修改config.py 文件，修改为自己的
