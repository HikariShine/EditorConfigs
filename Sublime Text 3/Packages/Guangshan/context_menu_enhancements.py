# coding=utf8
import sublime
import sublime_plugin
import os

# 暂时先依赖SideBarAPI吧，想独立的话可以去除SideBarAPI
from SideBarEnhancements.SideBarAPI import SideBarItem, SideBarSelection

global s
s = sublime.load_settings('Side Bar.sublime-settings')

class ViewEditToRightCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		window = sublime.active_window()
		view_to_right = window.active_view();
		window.run_command('set_layout', {"cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]})
		window.focus_group(1)
		window.set_view_index(view_to_right, 1, 0)

	def is_enabled(self, paths = []):
		return True

	def is_visible(self, paths =[]):
		return True

class CopyRelationPathCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		window = sublime.active_window()
		path = window.active_view().file_name()
		for directory in sublime.active_window().folders():
			path = path.replace(directory, '', 1)
		path.replace('\\', '/')
		if len(path) > 0:
			sublime.set_clipboard(path);
			sublime.status_message("Item copied")

	def is_visible(self, paths =[]):
		window = sublime.active_window()
		path = window.active_view().file_name()
		path2 = window.active_view().file_name()
		for directory in sublime.active_window().folders():
			path2 = path2.replace(directory, '', 1)
		return path != path2

# 下面这两个命令是从SideBarEnhancements插件中抽取出来的，与原插件内容略重复，可以抽取成方法公共调用。
class ContextOpenCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		window = sublime.active_window()
		path = window.active_view().file_name()
		dirname, filename = os.path.split(path)
		if sublime.platform() == 'osx':
			import subprocess
			subprocess.Popen(['open', filename], cwd=dirname)
		elif sublime.platform() == 'windows':
			import subprocess
			subprocess.Popen(['start',  '', path.replace("^", "^^")], cwd=dirname, shell=True)
		else:
			# linux下可能无效
			from . import desktop
			desktop.open(dirname)
			print('using desktop')

	def is_enabled(self, paths = []):
		return True

	def is_visible(self, paths =[]):
		return True

class ContextOpenTerminalCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		import subprocess
		window = sublime.active_window()
		path = window.active_view().file_name()
		dirname, filename = os.path.split(path)
		if sublime.platform() == 'osx':
			subprocess.Popen(['/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal', '.'], cwd=self.forCwdSystemPath())
		elif sublime.platform() == 'windows':
			if s.get('use_powershell', True):
				try:
					subprocess.Popen(['start', 'powershell'], cwd=dirname, shell=True)
				except:
					subprocess.Popen(['start', 'cmd', '.'], cwd=dirname, shell=True)
			else:
				subprocess.Popen(['start', 'cmd', '.'], cwd=dirname, shell=True)
		elif sublime.platform() == 'linux':
			subprocess.Popen(['gnome-terminal', '.'], cwd=dirname)

	def is_enabled(self, paths = []):
		return True

	def is_visible(self, paths =[]):
		return True

# 2016年11月13日10:26:40
# 用于屏蔽纯文件夹的打开控制台，文件夹打开控制台使用Terminal插件，缺点是Terminal插件不能多选文件夹并打开控制台。
# 2016-11-13 13:26:56
# 功能改变，Open / Run命令改为用默认方式打开，在只有文件夹时不显示。
class SideBarOpenCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		dirs =[path for path in paths if os.path.isdir(path)] + [os.path.split(path)[0] for path in paths if not os.path.isdir(path)]
		dirs = list(set(dirs))
		for item in SideBarSelection(paths).getSelectedItems():
			item.open(s.get('use_powershell', True))

	def is_enabled(self, paths = []):
		return True

	def is_visible(self, paths =[]):
		is_all_dir = True
		for path in paths:
			if not os.path.isdir(path):
				is_all_dir = False
		return (not s.get('disabled_menuitem_open_run', False)) & (not is_all_dir)

class SideBarOpenTerminalCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		dirs =[path for path in paths if os.path.isdir(path)] + [os.path.split(path)[0] for path in paths if not os.path.isdir(path)]
		dirs = list(set(dirs))
		for item in [SideBarItem(directory, True) for directory in dirs]:
			item.open(s.get('use_powershell', True))

	def is_enabled(self, paths = []):
		return True

	def is_visible(self, paths =[]):
		return True

# 从项目文件夹打开命令行
class OpenTerminalFromProjectCommand(sublime_plugin.WindowCommand):
	def run(self, paths = []):
		# 从Terminal拷贝过来的path获取规则，可以研究下
		window = sublime.active_window()
		if paths and not len(paths) < 1:
			path = paths[0]
		elif window.active_view() and window.active_view().file_name():
			path = window.active_view().file_name()
		elif window.folders():
			path = window.folders()[0]
		else:
			sublime.error_message('Terminal: No place to open terminal to')
			return
		# DEV: On ST3, there is always an active view.
		#   Be sure to check that it's a file with a path (not temporary view)
		if not path:
			return

		# DEV: We require separator to be appended since `/hello` and `/hello-world`
		#   would both match a file in `/hello` without it
		#   For more info, see https://github.com/wbond/sublime_terminal/issues/86
		dirs = [x for x in window.folders() if path.find(x + os.sep) == 0][0:1]
		# 增加不在项目中的时候的默认行为，在当前文件目录打开命令行
		if not dirs:
			dirs = [os.path.split(path)[0]]
		for item in [SideBarItem(directory, True) for directory in dirs]:
			item.open(s.get('use_powershell', True))

# 隐藏 give20
class SideBarDonateCommand(sublime_plugin.WindowCommand):
	def is_visible(self, paths =[]):
		return False
