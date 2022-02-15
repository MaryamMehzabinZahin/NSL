# SRP SOC
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        # return str(self.entries)
        return 'tt'.join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I cried.')
j.add_entry('I have read a book.')
print(f'journal entries:\n{j}')

file = r'C:\Users\NSL\Desktop\nsl\notes5.txt'
#PersistenceManager.save_to_file(j, file)
#
# with open(file) as fh:
#     print(fh.read())

