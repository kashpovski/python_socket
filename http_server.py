import socket
import random
import datetime
import http

IP_ADDRESS = "localhost"
PORT = random.randint(8083, 8083)

end_of_stream = "\r\n\r\n"


def handler_client(client, byte: int, stopper: str):
    client_data = ""
    frame_client_data = client.recv(byte)
    with client:
        while frame_client_data:
            client_data += frame_client_data.decode()
            if stopper in client_data:
                break
        print(f"data received")

        len_headers = client_data.find(stopper)
        headers = client_data[:len_headers].split("\r\n")
        method = headers[0].split()[0]

        status = headers[0].split()[1].rpartition("/?status=")[2]
        try:
            status_code = http.HTTPStatus(int(status)).value
        except ValueError:
            status_code = 200
        status_code_name = http.HTTPStatus(status_code).name

        http_response_headers = (
            f"HTTP/1.0 200 OK\r\n"
            f"Server: http server\r\n"
            f"Date: {datetime.datetime.now()}\r\n"
            f"Content-type: text/text; charset=UTF-8\r\n"
            f"\r\n"
        )

        http_response_body = (
            f"Request Method: {method}\r\n"
            f"Request Source: {client.getsockname()[0]}:{client.getsockname()[1]}\r\n"
            f"Response Status: {status_code} {status_code_name}\r\n"
            f"{'new_line'.join(map(str, headers[1:]))}\r\n".replace("new_line", "\n")
        )

        data_send = client.send(http_response_headers.encode()
                                + http_response_body.encode())
        print(f"data send: {data_send} byte")


with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
    server_socket.bind((IP_ADDRESS, PORT))
    server_socket.listen()
    print(f"Web server start {datetime.datetime.now()}\n"
          f"socket family: {server_socket.family.name}\n"
          f"socket type: {server_socket.type.name}\n"
          f"socket bind: {server_socket.getsockname()[0]}:{server_socket.getsockname()[1]}\n"
          )

    while True:
        print("Web server listening...\n")
        client_connection, client_address = server_socket.accept()
        print(f"Client accept: {client_address[0]} {client_address[1]}")

        handler_client(client=client_connection,
                       byte=1024,
                       stopper=end_of_stream
                       )
        print("Client disconnect\n")


