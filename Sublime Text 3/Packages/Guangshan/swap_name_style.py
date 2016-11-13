import sublime
import sublime_plugin
import string

class SwapNameStyleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for r in view.sel():
			if r.empty():
				r = view.word(r)

			s = view.substr(r)
			if self.is_underscore_case(s):
				txt = self.dash_case(s.split('_'))
			elif self.is_dash_case(s):
				txt = self.camel_case(s.split('-'))
			else:
				indexs = ([] if s[0] == s[0].capitalize() else [0]) + [i for i,c in enumerate(s) if c == c.capitalize()]
				strings = [s[indexs[i-1]:index] for i,index in enumerate(indexs) if i != 0] + [s[indexs[-1]:]]
				if len(strings) == 1:
					txt = s[0].swapcase() + s[1:]
				else:
					txt = self.underscore_case(strings)
			view.replace(edit, r, txt)

	# 驼峰命名法，默认大驼峰
	def camel_case(self, strings, upper = True):
		if upper:
			return ''.join([s.capitalize() for s in strings])
		else:
			return ''.join([strings[0]] + [s.capitalize() for s in strings[1:]])

	# 下划线风格
	def underscore_case(self, strings):
		return '_'.join([s[0].lower() + s[1:] for s in strings])

	def dash_case(self, strings):
		return '-'.join(strings)

	# 驼峰风格
	def is_camel_case(self, string):
		return not self.is_dash_case(string) and self.is_underscore_case(string)

	# 下划线风格
	def is_underscore_case(self, string):
		return string.find('_') >= 0

	# 中横线风格
	def is_dash_case(self, string):
		return string.find('-') >= 0
