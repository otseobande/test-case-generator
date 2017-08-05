class State(object):
	def __init__(self,state_item):
		self.state_item = state_item

	@property
	def name(self):
		return self.state_item.getAttribute('name')

	@property
	def id(self):
		return self.state_item.getAttribute('xmi.id')

	@property	
	def incoming(self):
		incoming_element = self.state_item.getElementsByTagName("UML:StateVertex.incoming")

		if len(incoming_element) == 0:
			return None
		elif len(incoming_element) >= 1:
			incoming_id_list = []
			incoming_node = incoming_element[0]
			incoming_transition = incoming_node.getElementsByTagName("UML:Transition")

			for i in range(len(incoming_transition)):
				incoming_id_list.append(incoming_transition[i].getAttribute("xmi.idref"))

			return incoming_id_list

	@property
	def outgoing(self):
		outgoing_element = self.state_item.getElementsByTagName("UML:StateVertex.outgoing")

		if len(outgoing_element) == 0:
			return None
		elif len(outgoing_element) >= 1:
			outgoing_id_list = []
			outgoing_node = outgoing_element[0]
			outgoing_transition = outgoing_node.getElementsByTagName("UML:Transition")

			for i in range(len(outgoing_transition)):
				outgoing_id_list.append(outgoing_transition[i].getAttribute("xmi.idref"))

			return outgoing_id_list

	@property
	def kind(self):
		return self.state_item.getAttribute("kind")

	@property
	def type(self):
		return self.state_item.tagName.strip("UML:")