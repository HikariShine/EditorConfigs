# coding=utf8
import sublime
import sublime_plugin
import os

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

# 隐藏 give20
class SideBarDonateCommand(sublime_plugin.WindowCommand):
	def is_visible(self, paths =[]):
		return False
