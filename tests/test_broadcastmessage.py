import asynctest
from asynctest.mock import patch


class TestBroadcastMessage(asynctest.TestCase):

    def setUp(self):
        patcher1 = patch('charlesbot_broadcast_message.broadcastmessage.BroadcastMessage.load_config')  # NOQA
        self.addCleanup(patcher1.stop)
        self.mock_load_config = patcher1.start()

        from charlesbot_broadcast_message.broadcastmessage import BroadcastMessage
        test_plug = BroadcastMessage()  # NOQA

    def tearDown(self):
        pass

    @asynctest.ignore_loop
    def test_something(self):
        pass
