class Solution:
	def defangIPaddr(self, address: str) -> str:
		return address.replace('.', '[.]')

"""
class Solution:
	def defangIPaddr(self, address: str) -> str:
		return "[.]".join(address.split("."))

class Solution:
	def defangIPaddr(self, address: str) -> str:
		ans = []
		for ch in address:
			if ch.isdigit():
				ans.append(ch)
			else:
				ans.append("[.]")

		return "".join(ans)
"""
