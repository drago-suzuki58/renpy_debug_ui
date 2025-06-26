# screens
screen debug_ui_display():
    layer "debug_ui_layer"

    key debug_ui.hotkey action Function(debug_ui.toggle_visibility)

    if debug_ui.visible:
        button:
            style "debug_ui"
            focus_mask True
            action NullAction()

            vbox:
                spacing 6

                textbutton ("[DBG]▼" if debug_ui.accordions["collapsed"] else "[DBG]▲") + " " + "Debug UI" action ToggleDict(debug_ui.accordions, "collapsed") style "debug_ui_title_accordion"
                if not debug_ui.accordions["collapsed"]:
                    viewport:
                        draggable True
                        mousewheel True
                        scrollbars "vertical"

                        vbox:
                            spacing 8

                            use debug_ui_readme()
                            use debug_ui_language_section()
                            use debug_ui_script_section()
                            use debug_ui_information_section()
                            use debug_ui_store_explorer()
                            use debug_ui_test_prompt()


screen debug_ui_readme():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("readme_collapsed", "[DBG]Debug UI Readme")
            if not debug_ui.accordions["readme_collapsed"]:
                vbox:
                    text "[DBG]This is a Debug UI for Ren'Py games." style "debug_ui_text"
                    text "[DBG]Press the hotkey (default: Insert) to toggle the visibility of this UI." style "debug_ui_text"
                    textbutton "[DBG]Close" action Function(debug_ui.toggle_visibility) style "debug_ui_button"

screen debug_ui_language_section():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("lang_collapsed", "[DBG]Language Settings")
            if not debug_ui.accordions["lang_collapsed"]:
                vbox:
                    textbutton "[DBG]Default Language" action Language(None) style "debug_ui_button"
                    for code in renpy.known_languages():
                        textbutton DBG + code action Language(code) style "debug_ui_button"

screen debug_ui_script_section():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("script_collapsed", "[DBG]Script Position")
            if not debug_ui.accordions["script_collapsed"]:
                vbox:
                    text "[DBG]File: [debug_ui.script_pos_filename]" style "debug_ui_text"
                    text "[DBG]Line: [debug_ui.script_pos_lineno]" style "debug_ui_text"

screen debug_ui_information_section():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("information_collapsed", "[DBG]Information Metrics")
            if not debug_ui.accordions["information_collapsed"]:
                python:
                    try:
                        renderer_info = renpy.get_renderer_info()
                        renderer_name = renderer_info.get("renderer", "Unknown") if renderer_info else "Unknown"
                        physical_size_x, physical_size_y = renpy.get_physical_size()
                    except:
                        renderer_name = "Unknown"

                vbox:
                    text "[DBG]Screen" style "debug_ui_text" size 20
                    text "[DBG]Screen Size: [config.screen_width]x[config.screen_height]" style "debug_ui_text"
                    text "[DBG]Window Size: [physical_size_x]x[physical_size_y]" style "debug_ui_text"
                    text "[DBG]Renderer: [renderer_name]" style "debug_ui_text"
                    text "[DBG]Fullscreen: [preferences.fullscreen]" style "debug_ui_text"

                    text "[DBG]System" style "debug_ui_text" size 20
                    text "[DBG]Ren'Py: [renpy.version_string]" style "debug_ui_text"
                    text "[DBG]Platform: [renpy.platform]" style "debug_ui_text"

screen debug_ui_store_explorer():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("store_explorer_collapsed", "[DBG]Store Explorer")
            if not debug_ui.accordions["store_explorer_collapsed"]:
                textbutton "[DBG]Refresh" action Function(debug_ui.update_store_explorer_cache) style "debug_ui_button"
                vbox:
                    spacing 4

                    for name in debug_ui.cached_store_items:
                        use debug_ui_store_variable(name)

