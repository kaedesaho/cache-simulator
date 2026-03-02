class Process:
    def __init__(self, pid, num_reads, pages, state):
        self.pid = pid
        self.num_reads = num_reads
        self.page_table = pages
        self.state = state

    def get_pid(self):
        return self.pid

    def get_num_reads(self):
        return self.num_reads

    def get_page_table(self):
        return self.page_table

    def get_state(self):
        return self.state

    def set_page_table(self, pages):
        self.page_table = pages

    def set_state(self, state):
        self.state = state
