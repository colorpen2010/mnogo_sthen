import model
import view, view2
import controller, controller2

while True:
    if model.scena=='igra1':
        view.viewer()
        controller.control()
    elif model.scena=='igra2':
        view2.viewer()
        controller2.control()
