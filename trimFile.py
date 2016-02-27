import sublime, sublime_plugin, re

class trimFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print('trimming white spaces...')
        view = self.view
        trailing_white_space = view.find_all("[\t ]+$")
        trailing_white_space.reverse()
        edit = view.begin_edit()
        for r in trailing_white_space:
            view.erase(edit, r)
        view.end_edit(edit)

        # Trim lines on the end of the file or start of file:
        # reobj = re.compile(r"(\A\s+|\s+\Z)")
        # Trim only from end:
        reobj = re.compile(r"\s+\Z")
        if view.size() > 0:
            region = sublime.Region(0, view.size())
            trimmed = reobj.sub("", view.substr(region))
            view.replace(edit, region, trimmed)

        if view.size() > 0 and view.substr(view.size() - 1) != '\n':
            edit = view.begin_edit()
            view.insert(edit, view.size(), "\n")
            view.end_edit(edit)
