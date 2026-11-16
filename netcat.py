import socket

RESET = "\033[0m"
BEYAZ = "\033[1;37m"
GRI = "\033[38;2;120;120;120m"
CYAN = "\033[38;2;0;255;255m"


def spiderweb():
    ascii_art = """
     _____  _____  _____ 
    |___  ||___  ||___  |
       / /    / /    / / 
      / /    / /    / /  
     /_/    /_/    /_/   
    """
    print(CYAN + ascii_art + RESET)
    try:
        ip = input(GRI + "Enter IP: " + RESET)
        port = int(input(GRI + "Enter Port: " + RESET))

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen(1)
        print(GRI + "[+] Listening to..." + RESET)

        conn, addr = s.accept()
        print(GRI + "[+] Connection from: ", addr, RESET)

        data = conn.recv(1024)
        print(GRI + "[+] Received: " + data.decode(errors="replace"), "From: ", addr , RESET)

    except KeyboardInterrupt:
        print(CYAN + "[-] User aborted." + RESET)

    except TimeoutError:
        print(CYAN + "[-] Timeout error." + RESET)

    except ConnectionResetError:
        print(CYAN + "[-] Connection reset error." + RESET)

    except ConnectionRefusedError:
        print(CYAN + "[-] Connection refused." + RESET)

    except OSError as e:
        print(CYAN + "[-] Socket error:", e, RESET)

    except ValueError:
        print(CYAN + "[-] Invalid port." + RESET)
spiderweb()

