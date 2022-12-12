from .strategy import Strategy
from ...utility.file_reader import File_Reader
from ...utility.request_maker import Request_Maker
from ...utility.paths import Paths
import json

class LB_Strategy(Strategy):

    def do_algorithm(self, id, received_info):
        print("[LB_Strategy] - performing the algorithm on a different node")

        received_info.is_load_balancing = True
        node_payload = json.dumps(received_info.__dict__)
        print("[LB_Strategy] - Sending node_payload:", node_payload, "to node with ID", id)

        nodes = json.loads(File_Reader.read_file(Paths.NODES.value))

        response = Request_Maker.make_request(nodes[id]["config"]["protocol"], 
                                                nodes[id]["config"]["ip"], 
                                                nodes[id]["config"]["port"], 
                                                nodes[id]["config"]["endpoint"], node_payload)

        print("[LB_Strategy] - response from node " + id + " is \n\n" + response)
    



#   TODO how to manage failed connections with the node(?)
#        err = 0
#        while err <= 2:
#            try:
#                print("Trying post to "+url_post)
#                r = requests.post(url_post, payload)
#                print(r.text)
#                print("Done!")
#                break
#            except requests.exceptions.ConnectionError:
#                print("Connection error.")
#                err = err + 1
#            except KeyboardInterrupt:
#                break
#        if err == 3:
#            print("Reached max number of attempts.")
