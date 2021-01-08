# Part 1 
##### autotest-基于web的测试管理平台
##### 功能模块：

 * 用户系统 <br>
  <small>--已实现：注册登录、菜单权限管理</small> 
 * 项目管理
  <small>（对接公司的项目管理平台，根据需求，集成部分常用功能）</small>
 * 环境管理
  <small>（对接公司的运维平台，根据需求，集成部分常用功能）</small>
 * 用例管理  <br>
 <small>--已实现：支持在web平台根据模板（http,web-ui,app-ui等）录入测试用例并提交到后台，实现测试数据的持久化。**便于团队协作，历史问题复现** </small><br>
  <small>--开发中：http接口支持调试、mock; ui测试任务提供任务监控功能; 支持用例批量导入</small>

##### 技术栈：
`python` `flask` `sqlalchemy` `bootstrap`

*web平台的实现代码在app\目录下

##### 快速部署：
```
git clone this_repo
cd autotest
virtualenv venv
source venv/bin/activate  
pip install -r requirements.txt
*for mac/linux:  (只在mac上做过测试...)
sh build.sh     (启动本地调试服务器，访问localhost:5000/login)
```
##### 有问题请联系: 
  qq: 124394105

# Part 2

##### 项目中有两个简单的测试脚本：

1. test-http.py  可以跑起来
2. test-webui.py 简单实现了基于关键字驱动+数据驱动的自动化测试（还需要稍作调试，大致的逻辑已经梳理好，详见代码注释）<br>

测试平台维护的数据能够和这样的测试脚本实现联动


### 备注：

1. 目前web前端部分采用的flask-bootstrap插件不方便做交互，仅实现了增+查，难以实现对数据进行筛选、排序、分页等操作。正在用Vue进行重构，框架已经搭好。
2. 项目结构混乱，后续会优化
3. 各种优化工作预计还需5~7天
