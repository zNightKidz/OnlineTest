import requests
import unittest



class MyTest(unittest.TestCase):
    '''接口名称：获取站点信息'''

    def setUp(self):
        print("start test!")
        pass
    def tearDown(self):
        print("end test!")
        pass

class test_allFacility_get(MyTest):
    def test_allFacility_get(self):
        self.url = 'http://140.143.191.187:38097/multimedia/platform/api/v1/facility/all'
        self.response = requests.get(self.url)
        self.strAllFacility = '''[{"facilityId":2,"name":"Beijing-AG1","building":""},{"facilityId":3,"name":"Beijing-AG2","building":""},{"facilityId":4,"name":"Beijing-BB1","building":""},{"facilityId":5,"name":"Beijing-BB2","building":""},{"facilityId":30,"name":"CCTV","building":null},{"facilityId":23,"name":"ChangSha-BB","building":null},{"facilityId":24,"name":"ChangSha-User","building":null},{"facilityId":6,"name":"ChengDu-BB","building":""},{"facilityId":7,"name":"FuZhou-BB","building":""},{"facilityId":8,"name":"GuangZhou-BB","building":""},{"facilityId":26,"name":"HangZhou-BB","building":null},{"facilityId":25,"name":"HangZhou-User","building":null},{"facilityId":15,"name":"HongKong-BB","building":""},{"facilityId":16,"name":"London-BB","building":""},{"facilityId":17,"name":"LosAngeles-BB","building":""},{"facilityId":27,"name":"Mobile-1","building":null},{"facilityId":28,"name":"Mobile-2","building":null},{"facilityId":21,"name":"NewYork-BB","building":null},{"facilityId":29,"name":"Satellite","building":null},{"facilityId":9,"name":"ShangHai-BB","building":""},{"facilityId":10,"name":"ShenYang-BB","building":""},{"facilityId":22,"name":"Sydney-BB","building":null},{"facilityId":11,"name":"TianJin-BB","building":""},{"facilityId":12,"name":"TianJin-User","building":""},{"facilityId":18,"name":"Tokyo-BB","building":""},{"facilityId":19,"name":"Urumchi-BB","building":null},{"facilityId":20,"name":"Urumchi-User","building":null},{"facilityId":13,"name":"WuHan-BB","building":""},{"facilityId":14,"name":"XiAn-BB","building":""}]'''
        print("response.text返回值：",self.response.text)
        print("response.status_code值：", self.response.status_code)
        self.foo = self.response.text.find(self.strAllFacility)
        print("起始位置为：", self.foo)
        self.assertNotEqual(self.foo,-1)

    def test_1(self):
        self.assertEqual(1,1)
    def test_2(self):
        self.assertNotEqual(1,2)


