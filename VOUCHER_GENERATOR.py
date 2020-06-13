class Run:
    def __init__(self):

        from kivy.app import App
        from kivy.uix.screenmanager import Screen

        class VoucherScreen(Screen):

            with open("voucher.txt") as f:

                voucher = f.read()

        class VoucherApp(App):

            def build(self):
                return VoucherScreen()


        VoucherApp().run()


obj = Run()
