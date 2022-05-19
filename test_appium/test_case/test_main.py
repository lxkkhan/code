from test_appium.page.app import App


class TestMain:
    def test_main(self):
        app = App()
        app.start().main().go_to_search()