#!/bin/bash
set -eo pipefail

if [ -f ../gambit.proto ]; then
    cd ../
fi

if [ ! -f ./gambit.proto ]; then
    echo "Cannot find the proto file, please run this script like this:"
    echo " $ cd ./hack; ./generate_proto.bash"
    echo " OR "
    echo " $ ./hack/generate_proto.bash"
    exit 1
fi

if ! python -m grpc_tools.protoc \
     -I./ \
     --python_out=. \
     --grpc_python_out=. \
     ./gambit.proto; then
    CODE=$?
    echo "The command failed, remember to install grpcio-tools if necessary:"
    echo "  $ pip install --user grpcio-tools"
    exit $CODE
fi

echo "Generation complete!"
