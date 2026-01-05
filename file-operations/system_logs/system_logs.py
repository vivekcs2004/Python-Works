system_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/system_logs/system_logs.txt"
info_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/system_logs/info_path.txt"
error_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/system_logs/error.txt"
warning_path = "C:/Users/vivek/OneDrive/Desktop/DEVELOPMENT-JOURNEY/PYTHON-WORKS/file-operations/system_logs/warning.txt"

fr_system = open(system_path,"r")
fw_info = open(info_path,"w")
fw_error = open(error_path,"w")
fw_warning= open(warning_path,"w")

for line in fr_system:
    log = line.rstrip("\n")

    if "INFO" in log:
        fw_info.write(log+"\n")
    
    elif "ERROR" in log:
        fw_error.write(log+"\n")
    
    else:
        fw_warning.write(log+"\n")




