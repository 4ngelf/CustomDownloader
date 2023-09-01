import pytest

from downloader import views


class TestMainWindow:
    def test_check_widgets_is_not_none(self):
        ...

    def test_open_link_prompt_dialog(self):
        ...

    def test_update_and_check_table_after_dialog(self):
        ...

    def test_button_start_download_files(self):
        ...

    def test_table_updates_on_download_progress(self):
        ...

    def test_table_updates_on_download_success(self):
        ...

    def test_table_updates_on_download_failure(self):
        ...


class TestLinkPromptDialog:
    def test_check_list_returned_by_dialog(self):
        ...

    def test_color_no_valid_input(self):
        ...

    def test_special_links_use_special_download_manager(self):
        ...
