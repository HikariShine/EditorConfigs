import sublime
import sublime_plugin


class ScrollToBofCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.run_command('move', {'by': 'lines', 'forward': False})
        # 移动到指定位置，使用下面的方法，先使用text_point方法定位位置，在使用sel().clear()清除当前选区
        # 接着使用sel().add(sublime.Region(pt))增加当前点到选区，最后显示选区完成移动操作。
        pt = self.view.text_point(2, 0)
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(pt))
        self.view.show(pt)