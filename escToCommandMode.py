import sublime, sublime_plugin

class ExitAutoCompleteAndInsertMode(sublime_plugin.TextCommand):

    def run(self, edit):

        self.view.run_command("exit_insert_mode")

        self.view.run_command("hide_auto_complete")
