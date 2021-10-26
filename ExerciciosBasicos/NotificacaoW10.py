from win10toast import ToastNotifier


toaster = ToastNotifier()

toaster.show_toast(
    "Notificação", 
    "Olá Magidel :)",
    threaded=True,
    icon_path=None,
    duration=3 
)