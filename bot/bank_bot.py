import uiautomator2 as u2
import time

package = 'mobi.acpm.sslunpinning'
bank = 'Shopee'

class SSLUnpinning:
    def __init__(self):

        self.device_info = {}
        d = u2.connect()
        self.device = d
        self.device_info['ip'] = d.wlan_ip
        self.device_info['device_id'] = d.serial
        self.device_info['accountAlias'] = d.device_info.get('brand', 'jake-device')
        self.device_info['log'] = 'transaction'
        self.device_info['bank'] = ''
        
    def start(self):
        self.device.screen_on()
        self.device.unlock()
        self.device.app_start('mobi.acpm.sslunpinning')
        time.sleep(1)
        status = self.unpin_activity()
        
        return status

    def unpin_activity(self):
        swip = 0
        bank_found = False
        while swip < 15:
            time.sleep(1)
            if self.device(text=f"self.device_info.get('bank', {bank})").exists():
                self.device(text=f"self.device_info.get('bank', {bank})").click()
                bank_found = True
                break
            self.device.swipe_ext('up')
            swip += 1
        return bank_found

    def post_device_to_log(self):
        return self.device_info


def xposed():
    bot = SSLUnpinning()
    response = bot.start()
    return {'msg': response}


def post_device():
    bot = SSLUnpinning()
    return {'data': bot.post_device_to_log()}