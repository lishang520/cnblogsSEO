class Config():
    #这里配置你的url
    cnblogs_url="https://www.cnblogs.com/painter-sec/"    #博客园你的博客主页网址，用于爬取文章url
    csdn_article="https://blog.csdn.net/qq_22009097/article/details/123454371?spm=1001.2014.3001.5501"    #这是你的CSDN文章页面，非编辑页面，用于获取页面内容
    csdn_edit_url = "https://editor.csdn.net/md/?articleId=123454371"  #CSDN你的文章编辑页面，注意：必须要是用MD编辑器编写的文章，用于自动发文章
    csdn_manage_url ="https://mp.csdn.net/mp_blog/manage/article?spm=1010.2135.3001.5448" #CSDN个人中心页面，用于插入cookie，免登录
