# import json
# blackjack_hand = (8, "Q")
# print(type(blackjack_hand))
# encoded_hand = json.dumps(blackjack_hand)
# print(type(encoded_hand))
# print (encoded_hand)
# # print(type(blackjack_hand))
# # decoded_hand = json.loads(encoded_hand)
# # print(type(decoded_hand))

a={
  "vmClusterId": "ocid1.exascalevmcluster.oc1.iad.anuwcljrj43zu2iazmvyijfsfvfwbctj67rpiq5codverughqamjrty72cta",
  "operation": "create",
  "status": "success",
  "hostNamePrefix": "tay",
  "vmCount": 2,
  "parentCompute": [
    "iad103312exscs05.iad103312exs.adminintlsn.oraclevcn.com",
    "iad103312exscs06.iad103312exs.adminintlsn.oraclevcn.com"
  ],
  "fetchServerDetails": 3,
  "networkPreparation": 189,
  "vmClusterConfiguration": 1806,
  "deletePrivateEndpoint": 101,
  "archiveLogs": 1,
  "vmclusterca": 2118,
  "prepareOeda": 16.826,
  "acquireLocks": 0.503,
  "createVms": 596.59,
  "createOsUsers": 10.827,
  "setupCellConnectivity": 13.495,
  "configureExascaleOnCompute": 27.359,
  "installGiCluster": 79.766,
  "initGiCluster": 795.66,
  "installDb": 141.788,
  "relinkDb": 63.882,
  "collectAllVmsDiag": 3.461,
  "raw": {
    "fetchServerDetailsStart": "2022-10-31T16:41:06Z",
    "fetchServerDetailsEnd": "2022-10-31T16:41:09Z",
    "networkPreparationStart": "2022-10-31T16:41:10Z",
    "networkPreparationEnd": "2022-10-31T16:44:19Z",
    "vmClusterConfigurationStart": "2022-10-31T16:44:19Z",
    "vmClusterConfigurationEnd": "2022-10-31T17:14:25Z",
    "deletePrivateEndpointStart": "2022-10-31T17:14:25Z",
    "deletePrivateEndpointEnd": "2022-10-31T17:16:06Z",
    "archiveLogsStart": "2022-10-31T17:16:11Z",
    "archiveLogsEnd": "2022-10-31T17:16:12Z",
    "vmclustercaStart": "2022-10-31T16:40:54Z",
    "vmclustercaEnd": "2022-10-31T17:16:12Z",
    "prepareOedaStart": "2022-10-31T16:44:44Z",
    "prepareOedaEnd": "2022-10-31T16:45:01Z",
    "acquireLocksStart": "2022-10-31T16:45:02Z",
    "acquireLocksEnd": "2022-10-31T16:45:02Z",
    "createVmsStart": "2022-10-31T16:45:02Z",
    "createVmsEnd": "2022-10-31T16:54:59Z",
    "createOsUsersStart": "2022-10-31T16:55:05Z",
    "createOsUsersEnd": "2022-10-31T16:55:16Z",
    "setupCellConnectivityStart": "2022-10-31T16:55:16Z",
    "setupCellConnectivityEnd": "2022-10-31T16:55:29Z",
    "configureExascaleOnComputeStart": "2022-10-31T16:55:29Z",
    "configureExascaleOnComputeEnd": "2022-10-31T16:55:56Z",
    "installGiClusterStart": "2022-10-31T16:55:56Z",
    "installGiClusterEnd": "2022-10-31T16:57:16Z",
    "initGiClusterStart": "2022-10-31T16:57:16Z",
    "initGiClusterEnd": "2022-10-31T17:10:32Z",
    "installDbStart": "2022-10-31T17:10:32Z",
    "installDbEnd": "2022-10-31T17:12:54Z",
    "relinkDbStart": "2022-10-31T17:12:54Z",
    "relinkDbEnd": "2022-10-31T17:13:58Z",
    "collectAllVmsDiagStart": "2022-10-31T17:13:58Z",
    "collectAllVmsDiagEnd": "2022-10-31T17:14:01Z"
  }
}
# print(type(a))
# print (a['raw'])

b=a['raw']
print (type(b))
# print (b)
print(b.get('fetchServerDetailsStart')) ## prints the value of the corresponding key.
