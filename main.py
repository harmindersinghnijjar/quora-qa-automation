from quora_automation import *


# Check if json file exists. If it does, run quora_automation.py. 
# If not, display GUI then run quora_automation.py
if check_json():
    print("json exists")
    # Create main window.
    root = Tk()
    print("root created")
    root.title("Quora Automation")
    root.geometry("400x400")
    root.update()
    print("root updated")
    start_gui(root)
    print("start_gui ran")

    
else:
    print("json does not exists")
    # Create main window.
    root = Tk()
    print("root created")
    root.title("Quora Automation")
    root.geometry("400x400")
    root.update()
    api_gui(root)
    print("api_gui ran")
    
root.mainloop()