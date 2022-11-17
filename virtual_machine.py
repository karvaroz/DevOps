from virtualbox import VirtualBox, Session

vbox = VirtualBox()
session = Session()

newVM = VirtualBox()
nameVM = "Ubuntu"

print([m.name for m in vbox.machines])

machine = vbox.find_machine(nameVM)
progress = machine.launch_vm_process(session, "gui", [])
progress.wait_for_completion()

# session.console.power_down()

vm = newVM.create_machine("",nameVM,[],"ubuntu64Guest","")
newVM.register_machine(vm)

machineBorrar = newVM.find_machine(nameVM)
# machineBorrar.remove()

