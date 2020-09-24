"""
============================
Author:丁琴
Time: 10:34
E-mail:394597923@qq.com
Company:南京瓦丁科技限公司
============================
"""
import pytest
from selenium import webdriver

from common.handle_confing import conf
from page.page_business import AddBusiness
from page.page_login import Login_Page
from page.page_index import Index_Page
from page.page_goods import AddGoods
from page.page_goodssearch import Good_Search
from page.page_ordersearch import Order_Search
from page.page_order import Order_Page
from page.page_warehouse import WareHouse
from page.page_quoted_price import QuotedPrice
# 登录前后置条件
@pytest.fixture(scope="class")
def login_fixture():
    # 前置条件
    driver = webdriver.Chrome(options=get_option())
    driver.implicitly_wait(20)
    login_page = Login_Page(driver)
    index_page = Index_Page(driver)
    yield login_page, index_page
    #     后置条件
    driver.quit()


# 添加物品,搜索的前置条件
@pytest.fixture(scope="class")
def goods_fixture():
    # 前置条件
    driver = webdriver.Chrome(options=get_option())
    driver.implicitly_wait(20)
    login_page = Login_Page(driver)
    index_page = Index_Page(driver)
    search_page=Good_Search(driver)
    #     添加物品详情页面
    addGoods = AddGoods(driver)
    #     调用登录先去登录
    login_page.login(conf.get("user_data", "mobile"), conf.get("user_data", "pwd"))
    #     登录完之后点击物品模块
    index_page.click_goods()

    yield addGoods, index_page,search_page
    #     后置条件
    driver.quit()

# 添加待交易的前置条件
@pytest.fixture(scope="class")
def business_fixture():
    # 前置条件
    driver = webdriver.Chrome(options=get_option())
    driver.implicitly_wait(30)
    login_page = Login_Page(driver)
    index_page = Index_Page(driver)
    add_business = AddBusiness(driver)
    #     调用登录先去登录
    login_page.login(conf.get("user_data", "mobile"), conf.get("user_data", "pwd"))

    yield index_page, add_business
    #     后置条件
    driver.quit()

# 新建订单前置条件，登录点击订单模块
@pytest.fixture(scope="class")
def order_fixture():
    # 前置条件
    driver = webdriver.Chrome(options=get_option())
    driver.implicitly_wait(30)
    login_page = Login_Page(driver)
    index_page = Index_Page(driver)
    order_page=Order_Page(driver)
    order_search=Order_Search(driver)
    #     调用登录先去登录
    login_page.login(conf.get("user_data", "mobile"), conf.get("user_data", "pwd"))
    # 点击订单
    index_page.click_order()
    yield  index_page,order_page,order_search
    #     后置条件
    driver.quit()

# 新建仓库，先要点击仓模块
@pytest.fixture(scope="class")
def warehouse_fixture():
    # 前置条件
    driver = webdriver.Chrome(options=get_option())
    driver.implicitly_wait(30)
    login_page = Login_Page(driver)
    index_page = Index_Page(driver)
    warehouse_page=WareHouse(driver)
    #     调用登录先去登录
    login_page.login(conf.get("user_data", "mobile"), conf.get("user_data", "pwd"))
    # 点击仓库管理
    index_page.click_warehouse()
    yield  index_page,warehouse_page
    #     后置条件
    driver.quit()

# 新建报价，先要点报价模块
@pytest.fixture(scope="class")
def quotedprice_fixture():
    # 前置条件
    driver = webdriver.Chrome(options=get_option())
    driver.implicitly_wait(30)
    login_page = Login_Page(driver)
    index_page = Index_Page(driver)
    business_page=AddBusiness(driver)
    quotedprice_page=QuotedPrice(driver)
    #     调用登录先去登录
    login_page.login(conf.get("user_data", "mobile"), conf.get("user_data", "pwd"))
    # 点击报价模块
    index_page.click_quotedprice()
    yield  index_page,business_page,quotedprice_page
    #     后置条件
    driver.quit()

def get_option():
    if conf.getboolean('env', "headless"):
        """设置浏览启动的选项：无头模式"""
        opt = webdriver.ChromeOptions()
        opt.binary_location = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"
        opt.add_argument('--no-sandbox')
        opt.add_argument("window-size=1200x600")
        # opt=Options()
        opt.add_argument("--headless")
        return opt
    else:
        return None