screen debug_ui_test_prompt():
    frame:
        style "debug_ui_section"
        vbox:
            spacing 4

            use debug_ui_accordion("test_prompt_collapsed", "[DBG]Test Prompt")
            if not debug_ui.accordions["test_prompt_collapsed"]:
                vbox:
                    text "[DBG]Test Prompt" style "debug_ui_text"
                    text "[DBG]Current Input: " + debug_ui.input_messages["test_prompt"] style "debug_ui_text" size 12
                    textbutton "[DBG]Set Message" action Function(debug_ui.input_prompt, "test_prompt", "Test Prompt") style "debug_ui_button"


# components
screen debug_ui_accordion(collapsed, header_text):
    textbutton ("[DBG]▼" if debug_ui.accordions[collapsed] else "[DBG]▲") + " " + header_text action ToggleDict(debug_ui.accordions, collapsed) style "debug_ui_accordion"

screen debug_ui_child_accordion(collapsed, header_text):
    textbutton ("[DBG]▼" if debug_ui.child_accordions[collapsed] else "[DBG]▲") + " " + header_text action ToggleDict(debug_ui.child_accordions, collapsed) style "debug_ui_child_accordion"

screen debug_ui_store_variable(name):
    python:
        safe_name = name.replace(' ', '_').replace('-', '_').replace('.', '_')
        child_collapsed_name = "store_explorer_" + safe_name + "_collapsed"

        if child_collapsed_name not in debug_ui.child_accordions:
            debug_ui.child_accordions[child_collapsed_name] = True

    use debug_ui_child_accordion(child_collapsed_name, "[DBG]" + name)
    if not debug_ui.child_accordions[child_collapsed_name]:
        python:
            value = getattr(renpy.store, name)
            value_type_name = type(value).__name__

        vbox:
            text "[DBG]Name: [name]" style "debug_ui_text"
            text "[DBG]Type: [value_type_name]" style "debug_ui_text"

            if isinstance(value, (int, float)):
                use debug_ui_store_number_display(name, value, )
            elif isinstance(value, str):
                use debug_ui_store_string_display(name, value)
            elif isinstance(value, bool):
                use debug_ui_store_bool_display(name, value)
            elif isinstance(value, (list, tuple)):
                use debug_ui_store_list_display(name, value)
            elif isinstance(value, dict):
                use debug_ui_store_dict_display(name, value)
            elif value is None:
                use debug_ui_store_none_display(name, value)
            elif hasattr(value, "__dict__"):
                use debug_ui_store_object_display(name, value)
            else:
                use debug_ui_store_other_display(name, value)

screen debug_ui_store_number_display(name, value):
    python:
        try:
            value_str = str(value)
        except:
            value_str = "<Error displaying value>"

    text "[DBG]Value: [value_str]" style "debug_ui_text"
    textbutton "[DBG]Edit Number" action Function(debug_ui.store_edit, name, value, "[DBG]Enter new number for '[name]'") style "debug_ui_button"

screen debug_ui_store_string_display(name, value):
    python:
        str_length = len(value)
        try:
            if str_length > 100:
                display_value = value[:100] + "..."
            else:
                display_value = value
        except:
            display_value = "<Error displaying value>"

    text "[DBG]Value: \"[display_value]\"" style "debug_ui_text"
    text "[DBG]Length: [str_length]" style "debug_ui_text"
    textbutton "[DBG]Edit String" action Function(debug_ui.store_edit, name, value, "[DBG]Enter new string for '[name]'") style "debug_ui_button"

screen debug_ui_store_bool_display(name, value):
    text "[DBG]Value: [value]" style "debug_ui_text"
    textbutton "[DBG]Toggle Bool" action ToggleVariable(name) style "debug_ui_button"

screen debug_ui_store_list_display(name, value):
    python:
        length = len(value)

    text "[DBG]Length: [length]" style "debug_ui_text"

    for index, item in enumerate(value):
        if index < 10:
            python:
                try:
                    item_display = str(item)[:50]
                except:
                    item_display = "<Error displaying value>"
            text "[DBG][index]: [item_display]" style "debug_ui_text"

    if isinstance(value, list):
        textbutton "[DBG]Edit List" action Function(debug_ui.store_edit, name, value, "[DBG]Enter new list for '[name]'") style "debug_ui_button"

