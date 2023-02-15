from pages.widgets_page import TabsPage, SliderPage, ProgressBarPage, AutoCompletePage


class TestAutoCompletePage:

    def test_fill_multi_autocomplete(self, driver):
        autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplete_page.open()
        colors = autocomplete_page.fill_input_multi()
        colors_result = autocomplete_page.check_color_in_multi()
        assert colors == colors_result, 'the added colors are missing in the input'


class TestWidgets:
    class TestSliderPage:
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after, 'the slider value has not been changed'

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after, 'the progress bar value has not been changed'

    class TestTabsPage:
        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            more_button, more_content = tabs.check_tabs('more')
            assert what_button == 'What' and what_content != 0, 'the tab "what" was not pressed or the text is missing'
            assert origin_button == 'Origin' and origin_content != 0, 'the tab "origin" was not pressed or the text is missing'
            assert use_button == 'Use' and use_content != 0, 'the tab "use" was not pressed or the text is missing'
            assert more_button == 'More' and what_content != 0, 'the tab "more" was not pressed or the text is missing'
