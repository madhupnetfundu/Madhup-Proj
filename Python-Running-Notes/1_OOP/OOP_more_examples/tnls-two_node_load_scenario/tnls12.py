import json


class LoadTestScenario:
    def __init__(self, load_percentage, nodes_per_vm_cluster, cores_per_vm, db_setup=None):
        self.load_percentage = load_percentage
        self.nodes_per_vm_cluster = nodes_per_vm_cluster
        self.cores_per_vm = cores_per_vm
        self.db_setup = db_setup

    def get_json(self):
        scenario = {
            "description": f"Example: Create {self.nodes_per_vm_cluster}-node {self.cores_per_vm}-core VM Clusters",
            "loadPercentage": self.load_percentage,
            "nodesPerVmCluster": self.nodes_per_vm_cluster,
            "coresPerVm": self.cores_per_vm
        }
        if self.db_setup == "vault":
            scenario["dbSetup"] = self.db_setup
        return scenario


print("Scenario 1: 2n4c_dbvlt")
load_percentage_1 = int(input("Enter load percentage for scenario 1: "))
nodes_per_vm_cluster_1 = int(
    input("Enter number of nodes per VM cluster for scenario 1: "))
cores_per_vm_1 = int(input("Enter number of cores per VM for scenario 1: "))

print("\nScenario 2: 2n8c")
load_percentage_2 = int(input("Enter load percentage for scenario 2: "))
nodes_per_vm_cluster_2 = int(
    input("Enter number of nodes per VM cluster for scenario 2: "))
cores_per_vm_2 = int(input("Enter number of cores per VM for scenario 2: "))

print("\nScenario 3: 2n4c")
load_percentage_3 = int(input("Enter load percentage for scenario 3: "))
nodes_per_vm_cluster_3 = int(
    input("Enter number of nodes per VM cluster for scenario 3: "))
cores_per_vm_3 = int(input("Enter number of cores per VM for scenario 3: "))

scenario_2n4c_dbvlt = LoadTestScenario(
    load_percentage_1, nodes_per_vm_cluster_1, cores_per_vm_1, db_setup="vault")

scenario_2n8c = LoadTestScenario(
    load_percentage_2, nodes_per_vm_cluster_2, cores_per_vm_2)

scenario_2n4c = LoadTestScenario(
    load_percentage_3, nodes_per_vm_cluster_3, cores_per_vm_3)

scenario_list = [scenario_2n4c_dbvlt, scenario_2n8c, scenario_2n4c]
scenario_json_list = [scenario.get_json() for scenario in scenario_list]

print(json.dumps(scenario_json_list, indent=4))