import sublime_plugin


class DuplicateLineCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward):
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                if forward:
                    line_contents = '\n' + self.view.substr(line)
                    self.view.insert(edit, line.end(), line_contents)
                else:
                    line_contents = self.view.substr(line) + '\n'
                    self.view.insert(edit, line.begin(), line_contents)
            else:
                if forward:
                    self.view.insert(edit, region.begin(), self.view.substr(region))
                else:
                    self.view.insert(edit, region.end(), self.view.substr(region))

