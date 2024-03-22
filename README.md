#DDQNSoftware#
DDQNSoftware 是一个基于 PyQt5 构建的软件，它采用了前后端开发的分离方式。通过 QtDesigner 插件，我们可以可视化生成前端文件 mainwindow.ui。然后，使用 PyUIC 插件将 mainwindow.ui 转换为可执行的 mainwindow.py 文件。mainwindow.py 文件用于生成软件的前端界面，而 main.py 文件则是软件的后端代码。

这种分离的开发方式使得我们可以单独修改前端或后端代码，便于后续的维护和开发工作。

DDQNSoftware 的运行环境不要求安装 Python，因此运行端无需安装 Python 环境即可运行。不过，对于性能方面有一定要求。
