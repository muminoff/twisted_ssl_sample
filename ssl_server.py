from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol

class Echo(Protocol):
    def dataReceived(self, data):
        """As soon as any data is received, write it back."""
        print 'Wow, we got data from client', data
        self.transport.write(data)

if __name__ == '__main__':
    factory = Factory()
    factory.protocol = Echo
    reactor.listenSSL(8000, factory,
                      ssl.DefaultOpenSSLContextFactory(
            'server.key', 'server.crt'))
    print 'Server is listening on 8000 port...'
    reactor.run()
