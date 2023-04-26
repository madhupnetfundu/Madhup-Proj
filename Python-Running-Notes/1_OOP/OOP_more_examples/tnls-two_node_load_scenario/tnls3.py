import json

class TwoNodeLoadScenario:
    nodes_per_vm_cluster = 2
    description2n_4c_db = "Example: Create 2-node 4-core dbonvault VM Clusters"
    description2n_8c = "Example: Create 2-node 8-core VM Clusters"
    description2n_4c = "Example: Create 2-node 4-core VM Clusters"

    def __init__(self, load_percentage, cores_per_vm):
        self.load_percentage = load_percentage
        self.cores_per_vm = cores_per_vm

    def get_json(self):
        scenario1_1 = {
            "description": self.description1_3,
            "loadPercentage": self.load_percentage,
            "coresPerVm": self.cores_per_vm
        }
        return scenario1_1


a = TwoNodeLoadScenario(25, 4)
print(json.dumps(a.get_json(), indent=4))
