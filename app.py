from flask import Flask, request, render_template
import socket

app = Flask(__name__)

def scan_ports(target, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        target = request.form["target"]
        start_port = int(request.form["start_port"])
        end_port = int(request.form["end_port"])
        open_ports = scan_ports(target, start_port, end_port)
        return render_template("index.html", target=target, open_ports=open_ports, start_port=start_port, end_port=end_port)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
