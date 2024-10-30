import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grpc_project.settings')

import django
django.setup()

import grpc
from concurrent import futures
from proto import user_pb2, user_pb2_grpc
from users.models import User


class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        try:
            # Ensure request.id is accessed correctly (should be an integer)
            user = User.objects.get(id=request.id)
            response = user_pb2.UserResponse(
                users=[user_pb2.User(id=user.id, name=user.name, email=user.email)]
            )
            return response
        except User.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.UserResponse()


def serve():
    try:
        print("Starting gRPC server...")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        print("gRPC server running on port 50051")
        server.wait_for_termination()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    serve()
