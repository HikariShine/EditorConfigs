安装的数据目录：C:\Users\Administrator\AppData\Roaming\Sublime Text 3

安装的插件目录：${data_dir}\Installed Packages

用户的插件目录(可覆盖默认插件)：${data_dir}\Packages

其中已有目录：${data_dir}\Packages\User，最优先加载的插件，包括两个重要的文件：

Default (Windows).sublime-keymap：用户的快捷键配置，可覆盖默认配置

Preferences.sublime-settings：软件设置（界面、布局、字体等基本设置），可覆盖默认配置

<executable_path>/Packages：默认插件目录，有以下几个插件。
```
Packages/Default/delete_word.py Deletes a word to the left or right of the cursor
Packages/Default/duplicate_line.py Duplicates the current line
Packages/Default/exec.py Uses phantoms to display errors inline
Packages/Default/font.py Shows how to work with settings
Packages/Default/goto_line.py Prompts the user for input, then updates the selection
Packages/Default/mark.py Uses add_regions() to add an icon to the gutter
Packages/Default/show_scope_name.py Uses a popup to show the scope names at the caret
Packages/Default/trim_trailing_whitespace.py Modifies a buffer just before its saved
```
用户插件目录： <data_path>/Installed Packages

可能找不到上述几个文件，其实他们是在这个目录下的Default.sublime-package文件,文件后缀改为zip解压就可以看到源文件了。

如何覆盖这些插件呢？只要Packages/<Package Name>创建这样一个目录即可。假设覆盖Python.sublime-package文件的function.sublime-snippet内容，创建一个目录Python在<data_path>/Packages下，文件function.sublime-snippet放到里面即可。

例如我要把duplicate_line.py换掉，修改成可以增加上下复制的方法（类似于eclipse），可这样修改：