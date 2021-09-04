from nodewire import Node

class MyNode(Node):
    def got_count(self, nodename):
        print(counter.count)
        if counter.count == 10 :
            counter.reset = 0

    async def loop(self):
        global counter
        print('connected')
        counter = await self.get_node('pynode')
        counter.start = 1
        counter.on_count = self.got_count

mynode = MyNode(nodename='control', server='localhost')
mynode.nw.run()