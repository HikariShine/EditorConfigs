import sublime
import sublime_plugin


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
