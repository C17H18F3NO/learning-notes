让大家对 Ubuntu 的使用从很 陌生 达到 灵活操作

文件操作

目录操作

网络操作

## 常用 Linux 命令的基本使用

- Linux 刚面世时并没有图形界面，所有的操作全靠命令完成，如 **磁盘操作**、**文件存取**、**目录操作**、**进程管理**、**文件权限** 设定等
- 在职场中，大量的 **服务器维护工作** 都是在 **远程** 通过 **SSH 客户端** 来完成的，并没有图形界面，所有的维护工作都需要通过命令来完成
- 在职场中，作为后端程序员，必须要或多或少的掌握一些 Linux 常用的终端命令
- Linux 发行版本的命令大概有 200 多个，但是常用的命令只有 10 多个而已

> 学习终端命令的技巧：
>
> - 不需要死记硬背，对于常用命令，用的多了，自然就记住了
> - 不要尝试一次学会所有的命令，有些命令是非常不常用的，临时遇到，临时百度就可以

**常用 Linux 命令**

| 序号 | 命令           | 对应英文             | 作用                     |
| :--- | :------------- | :------------------- | :----------------------- |
| 01   | ls             | list                 | 查看当前文件夹下的内容   |
| 02   | pwd            | print wrok directory | 查看当前所在文件夹       |
| 03   | cd [目录名]    | change directory     | 切换文件夹               |
| 04   | touch [文件名] | touch                | 如果文件不存在，新建文件 |
| 05   | mkdir [目录名] | make directory       | 创建目录                 |
| 06   | rm [文件名]    | remove               | 删除指定的文件名         |
| 07   | clear          | clear                | 清屏                     |

> 小技巧
>
> - `ctrl + shift + =` **放大**终端窗口的字体显示
> - `ctrl + -` **缩小**终端窗口的字体显示

### Linux 终端命令格式

```bash
command [-options] [parameter]
```

说明：

- `command`：命令名，相应功能的英文单词或单词的缩写
- `[-options]`：选项，可用来对命令进行控制，也可以省略
- `parameter`：传给命令的参数，可以是 **零个**、**一个** 或者 **多个**

> `[]` 代表可选

### 查阅命令帮助信息（知道）

> 提示
>
> - 现阶段只需要 **知道** 通过以下两种方式可以查询命令的帮助信息
> - 先学习**常用命令**及**常用选项**的使用即可，工作中如果遇到问题可以借助 **网络搜索** 

#### `--help`

```bash
command --help
```

说明：

- 显示 `command` 命令的帮助信息

#### man

```bash
man command
```

说明：

- 查阅 `command` 命令的使用手册

> `man` 是 **manual** 的缩写，是 Linux 提供的一个 **手册**，包含了绝大部分的命令、函数的详细使用说明

使用 `man` 时的操作键：

| 操作键   | 功能                 |
| :------- | :------------------- |
| 空格键   | 显示手册页的下一屏   |
| Enter 键 | 一次滚动手册页的一行 |
| b        | 回滚一屏             |
| f        | 前滚一屏             |
| q        | 退出                 |
| /word    | 搜索 **word** 字符串 |



# 文件和目录常用命令

## 目标

- 查看目录内容
  - `ls`
- 切换目录
  - `cd`
- 创建和删除操作
  - `touch`
  - `rm`
  - `mkdir`
- 拷贝和移动文件
  - `cp`
  - `mv`
- 查看文件内容
  - `cat`
  - `more`
  - `grep`
- 其他
  - `echo`
  - 重定向 `>` 和 `>>`
  - 管道 `|`

##  查看目录内容

### 终端实用技巧

#### 自动补全

- 在敲出文件／目录／命令的前几个字母之后，按下`tab`键
  - 如果输入的没有歧义，系统会自动补全
  - 如果还存在其他 `文件`／`目录`／`命令`，再按一下 `tab` 键，系统会提示可能存在的命令

####  曾经使用过的命令

- 按 `上`／`下` 光标键可以在曾经使用过的命令之间来回切换
- 如果想要退出选择，并且不想执行当前选中的命令，可以按 `ctrl + c`

### `ls` 命令说明

