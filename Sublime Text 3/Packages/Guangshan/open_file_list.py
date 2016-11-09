import sublime
import sublime_plugin

class OpenFileListCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        open_file_list = sublime.active_window().views()
        keys = [x.file_name() for x in open_file_list if x.file_name()]
        views = [x for x in open_file_list if x.file_name()]
        self.view.show_popup_menu(keys, lambda choice_index: self.show_choice(choice_index, views))

    def is_enabled(self):
        return True

    def show_choice(self, choice_index, views):
        if choice_index == -1:
            return
        sublime.active_window().focus_view(views[choice_index])
