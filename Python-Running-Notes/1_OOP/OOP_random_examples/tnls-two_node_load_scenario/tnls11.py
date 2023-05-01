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


load_percentage_1 = int(input("Enter load percentage for scenario 1: "))
nodes_per_vm_cluster_1 = int(
    input("Enter number of nodes per VM cluster for scenario 1: "))
cores_per_vm_1 = int(input("Enter number of cores per VM for scenario 1: "))

load_percentage_2 = int(
    input("Enter load percentage for scenario 2 (2n4c_dbvlt): "))
nodes_per_vm_cluster_2 = int(
    input("Enter number of nodes per VM cluster for scenario 2 (2n4c_dbvlt): "))
cores_per_vm_2 = int(
    input("Enter number of cores per VM for scenario 2 (2n4c_dbvlt): "))

load_percentage_3 = int(input("Enter load percentage for scenario 3: "))
nodes_per_vm_cluster_3 = int(
    input("Enter number of nodes per VM cluster for scenario 3: "))
cores_per_vm_3 = int(input("Enter number of cores per VM for scenario 3: "))

scenario_2n4c_dbvlt = LoadTestScenario(
    "Example: Create 2-node 4-core DB on Vault", load_percentage_2, nodes_per_vm_cluster_2, cores_per_vm_2, db_setup="vault")

scenario_2n8c = LoadTestScenario(
    "Example: Create 2-node 8-core VM Clusters", load_percentage_1, nodes_per_vm_cluster_1, cores_per_vm_1)

scenario_2n4c = LoadTestScenario(
    "Example: Create 2-node 4-core VM Clusters", load_percentage_3, nodes_per_vm_cluster_3, cores_per_vm_3)

scenario_list = [scenario_2n4c_dbvlt, scenario_2n8c, scenario_2n4c]

scenario_json_list = [s.get_json() for s in scenario_list]

print(json.dumps(scenario_json_list, indent=4))