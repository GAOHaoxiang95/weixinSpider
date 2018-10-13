import requests
import json
import aiohttp
import asyncio
import time
#http://www.moguproxy.com/
API = "http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=ce0394234fe8403895324a23b9281af3&count=10&expiryDate=0&format=1&newLine=2"

class Agents():

	def __init__(self, testURL):
		self.agentsList = []
		self.fullList = []
		for i in range(0,3):
			self.fullList = self.fullList + self.get_agents()
			time.sleep(5)

	def get_agents(self):#100 agents
		try:
			response = requests.get(API)
			#print(response)
			data = json.loads(response.text)
			agents = data['msg']
			l = []
			print(agents)
			for a in agents:
				#print(a)
				pro = a['ip'] + ':' + a['port']
				l.append(pro)
			return l
		except requests.exceptions.ConnectionError as e:
			print('Error', e.args)
		
		
	async def test_agents(self, testURL, pro):#create valid agents pool
		conn = aiohttp.TCPConnector(verify_ssl=False)
		async with aiohttp.ClientSession(connector=conn) as session:
			try:
				proxy = 'http://' + pro
				print('Testing ', proxy)
				async with session.get(testURL, proxy=proxy, timeout=15) as response:
					if response.status in [200]:
						print(proxy)
						self.agentsList.append(proxy)
					else:
						print('Failed')
			except:
				print('Invalid link')
			
	def saveAsTXT(self):
		f = open('agent.txt', "w", encoding = "utf8")
		for i in self.agentsList:
			f.write(i + '\n')
			
	def get_agentsList(self):
		return self.agentsList

a = Agents("https://weixin.sogou.com/")
loop = asyncio.get_event_loop()
for i in range(0, len(a.fullList), 100):
	test = a.fullList[i:i+100]
	tasks = [a.test_agents("http://httpbin.org/get", p) for p in test]
	loop.run_until_complete(asyncio.wait(tasks))
	time.sleep(5)
a.saveAsTXT()