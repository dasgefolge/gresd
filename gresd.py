import sys
import tcp

def main(cmd, args):
    server = tcp.ProgressServer((tcp.HOST, tcp.PORT), tcp.ProgressRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1:] if len(sys.argv) > 1 else [])
