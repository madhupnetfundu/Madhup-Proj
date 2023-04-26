import json

class LoadTestScenario:
    def __init__(self, load_percentage, nodes_per_vm_cluster, cores_per_vm):
        self.load_percentage = load_percentage
        self.nodes_per_vm_cluster = nodes_per_vm_cluster
        self.cores_per_vm = cores_per_vm

    def get_json(self):
        scenario = {
            "description": f"Example: Create {self.nodes_per_vm_cluster}-node {self.cores_per_vm}-core VM Clusters",
            "loadPercentage": self.load_percentage,
            "nodesPerVmCluster": self.nodes_per_vm_cluster,
            "coresPerVm": self.cores_per_vm
        }
        return scenario


load_percentage = int(input("Enter load percentage: "))
nodes_per_vm_cluster = int(input("Enter number of nodes per VM cluster: "))
cores_per_vm = int(input("Enter number of cores per VM: "))

scenario = LoadTestScenario(load_percentage, nodes_per_vm_cluster, cores_per_vm)

print(json.dumps(scenario.get_json(), indent=4))

