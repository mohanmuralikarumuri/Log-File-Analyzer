try:
    file = open("server.log", "r")

    info = 0
    warning = 0
    error = 0

    for line in file:

        if "INFO" in line:
            info += 1

        elif "WARNING" in line:
            warning += 1

        elif "ERROR" in line:
            error += 1

    file.close()

    print("===== LOG ANALYZER =====")
    print("INFO    :", info)
    print("WARNING :", warning)
    print("ERROR   :", error)

except FileNotFoundError:
    print("Error: server.log file not found")

except PermissionError:
    print("Error: Permission denied")