import json


class LoadTestScenario:
    def __init__(self, description, load_percentage, nodes_per_vm_cluster, cores_per_vm, db_setup=None):
        self.description = description
        self.load_percentage = load_percentage
        self.nodes_per_vm_cluster = nodes_per_vm_cluster
        self.cores_per_vm = cores_per_vm
        self.db_setup = db_setup

    def get_json(self):
        scenario = {
            "description": self.description,
            "loadPercentage": self.load_percentage,
            "nodesPerVmCluster": self.nodes_per_vm_cluster,
            "coresPerVm": self.cores_per_vm
        }
        if self.db_setup == "vault":
            scenario["dbSetup"] = self.db_setup
        return scenario


load_percentage = int(input("Enter load percentage for scenario 1: "))
nodes_per_vm_cluster = int(
    input("Enter number of nodes per VM cluster for scenario 1: "))
cores_per_vm = int(input("Enter number of cores per VM for scenario 1: "))

scenario_2n4c_dbvlt = LoadTestScenario(
    "Example: Create 2-node 4-core DB on Vault", load_percentage, nodes_per_vm_cluster, cores_per_vm, db_setup="vault")

load_percentage = int(input("Enter load percentage for scenario 2: "))
nodes_per_vm_cluster = int(
    input("Enter number of nodes per VM cluster for scenario 2: "))
cores_per_vm = int(input("Enter number of cores per VM for scenario 2: "))

scenario_2n8c = LoadTestScenario(
    "Example: Create 2-node 8-core VM Clusters", load_percentage, nodes_per_vm_cluster, cores_per_vm)

load_percentage = int(input("Enter load percentage for scenario 3: "))
nodes_per_vm_cluster = int(
    input("Enter number of nodes per VM cluster for scenario 3: "))
cores_per_vm = int(input("Enter number of cores per VM for scenario 3: "))

scenario_2n4c = LoadTestScenario(
    "Example: Create 2-node 4-core VM Clusters", load_percentage, nodes_per_vm_cluster, cores_per_vm)

scenarios = [scenario_2n4c_dbvlt.get_json(), scenario_2n8c.get_json(),
             scenario_2n4c.get_json()]

print(json.dumps(scenarios, indent=4))
