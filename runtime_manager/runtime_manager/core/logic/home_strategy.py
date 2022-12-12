from .strategy import Strategy
from ...utility.file_reader import File_Reader
from ...utility.request_maker import Request_Maker
from ...utility.paths import Paths
import json

class Home_Strategy(Strategy):
    
    def do_algorithm(self,  id_flow, payload):
        print("[Home_Strategy] - performing the algorithm at home")

        components = json.loads(File_Reader.read_file(Paths.COMPONENTS.value))

        flows = File_Reader.read_file(Paths.FLOWS.value)
        flows = flows.split("\n\n")

        flow = None
        for f in flows:
            if f[0] == str(id_flow):
                flow = f

        if flow:
            flow = flow.splitlines()
            del flow[0]
            results = []
            results.append("")
            for instruction in flow:
                instruction = instruction.split(" ")
                print(instruction)
                if instruction[0] == "TO":
                    del instruction[0]
                    for i in instruction:
                        print(i)
                        if i[0:3] == "com":
                            component_id = i[-1]
                        elif i[0:3] == "end":
                            endpoint_id = i[-1]
                        else:
                            print("[Home_Strategy] - Istruction "+i+" not recognized")

                    #   REST configuration
                    protocol = components[str(component_id)]["config"]["protocol"]
                    host = components[str(component_id)]["config"]["ip"]
                    port = components[str(component_id)]["config"]["port"]
                    endpoint = components[str(component_id)]["config"]["endpoints"][str(endpoint_id)]

                elif instruction[0] == "GET":
                    try:
                        results.append(Request_Maker.make_request(protocol, host, port, endpoint))
                    except TypeError:
                        print("[Home_Strategy] - Missing information, unable to perform GET request")
                elif instruction[0] == "POST":
                    try:
                        to_post = []
                        del instruction[0]
                        for i in instruction:
                            if i[0:3] == "res":
                                try:
                                    result_id = int(i[-1])
                                    to_post.append(results[result_id])
                                except IndexError:
                                    print("[Home_Strategy] - Istruction "+i+" does not exist")
                            elif i[0:3] == "pay":
                                to_post.append(payload)
                            else:
                                print("[Home_Strategy] - Istruction "+i+" not recognized")
                                continue
                        try:
                            to_post_json = str({"payload":to_post})
                            results.append(Request_Maker.make_request(protocol, host, port, endpoint, to_post_json))
                        except UnboundLocalError:
                            raise TypeError
                    except TypeError:
                        print("[Home_Strategy] - Missing information, unable to perform POST request")
                elif instruction[0][0] == "#":
                    pass
                else:
                    print("[Home_Strategy] - Istruction "+instruction[0]+" not recognized")
        else:
            print("[Home_Strategy] - ID not valid")

