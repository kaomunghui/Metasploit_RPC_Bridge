import nmap


# return掃描子網下狀態是up的主機
def nmap_ip_scan(net):
    nm = nmap.PortScanner()
    # -sn查在線主機
    res_scan = nm.scan(hosts=net, arguments="-sn -PE -n")
    print("nmap command line :" + res_scan["nmap"]["command_line"])
    host_list = []
    # print(res_scan["scan"])
    for ip in res_scan["scan"]:
        try:
            if res_scan["scan"][ip]["status"]["state"] == "up":
                IP = res_scan["scan"][ip]["addresses"]["ipv4"]
                host_list.append(IP)
        except Exception as e:
            print("Eorr:", e)
            pass
    return host_list


# 對存活主機掃描指定port資訊
def nmap_port_scan(host, port):
    nm = nmap.PortScanner()
    host_port_os = []
    for ip in host:
        # -A偵測主機作業系統與各服務版本 -O作業系統資訊
        res_scan = nm.scan(hosts=ip, ports=port, arguments=" -A -O")
        print("nmap command line:" + res_scan["nmap"]["command_line"])
        #print(res_scan["scan"])
        # 所有各自ip主機資訊
        for ip in res_scan["scan"]:
            host_dic = {ip: {"tcp_port": {}, "os": []}}
            try:
                # tcp port 各自服務的名稱、版本資訊
                for p in res_scan["scan"][ip]["tcp"]:
                    host_dic[ip]["tcp_port"][p] = {}
                    host_dic[ip]["tcp_port"][p]["name"] = res_scan["scan"][ip]["tcp"][p]["name"]
                    host_dic[ip]["tcp_port"][p]["version"] = res_scan["scan"][ip]["tcp"][p]["version"]
                # 主機作業系統資訊
                host_dic[ip]["os"].append(res_scan["scan"][ip]["osmatch"][0]["name"])
                host_port_os.append(host_dic)
            except Exception as e:
                print("Eorr:", e)
                pass
    return host_port_os