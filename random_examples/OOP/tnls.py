import json


class TwoNodeLoadScenario:
    nodes_per_vm_cluster = 2
    description1_1 = "Example: Create 2-node 4-core dbonvault VM Clusters"
    description1_2 = "Example: Create 2-node 8-core VM Clusters"
    description1_3 = "Example: Create 2-node 4-core VM Clusters"

    def __init__(self, load_percentage, cores_per_vm):
        if not (0 <= load_percentage <= 100):
            raise ValueError("load_percentage must be between 0 and 100")
        if cores_per_vm not in [4, 8, 12]:
            raise ValueError("cores_per_vm must be either 4 or 8 or 12")
        self.load_percentage = load_percentage
        self.cores_per_vm = cores_per_vm

    @classmethod
    def inputs_for_2n4c(cls):
        print("Pls enter the inputs for 2 node 4 core VM Cluster as prompted")
        load_percentage = int(input("Enter load percentage: "))
        cores_per_vm = 4
        return cls(load_percentage, cores_per_vm)

    @classmethod
    def inputs_for_2n8c(cls):
        print("Pls enter the inputs for 2 node 8 core VM Cluster as prompted")
        load_percentage = int(input("Enter load percentage: "))
        cores_per_vm = 8
        return cls(load_percentage, cores_per_vm)

    def get_json(self):
        scenario1_2 = {
            "description": self.description1_2,
            "loadPercentage": self.load_percentage,
            "nodesPerVmCluster": self.nodes_per_vm_cluster,
            "coresPerVm": self.cores_per_vm
        }
        scenario1_3 = {
            "description": self.description1_3,
            "loadPercentage": self.load_percentage,
            "nodesPerVmCluster": self.nodes_per_vm_cluster,
            "coresPerVm": self.cores_per_vm
        }
        return scenario1_2
        # return scenario1_3


# scenario1_3 = TwoNodeLoadScenario.inputs_for_2n4c()
scenario1_2 = TwoNodeLoadScenario.inputs_for_2n8c()
print(json.dumps(scenario1_3.get_json(), indent=4))
print(json.dumps(scenario1_2.get_json(), indent=4))
