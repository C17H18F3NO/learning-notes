### pipenv

Pipenv 是基于 pip 的  Python  包管理工具，它和 pip 的用法非常相似，可以 看作 pip 的加强版，它的出现解决了旧的 pip+virtualenv+requirements.txt 的工作方式的弊端。具体来说，它是 pip、Pipfile 和 Virtualenv 的结合体，它让包 安装、包依赖管理和虚拟环境管理更加方便，使用它可以实现高效的  Python  项目开发工作流。

#### 安装pip和Pipenv

pip 是用来安装  Python 包的工具。如果你使用  Python2.7.9 及以上版本或  Python3.4 及以上版本，那么pip已经安装好了。可以使用下面的命令检查 pip是否已经安装：

```
$ pip --version
```

如果报错，那么你需要自己安装pip。

```
$ pip install pipenv
```

这会从PyPI（ Python  Package Index， Python 包索引）上下载并安装指 定的包。

可以使用下面的命令检查Pipenv是否已经安装：

```
$ pipenv --version 
pipenv, version 2018.11.26
```

### pipenv常用命令

 `pipenv install` 创建一个虚拟环境

 `pipenv shell` 激活虚拟环境，`exit` 退出虚拟环境

 `pipenv install requests` 安装 Python 包，`pipenv install django==1.11.7` 安装制定版本的包

 `pipenv uninstall requests` 卸载包

 `pipenv graph` 查看安装的包，以及依赖的其他包

`pipenv update flask` 更新

pipenv install flask  安装flask

