from concurrent import futures

import grpc

import item_pb2
import item_pb2_grpc


class ItemServicer(item_pb2_grpc.ItemServiceServicer):

    def Create(self, request, context):

        request_value = {
            'name': request.name,
            'brand_name': request.brand_name,
            'id': int(request.id),
            'weight': request.weight
        }

        print(request_value)
        return item_pb2.ItemMessage(**request_value)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
item_pb2_grpc.add_ItemServiceServicer_to_server(ItemServicer(), server)

print('server starting... 5005 port')
server.add_insecure_port('[::]:5005')
server.start()
server.wait_for_termination()