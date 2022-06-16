from pymetasploit3.msfrpc import MsfRpcClient

def smb_attack(host):
    client = MsfRpcClient(username="msf", password="123", server="127.0.0.1", port=55552)
    print("client:", client)

    # 使用metasploit攻擊模組，路徑
    exploit = client.modules.use('auxiliary', 'scanner/smb/smb_ms17_010')
    # print("option:", exploit.options)     # 模組可使用配置項目
    exploit["RHOSTS"] = host
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
    result = console.run_module_with_output(exploit, payload='scanner/smb/smb_ms17_010')
    print("result:", result)

    if mysession:
        return True
    else:
        return False