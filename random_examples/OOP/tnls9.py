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


load_percentage_1 = 25
nodes_per_vm_cluster_1 = 2
cores_per_vm_1 = 4

load_percentage_2 = 25
nodes_per_vm_cluster_2 = 2
cores_per_vm_2 = 8

load_percentage_3 = 50
nodes_per_vm_cluster_3 = 2
cores_per_vm_3 = 4

scenario_1 = LoadTestScenario("Example: Create 2-node 4-core DB on Vault",
                              load_percentage_1, nodes_per_vm_cluster_1, cores_per_vm_1, db_setup="vault")
scenario_2 = LoadTestScenario("Example: Create 2-node 8-core VM Clusters",
                              load_percentage_2, nodes_per_vm_cluster_2, cores_per_vm_2)
scenario_3 = LoadTestScenario("Example: Create 2-node 4-core VM Clusters",
                              load_percentage_3, nodes_per_vm_cluster_3, cores_per_vm_3)

scenarios = [scenario_1.get_json(), scenario_2.get_json(),
             scenario_3.get_json()]

with open("2-node-load-scenario.json", "w") as f:
    json.dump(scenarios, f, indent=4)
