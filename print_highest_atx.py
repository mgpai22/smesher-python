import api

node_ip = "localhost:9092" # set ip

client = api.ActivationClient(node_ip)
print(client.get_highest_atx_id())