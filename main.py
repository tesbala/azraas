from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.webview import MDWebView
class WebViewApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        screen = MDScreen()
        webview = MDWebView(url="https://azraas.com/")
        screen.add_widget(webview)
        return screen
WebViewApp().run()
