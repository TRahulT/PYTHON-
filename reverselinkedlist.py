def reverse_list(self):
        temp = self.head.next
        prev = self.head
        h = self.head
        while(temp):
            t = temp
            temp = temp.next
            t.next = prev
            h.next = None
            prev = t
        self.head = t