screen debug_ui_store_dict_display(name, value):
    python:
        keys_length = len(value.keys())

        try:
            safe_keys = []
            for k in list(value.keys())[:10]:
                safe_keys.append(str(k))
            value_keys = ', '.join(safe_keys)
        except:
            value_keys = "<Error displaying keys>"

        try:
            dict_items = list(value.items())[:5]
        except:
            dict_items = []

    text "[DBG]Length: [keys_length]" style "debug_ui_text"
    text "[DBG]Keys: [value_keys]" style "debug_ui_text"

    for key, item in dict_items:
        python:
            try:
                key_str = str(key)
                item_str = str(item)[:50]
            except:
                key_str = "<Error displaying key>"
                item_str = "<Error displaying value>"
        text "[DBG][key_str]: [item_str]" style "debug_ui_text"

    textbutton "[DBG]Edit Dict" action Function(debug_ui.store_edit, name, value, "[DBG]Enter new dict for '[name]'") style "debug_ui_button"

screen debug_ui_store_none_display(name, value):
    text "[DBG]Value: None" style "debug_ui_text"
    textbutton "[DBG]Set Value" action Function(debug_ui.store_edit, name, value, "[DBG]Enter new value for '[name]'") style "debug_ui_button"

screen debug_ui_store_object_display(name, value):
    python:
        try:
            safe_attrs = []
            for attr in dir(value)[:10]:
                safe_attrs.append(str(attr))
            attrs_display = ', '.join(safe_attrs)
        except:
            attrs_display = "<Error displaying attributes>"

    text "[DBG]Attributes: [attrs_display]" style "debug_ui_text"

screen debug_ui_store_other_display(name, value):
    python:
        try:
            value_display = str(value)[:100]
        except:
            value_display = "<Error displaying value>"

    text "[DBG]Value: [value_display]" style "debug_ui_text"


# Other
screen debug_ui_input_prompt():
    layer "debug_ui_layer"
    modal True

    button:
        style "debug_ui_textinput"
        action NullAction()

        frame:
            style "debug_ui_textinput_floating"
            vbox:
                spacing 10

                text debug_ui._input_data_prompt style "debug_ui_text" size 20
                frame:
                    style "debug_ui_textinput_section"
                    input value FieldInputValue(debug_ui, "_input_temp_message") style "debug_ui_textinput_input"

                vbox:
                    spacing 10
                    textbutton "[DBG]Submit" action [
                        SetDict(debug_ui.input_messages, debug_ui._input_data_key, debug_ui._input_temp_message),
                        Hide("debug_ui_input_prompt")
                    ] style "debug_ui_button"
                    textbutton "[DBG]Cancel" action Hide("debug_ui_input_prompt") style "debug_ui_button"

screen debug_ui_store_input_prompt():
    layer "debug_ui_layer"
    modal True

    button:
        style "debug_ui_textinput"
        action NullAction()

        frame:
            style "debug_ui_textinput_floating"
            vbox:
                spacing 10

                text "Edit [debug_ui._store_edit_prompt]" style "debug_ui_text" size 20
                frame:
                    style "debug_ui_textinput_section"
                    input value FieldInputValue(debug_ui, "_store_edit_temp") style "debug_ui_textinput_input"

                vbox:
                    spacing 10
                    textbutton "[DBG]Submit" action [
                        Function(debug_ui.set_store_value, debug_ui._store_edit_key, debug_ui._store_edit_temp),
                        Hide("debug_ui_store_input_prompt")
                    ] style "debug_ui_button"
                    textbutton "[DBG]Cancel" action Hide("debug_ui_store_input_prompt") style "debug_ui_button"
