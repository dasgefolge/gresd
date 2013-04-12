import socketserver
import sys

HOST = "localhost"
PORT = 4468

class ProgressServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ProgressRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # received a connection
        print("CONN %s:%s" % self.client_address)
        while True:
            try:
                line = self.rfile.readline()
            except:
                break
            if not line:
                break
            line = line.decode("utf-8").rstrip("\n")
            # received a line
            print(("RECV %s:%s " % self.client_address) + line)
            if line == "QUIT":
                break
            to_send = "ERROR 1 unknown command"
            try:
                self.wfile.write((to_send + "\n").encode("utf-8"))
            except:
                break
            else:
                # sent a line
                print(("SEND %s:%s " % self.client_address) + to_send)
        # disconnecting or disconnected
        print("DISC %s:%s" % self.client_address)

def main(cmd, args):
    server = ProgressServer((HOST, PORT), ProgressRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1:] if len(sys.argv) > 1 else [])
