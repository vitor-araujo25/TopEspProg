#Team Queue
class Node:
    def __init__(self, previous, next_node, element):
        self.previous = previous
        self.next = next_node
        self.element = element

class Element:
    def __init__(self, team, value):
        self.team = team
        self.value = value

    ##DEBUG
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        string = f"{{t: {self.team}, v:{self.value}}}"
        return string
    ##DEBUG


class TeamQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        self.teams_positions = dict()
    
    def __len__(self):
        return self.len

    def enqueue(self, element):
        if self.len == 0:
            new_node = Node(previous=None, next_node=None, element=element)
            self.head = new_node
            self.tail = new_node
        elif element.team in self.teams_positions:
            teammate = self.teams_positions[element.team]
            new_node = Node(previous=teammate.previous, next_node=teammate, element=element)
            if teammate.previous:
                teammate.previous.next = new_node
            else:
                self.tail = new_node
            teammate.previous = new_node
        else: #sem amigos na fila     
            new_node = Node(previous=None, next_node=self.tail, element=element)
            if self.tail:
                self.tail.previous = new_node
            self.tail = new_node
        self.len += 1
        self.teams_positions[element.team] = new_node
    
    def dequeue(self):
        if self.len != 0:
            dequeued_node = self.head
            self.head = dequeued_node.previous
            self.len -= 1
            print(dequeued_node.element.value)
            if self.head:
                self.head.next = None
                if self.head.element.team != dequeued_node.element.team:
                    del self.teams_positions[dequeued_node.element.team]
                elif self.teams_positions[self.head.element.team].element == dequeued_node.element:
                    self.teams_positions[self.head.element.team] = self.head
            else:
                del self.teams_positions[dequeued_node.element.team]
                self.tail = None      

    ##DEBUG
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        string = f"{self.len}: "
        ptr = self.tail
        while ptr is not None:
            string += f"{ptr.element.value} -> "
            ptr = ptr.next
        string += "//"
        return string
    ##DEBUG

def main():
    case_count = 1
    debug = False
    while True:
        teams_qnt = int(input())
        if teams_qnt == 0:
            break
        teams_dict = dict()
        for i in range(teams_qnt):
            team = input().strip().split(" ")[1:]
            teams_dict.update({t:i for t in team})
        queue = TeamQueue()
        command = input().strip().split(" ")
        print("Scenario #{}".format(case_count))
        while command[0] != "STOP":
            if command[0] == "ENQUEUE":
                # if command[1] == '23':
                #     debug = True
                # if debug:
                #     import pdb; pdb.set_trace()
                value = command[1]
                elem = Element(value=value, team=teams_dict[value])
                # print(elem)
                queue.enqueue(elem)
            elif command[0] == "DEQUEUE":
                queue.dequeue()
            # print(queue)
            command = input().strip().split(" ")
        print()
        case_count += 1

if __name__ == "__main__":
    main()

        

    
