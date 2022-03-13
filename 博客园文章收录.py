'''
功能：博客园seo，博客园自己的博客文章，不容易被百度收录，通过该脚本，将我们的博客园文章提取出来，然后以特定格式发表到CSDN上，使其能够收录
查看收录的文章：site:www.cnblogs.com inurl:painter-sec
实现步骤：
    1、获取博客园的所有文章链接
    2、将博客园的链接转换为超链接的格式，存储到:cnblogs_urls 中
    3、获取CSDN已经发表的文章(该文章是转门用来存储cnblogs的url的)，获取文章里的url链接，存储到CSDN_list中
    4、对cnblogs_url和CSDN_list的内容进行比对，对于cnblogs_url中有，但是CSDN_list中没有的内容，存储到 add_url  中
    3、修改CSDN的文章，将add_url发表到CSDN上
        CSDN自动发表的实现思路：
            1、自动获取CSDN的cookie，存储cookie到本地的cookie.txt中
            2、以后登录就是用cookie登录，如果cookie失效，则重新获取cookie，将本地的cookie文件进行覆盖
用法：
    前提：需要修改本地的配置文件: config.txt  ,将里面的cnblogs_url 替换成你们自己的博客园博客主页，
        将article_CSDN 的内容替换为你们用来专门seo的文章地址
            注意：csdn的文章一定要是用  MD编辑器编辑的文章，我们只需要使用MD编辑器创建一个文章，然后获取该文章的编辑地址即可
'''
import time,datetime

from lxml import etree
import requests,os,json,re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config   #导入配置文件
from selenium.webdriver.chrome.options import Options


def get_cnbologs_articles():
    blog_url =  config.Config.cnblogs_url   #博客园文章地址
    page = 1
    result = []
    while True:
        article_page = blog_url + "/default.html?page={}".format(page)
        req = requests.get(article_page).content.decode("utf-8")
        temp_url = re.findall('<a class="postTitle2 vertical-middle" href="(.*)">', req)
        if temp_url == []:    #如果页数不存在，则自动跳出循环
            break
        for t in temp_url:
            result.append(t)
        page = page+1
    if result == []:
        print("[+]运行错误，请确保你已经在博客园发表文章，并且发表到了首页...")
        exit()

    cnblogs_url = []
    for u in result:
        u = str(u).replace("https://www.cnblogs.com/painter-sec","https://painter-sec.cnblogs.com")
        cnblogs_url.append(u)

    return cnblogs_url
def get_CSDN_url():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36"}
    article_CSDN = config.Config.csdn_article
    req = requests.get(article_CSDN,headers=headers).content.decode("utf-8")
    temp = etree.HTML(req)
    print(temp)
    result = temp.xpath('//*[@id="content_views"]/p/a/@href')    #获取的是CSDN专门用来seo的文章里的url
    url_CSDN = []
    for u in result:
        u = str(u)
        url_CSDN.append(u)

    return url_CSDN


def login_CSDN():
    # 尝试使用cookie登录，前提是cookie没失效的情况下
    print('[+]开始登录CSDN中.....')
    cookie_path = 'cookie.txt'
    browser.get(config.Config.csdn_manage_url)
    with open(cookie_path, 'r', encoding='utf8') as f:
        listcookies = json.loads(f.read())
    # 往browser里添加cookies
    for cookie in listcookies:
        cookie_dict = {
            'domain': '.csdn.net',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        browser.add_cookie(cookie_dict)
    browser.refresh()  # 刷新网页,cookies才成功





def get_CSDN_cookie():
    #获取CSDN的cookie
    if not os.path.exists('cookie.txt') :
        print('cookie不存在，正在获取cookie------.')
        cookie_path = 'cookie.txt'
        browser.get('https://passport.csdn.net/login?code=public')
        browser.implicitly_wait(60)    #最大等待时间60s，如果3s就加载完毕，那么就直接往下执行，60s还没执行完毕，也继续往下执行
        input('在打开的浏览器中手工登录，登录成功后按下enter>>>>>>')
        dictcookies = browser.get_cookies()  # 获取list的cookies
        jsoncookies = json.dumps(dictcookies)  # 转换成字符串保存
        with open(cookie_path, 'w') as f:
            f.write(jsoncookies)
        print('cookies保存成功！')

def get_add_url():
    #通过对比，获取需要添加的url
    add_url = []
    cnblogs_url = get_cnbologs_articles()     #得到cnblogs的url
    url_CSDN = get_CSDN_url()   #得到CSDN的url
    for target in cnblogs_url:
        if target not in url_CSDN :
            add_url.append(target)
    if len(add_url) == 0:
        print("[+]没有变更内容，不需要添加，程序正在推出...")
        exit()
    #每次都提前清空add_message.md文件
    with open("add_message.md","w",encoding="utf-8") as f:
        f.write('')
    for temp in add_url:
        with open("add_message.md","a+",encoding="utf-8") as f:
            f.write('<a href="'+temp+"\""+">"+temp+'</a>'+'\n')

    with open("add_message.md",'r',encoding="utf-8") as f :
        add_message = f.readlines()
    return add_message
def update_article():
    #更新CSDN的文章
    add_message = get_add_url()   #待添加的数据
    print("[+]预计新增数据{}条".format(len(add_message)))
    browser.get(config.Config.csdn_edit_url)    #打开文章编辑界面
    time.sleep(3)
    # browser.switch_to_frame(0)    #切换到frame标签里，否则下面找不到元素
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/pre/div[1]").send_keys(Keys.CONTROL + 'a')    #全选
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/pre/div[1]").send_keys(Keys.ARROW_DOWN)      #按下  向下的 案件
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/pre/div[1]").send_keys(str(datetime.date.today())+" 提交{}条".format(len(add_message))+'\n')    #输入内容,进行分隔，区分是哪一天提交的
    time.sleep(1)
    for info in add_message:
        browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/pre/div[1]").send_keys(info)
    time.sleep(1.5)
    while True:
        try :
            browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[3]/button").click()
        except:
            break
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/button[2]").click()
    print("[+]更新成功...")






if __name__ == '__main__':
    chrome_options = Options()
    # chrome_options.add_argument('--window-size=1920,1080')  # 设置窗口界面大小
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    # browser = webdriver.Chrome()  # 必须要放在外面，否则窗口会自动关闭
    #如果报错，就重新获取cookie
    try :
        login_CSDN()
    except:
        print("[+]cookie失效，请在稍后的登录窗口中重新登录，重新获取cookie...")
        get_CSDN_cookie()
    update_article()
