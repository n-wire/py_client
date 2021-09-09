import asyncio
from nodewire import Node

class MyNode(Node):
    def on_reset(self, value, sender):
        self.count = value

    def get_status(self, sender):
        return {
            'counting': self.start==1,
            'count': self.count
        }

    async def loop(self):
        print('connected')
        while True:
            await asyncio.sleep(1)
            if self.start==1: 
                self.count = self.count + 1

mynode = MyNode(inputs='start reset', outputs='count status')
mynode.nw.debug = True
mynode.nw.run()