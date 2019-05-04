class Solution:
    def compareEmails(self, email1: str, email2: str) -> bool:
        if len(email1) != len(email2):
            return False
        for j in range(len(email1)):
            if email1[j] != email2[j]:
                return False
        return True

    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            # Convert str to list
            currEmail = []
            for j in range(len(emails[i])):
                currEmail.append(emails[i][j])
            
            # Normalize local name
            index = 0
            isFirstPlusSign = True
            while currEmail[index] != '@':
                if currEmail[index] == '.':
                    currEmail.pop(index)
                elif currEmail[index] == '+':
                    while currEmail[index] != '@':
                        currEmail.pop(index)
                else:
                    index = index + 1

            emails[i] = currEmail
        print([''.join(emails[i]) for i in range(len(emails))])
        
        emails.sort()
        index = 0
        while index < len(emails) - 1:
            isSimilar = self.compareEmails(emails[index], emails[index + 1])
            if isSimilar:
                emails.pop(index)
            else:
                index = index + 1
        print([''.join(emails[i]) for i in range(len(emails))])

        numUniqueEmails = len(emails)

        return numUniqueEmails
