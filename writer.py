import grpc
import item_pb2
import item_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = item_pb2_grpc.ItemServiceStub(channel)

# Update this with desired payload
order = item_pb2.ItemMessage(
    name="Francisco",
    brand_name="Virtus",
    id=10,
    weight=15.2
)

response = stub.Create(order)