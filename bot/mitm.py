from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster

import threading
import asyncio
import time

class Addon(object):
    def __init__(self):
        self.num = 1

    def request(self, flow):
        flow.request.headers["count"] = str(self.num)

    def response(self, flow):
        print(flow.request, '<==== REQUEST')


def loop_in_thread(loop, m):
    asyncio.set_event_loop(loop)
    m.run_loop(loop.run_forever)


if __name__ == "__main__":
    options = Options(listen_host='0.0.0.0', listen_port=8080, http2=True)
    m = DumpMaster(options, with_termlog=False, with_dumper=False)
    config = ProxyConfig(options)
    m.server = ProxyServer(config)
    m.addons.add(Addon())

    loop = asyncio.get_event_loop()
    t = threading.Thread( target=loop_in_thread, args=(loop,m) )
    t.start()
    print('running proxy on port 8080')