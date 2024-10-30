import grpc
from proto import user_pb2, user_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)

        # Send a request with a valid integer ID
        request = user_pb2.GetUserRequest(id=1)  # Use an integer value here
        response = stub.GetUser(request)

        print(f"Id: {response.users[0].id}, User: {response.users[0].name}, Email: {response.users[0].email}")

if __name__ == "__main__":
    run()
