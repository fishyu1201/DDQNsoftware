# DDQNSoftware

## 编写逻辑

DDQNSoftware 是一个基于 PyQt5 构建的软件，它采用了前后端开发的分离方式。通过 QtDesigner 插件，我们可以可视化生成前端文件 mainwindow.ui。然后，使用 PyUIC 插件将 mainwindow.ui 转换为可执行的 mainwindow.py 文件。mainwindow.py 文件用于生成软件的前端界面，而 main.py 文件则是软件的后端代码。
这种分离的开发方式使得我们可以单独修改前端或后端代码，便于后续的维护和开发工作。

## 项目结构

```
├── .idea                   # PyCharm生成的配置文件夹
├── build                   # pyinstaller生成exe文件的过程生成的文件夹
├── designer                # 代码文件夹
│   ├── input.txt           # 用于测试软件导入文件功能的示例文件
│   ├── mainwindow.ui       # 前端ui文件
│   ├── mainwindow.py       # 前端py文件
│   └── main.py             # 软件主程序以及后端py文件
├── 参考样式.png            # 该软件的原型参考样式图片
└── README.md               # 项目说明文档
```

## 运行要求

DDQNSoftware 的运行环境不要求安装 Python，因此运行端无需安装 Python 环境即可运行。不过，对于性能方面有一定要求。
