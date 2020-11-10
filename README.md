##generate files

python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ item.proto

##libraries version used

grpcio = "==1.33.2"

grpcio-tools = "==1.33.2"