# {
#     "description": "Example: Create 2-node 8-core VM Clusters"
#     "loadPercentage": 25,
#     "nodesPerVmCluster": 2,
#     "coresPerVm": 8
# }

import json

load_percentage = int(input("Enter load percentage: "))
nodes_per_vm_cluster = int(input("Enter number of nodes per VM cluster: "))
cores_per_vm = int(input("Enter number of cores per VM: "))
db_setup = True

scenario = {
    "description": f"Example: Create {nodes_per_vm_cluster}-node {cores_per_vm}-core {db_setup} VM Clusters",
    "loadPercentage": load_percentage,
    "nodesPerVmCluster": nodes_per_vm_cluster,
    "coresPerVm": cores_per_vm
}

print(json.dumps(scenario, indent=4))
