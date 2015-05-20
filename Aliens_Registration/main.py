from ui import Ui
def main():
    ui = Ui()
    details = ui.get_details()
    status = admin.register(details,ui)
    if status == True:
        ui.display( "registration successed")
    else:
        ui.display("registration failed")

