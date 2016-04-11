import sys
import time

sys.path.append('./gen-py')

from rpc import NewsServlet
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

socket = TSocket.TSocket('localhost', 12345)
transport = TTransport.TBufferedTransport(socket)    #缓冲
protocol = TBinaryProtocol.TBinaryProtocol(transport) #协议
client = NewsServlet.Client(protocol)
transport.open()
result = client.get_news_detail()
print result
