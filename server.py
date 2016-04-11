import sys
import time
sys.path.append('./gen-py')

from rpc import NewsServlet
from rpc.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class NewsHandler:
    def __init__(self):
        pass

    def get_news_detail(self):
        print "client call %s" %(self.__class__.__name__)
        return NewsDetail(1, "title", "content", "news", str(time.time()))

    def get_news_list(self):
        pass



handler = NewsHandler()
processor = NewsServlet.Processor(handler)
transport = TSocket.TServerSocket(port=12345)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

server.serve()
