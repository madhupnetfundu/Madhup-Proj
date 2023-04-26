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
        if self.db_setup is not None:
            scenario["dbSetup"] = self.db_setup
        return scenario


a = LoadTestScenario()
