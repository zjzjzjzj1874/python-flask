# python-flask
flask框架

## gunicorn和uwsgi比较

| 比较维度 | Gunicorn | uWSGI |
|---------|----------|--------|
| 实现语言 | Python + C (gevent) | C |
| 性能表现 | 优秀，适合中小型应用 | 卓越，适合大型应用 |
| 配置复杂度 | 简单，配置文件清晰易懂 | 较复杂，选项丰富但配置繁琐 |
| 安装部署 | 简单，pip安装即可 | 相对复杂，可能需要编译安装 |
| 配置复杂性 | 	简单，快速上手 | 复杂，需学习曲线
| 协议支持	 | 仅 WSGI |	WSGI、uwsgi、HTTP 等 |
| 语言支持	 | 仅 Python |	Python、PHP、Ruby 等 |
| 高级功能	| 基本无	| 缓存、负载均衡、Emperor 模式 |
| 典型搭配	| nginx + Gunicorn |	nginx + uWSGI（uwsgi 协议） |
| 资源占用 | 较低 | 极低 | 
| 功能特性 | - 支持热部署<br>- 支持多进程<br>- 支持多线程<br>- 支持异步<br>- 支持协程<br>- 支持多worker | - 支持热部署<br>- 支持多进程<br>- 支持多线程<br>- 支持异步<br>- 支持协程<br>- 支持多worker |
| 调试便利性 | 优秀，错误信息清晰 | 一般，错误信息相对简单 |
| 社区活跃度 | 非常活跃，更新频繁 | 活跃，但更新相对较慢 |
| 文档完整性 | 完善，示例丰富 | 完善，但部分文档晦涩 |
| 适用场景 | 开发环境和中小型生产环境 | 大型生产环境 |

## 参考链接
- Flask- 官网：https://flask.palletsprojects.com/
- Flask 中文文档：https://flask.palletsprojects.com/zh-cn/stable/quickstart/
- Flask 源码：https://github.com/pallets/flask/
- Flask 菜鸟教程：https://www.runoob.com/flask/flask-tutorial.html