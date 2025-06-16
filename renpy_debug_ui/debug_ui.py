import renpy


class DebugUI:
    def __init__(self):
        # Debug UI Configuration
        self.visible = True
        self.hotkey = "K_INSERT"
        self.font_path = "renpy_debug_ui/assets/fonts/MPLUS1p-Regular.ttf"
        self.accordions = {
            "collapsed": False,
            "readme_collapsed": False,
            "lang_collapsed": False,
            "script_collapsed": False,
            "information_collapsed": False,
            "test_prompt_collapsed": False,
        }


        # Tracking
        self.script_pos_filename = ""
        self.script_pos_lineno = 0

        self.input_messages = {
            "test_prompt": "",
        }

    # Debug UI System Methods
    def toggle_visibility(self):
        self.visible = not self.visible
        renpy.exports.restart_interaction()


    # Tracking
    def track_say_statements(self, statement_name):
        targets = [
            "say", "say-bubble", "say-nvl", "say-centered", "menu", "menu-nvl", "menu-with-caption", "menu-nvl-with-caption"
        ]
        if any(statement_name.startswith(t) for t in targets):
            filename, lineno = renpy.exports.get_filename_line()
            self.script_pos_filename = filename
            self.script_pos_lineno = lineno

    def input_prompt(self, key, prompt):
        self._input_data_key = key
        self._input_data_prompt = prompt
        self._input_temp_message = self.input_messages.get(key, "")

        renpy.exports.show_screen("debug_ui_input_prompt")

    def handle_input_result(self, key, message):
        if message is not None:
            self.input_messages[key] = message
        renpy.exports.restart_interaction()