- `ls` 是英文单词 **list** 的简写，其功能为列出目录的内容，是用户最常用的命令之一，类似于 **DOS** 下的 `dir` 命令

#### Linux 下文件和目录的特点

- Linux **文件** 或者 **目录** 名称最长可以有 `256` 个字符
- 以 `.` 开头的文件为隐藏文件，需要用 -a 参数才能显示
- **.** 代表当前目录
- **..** 代表上一级目录

### ls 常用选项

| 参数 | 含义                                         |
| :--- | :------------------------------------------- |
| -a   | 显示指定目录下所有子目录与文件，包括隐藏文件 |
| -l   | 以列表方式显示文件的详细信息                 |
| -h   | 配合 -l 以人性化的方式显示文件大小           |

#### 计算机中文件大小的表示方式（科普）

| 单位 | 英文           | 含义                                            |
| :--- | :------------- | :---------------------------------------------- |
| 字节 | B（Byte）      | 在计算机中作为一个数字单元，一般为 8 位二进制数 |
| 千   | K（Kibibyte）  | 1 KB = 1024 B，千字节 （1024 = 2 ** 10）        |
| 兆   | M（Mebibyte）  | 1 MB = 1024 KB，百万字节                        |
| 千兆 | G（Gigabyte）  | 1 GB = 1024 MB，十亿字节，千兆字节              |
| 太   | T（Terabyte）  | 1 TB = 1024 GB，万亿字节，太字节                |
| 拍   | P（Petabyte）  | 1 PB = 1024 TB，千万亿字节，拍字节              |
| 艾   | E（Exabyte）   | 1 EB = 1024 PB，百亿亿字节，艾字节              |
| 泽   | Z（Zettabyte） | 1 ZB = 1024 EB，十万亿亿字节，泽字节            |
| 尧   | Y（Yottabyte） | 1 YB = 1024 ZB，一亿亿亿字节，尧字节            |

### ls 通配符的使用

| 通配符 | 含义                                 |
| :----- | :----------------------------------- |
| *      | 代表任意个数个字符                   |
| ?      | 代表任意一个字符，至少 1 个          |
| []     | 表示可以匹配字符组中的任一一个       |
| [abc]  | 匹配 a、b、c 中的任意一个            |
| [a-f]  | 匹配从 a 到 f 范围内的的任意一个字符 |



## 切换目录

###  `cd`

- `cd` 是英文单词 **change directory** 的简写，其功能为更改当前的工作目录，也是用户最常用的命令之一

> 注意：Linux 所有的 **目录** 和 **文件名** 都是大小写敏感的

| 命令  | 含义                                   |
| :---- | :------------------------------------- |
| cd    | 切换到当前用户的主目录(/home/用户目录) |
| cd ~  | 切换到当前用户的主目录(/home/用户目录) |
| cd .  | 保持在当前目录不变                     |
| cd .. | 切换到上级目录                         |
| cd -  | 可以在最近两次工作目录之间来回切换     |

### 相对路径和绝对路径

**相对路径** 在输入路径时，最前面不是 **/** 或者 **~**，表示相对 **当前目录** 所在的目录位置

**绝对路径** 在输入路径时，最前面是 **/** 或者 **~**，表示从 **根目录/家目录** 开始的具体目录位置

## 创建和删除操作

### `touch` 

创建文件或修改文件时间
- 如果文件 **不存在**，可以创建一个空白文件
- 如果文件 **已经存在**，可以修改文件的末次修改日期

###  `mkdir`

创建一个新的目录

| 选项 | 含义             |
| :--- | :--------------- |
| -p   | 可以递归创建目录 |

> **新建目录的名称** 不能与当前目录中 **已有的目录或文件** 同名

###  `rm`

删除文件或目录

> 使用 `rm` 命令要小心，因为文件删除后不能恢复

| 选项 | 含义                                                  |
| :--- | :---------------------------------------------------- |
| -f   | 强制删除，忽略不存在的文件，无需提示                  |
| -r   | 递归地删除目录下的内容，**删除文件夹** 时必须加此参数 |

##  拷贝和移动文件

