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
    def inputs_for_2n4c_db(cls):
        print("Pls enter the inputs for 2 node 4 core dbonvault VM Cluster as prompted")
        load_percentage = int(input("Enter load percentage for 2n4c_db on vault: "))
        cores_per_vm = 4
        dbonvault=True
        return cls(load_percentage, dbonvault, cores_per_vm)

    @classmethod
    def inputs_for_2n8c(cls):
        print("Pls enter the inputs for 2 node 8 core VM Cluster as prompted")
        load_percentage = int(input("Enter load percentage for 2n8c : "))
        cores_per_vm = 8
        return cls(load_percentage, cores_per_vm)

    @classmethod
    def inputs_for_2n4c(cls):
        print("Pls enter the inputs for 2 node 4 core VM Cluster as prompted")
        load_percentage = int(input("Enter load percentage 2n4c: "))
        cores_per_vm = 4
        return cls(load_percentage, cores_per_vm)

    def get_json(self):
        scenario = {
            "description": self.description1_1,
            "loadPercentage": self.load_percentage,
            "nodesPerVmCluster": self.nodes_per_vm_cluster,
            "coresPerVm": self.cores_per_vm
        }
        return scenario
    

a = TwoNodeLoadScenario.inputs_for_2n4c_db()
print(json.dumps(a.get_json(), indent=4))

    # def get_json(self):
    #     scenario = {
    #         "description": self.description1_2,
    #         "loadPercentage": self.load_percentage,
    #         "nodesPerVmCluster": self.nodes_per_vm_cluster,
    #         "coresPerVm": self.cores_per_vm
    #     }
    #     return scenario

# def generate_load_test():
#     scenario1_2 = TwoNodeLoadScenario.inputs_for_2n8c()
#     scenario1_3 = TwoNodeLoadScenario.inputs_for_2n4c()

#     load_test = {
#         "scenarios": [
#             {
#                 "name": "Scenario 1.2",
#                 "description": scenario1_2.description1_2,
#                 "request": {
#                     "method": "GET",
#                     "url": "/cluster",
#                     "params": {
#                         "loadPercentage": scenario1_2.load_percentage,
#                         "nodesPerVmCluster": scenario1_2.nodes_per_vm_cluster,
#                         "coresPerVm": scenario1_2.cores_per_vm
#                     }
#                 }
#             },
#             {
#                 "name": "Scenario 1.3",
#                 "description": scenario1_3.description1_3,
#                 "request": {
#                     "method": "GET",
#                     "url": "/cluster",
#                     "params": {
#                         "loadPercentage": scenario1_3.load_percentage,
#                         "nodesPerVmCluster": scenario1_3.nodes_per_vm_cluster,
#                         "coresPerVm": scenario1_3.cores_per_vm
#                     }
#                 }
#             }
#         ]
#     }

#     return json.dumps(load_test, indent=4)
