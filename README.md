# 项目使用说明
- - - 
## 前端
- 项目使用Vue.js框架
- 项目使用ElementUI组件库
- 项目使用axios进行前后端数据交互
- 项目使用vue-router进行路由管理
- 端口为5173
### 启动方式
```shell
cd /vue-project/src
npm install #如果没有node_modules文件夹
npm run dev
```

## 后端
- 项目使用Django框架
- 项目使用Django REST framework进行前后端数据交互
- 本项目没有使用数据库，所有数据都是存储在内存中
- 端口为8000
### 启动方式
```shell
cd /mysite/mysite
python manage.py runserver
```

### 文件路径处理
- 关于聚合表，路径不需要更改，已经存在temporary文件夹中了
- 对于原始表，需要在`/mysite/mysite/visual_app/views.py`中修改`SOURCE_AGGREGATE_DIR `的值为原始表的路径，这样才能正常使用原始表的数据

## 应用程序使用
- 具体可以看发在群里的视频