| 序号 | 命令                         | 对应英文 | 作用                                 |
| :--- | :--------------------------- | :------- | :----------------------------------- |
| 01   | tree [目录名]                | tree     | 以树状图列出文件目录结构             |
| 02   | cp 源文件 目标文件           | copy     | 复制文件或者目录                     |
| 03   | mv 路径/源文件 路径/目标文件 | move     | 移动文件或者目录／文件或者目录重命名 |

###  `tree` 

 `tree` 命令可以以树状图列出文件目录结构

| 选项 | 含义       |
| :--- | :--------- |
| -d   | 只显示目录 |

###  `cp` 

 `cp` 命令的功能是将给出的 **文件** 或 **目录** 复制到另一个 **文件** 或 **目录** 中，相当于 **DOS** 下的 `copy` 命令

| 选项 | 含义                                                         |
| :--- | :----------------------------------------------------------- |
| -i   | 覆盖文件前提示                                               |
| -r   | 若给出的源文件是目录文件，则 cp 将递归复制该目录下的所有子目录和文件，目标文件必须为一个目录名 |

###  `mv`

 `mv` 命令可以用来 **移动** **文件** 或 **目录**，也可以给 **文件或目录重命名**

| 选项 | 含义           |
| :--- | :------------- |
| -i   | 覆盖文件前提示 |

##  查看文件内容

| 序号 | 命令                 | 对应英文    | 作用                                                 |
| :--- | :------------------- | :---------- | :--------------------------------------------------- |
| 01   | cat 文件名           | concatenate | 查看文件内容、创建文件、文件合并、追加文件内容等功能 |
| 02   | more 文件名          | more        | 分屏显示文件内容                                     |
| 03   | grep 搜索文本 文件名 | grep        | 搜索文本文件内容                                     |

###  `cat` 

- `cat` 命令可以用来 **查看文件内容**、**创建文件**、**文件合并**、**追加文件内容** 等功能
- `cat` 会一次显示所有的内容，适合 **查看内容较少** 的文本文件

| 选项 | 含义               |
| :--- | :----------------- |
| -b   | 对非空输出行编号   |
| -n   | 对输出的所有行编号 |

> Linux 中还有一个 `nl` 的命令和 `cat -b` 的效果等价

###  `more`

- `more` 命令可以用于分屏显示文件内容，每次只显示一页内容
- 适合于 **查看内容较多**的文本文件

使用 `more` 的操作键：

| 操作键   | 功能                 |
| :------- | :------------------- |
| 空格键   | 显示手册页的下一屏   |
| Enter 键 | 一次滚动手册页的一行 |
| b        | 回滚一屏             |
| f        | 前滚一屏             |
| q        | 退出                 |
| /word    | 搜索 **word** 字符串 |

###  `grep`

- Linux 系统中 `grep` 命令是一种强大的文本搜索工具
- `grep`允许对文本文件进行 **模式**查找，所谓模式查找，又被称为正则表达式，在就业班会详细讲解

| 选项 | 含义                                     |
| :--- | :--------------------------------------- |
| -n   | 显示匹配行及行号                         |
| -v   | 显示不包含匹配文本的所有行（相当于求反） |
| -i   | 忽略大小写                               |

- 常用的两种模式查找

| 参数 | 含义                         |
| :--- | :--------------------------- |
| ^a   | 行首，搜寻以 **a** 开头的行  |
| ke$  | 行尾，搜寻以 **ke** 结束的行 |

##  其他

###  `echo 文字内容`

- `echo` 会在终端中显示参数指定的文字，通常会和 **重定向** 联合使用

###  重定向 `>` 和 `>>` 

- Linux 允许将命令执行结果 **重定向**到一个 **文件** 
- 将本应显示在**终端上的内容** **输出／追加** 到**指定文件中** 

其中

- `>` 表示输出，会覆盖文件原有的内容
- `>>` 表示追加，会将内容追加到已有文件的末尾

###  管道 `|` 

- Linux 允许将 **一个命令的输出** 可以**通过管道** 做为 **另一个命令的输入** 
- 可以理解现实生活中的管子，管子的一头塞东西进去，另一头取出来，这里 `|` 的左右分为两端，左端塞东西（写），右端取东西（读）

常用的管道命令有：

- `more`：分屏显示内容
- `grep`：在命令执行结果的基础上查询指定的文本