D_SCORE = -2
MATCH_SCORE = 1
NOT_MATCH_SCORE = -1


class PairwiseAlignment:

    list1 = ""
    list2 = ""
    # gcgctaatggcatg
    # gccctaagcgcatt

    def input_lists(self):
        self.list1 = input("配列１ >> ")
        self.list2 = input("配列２ >> ")

    def init_matrix(self):
        score = []
        for j in range(len(self.list2) + 1):
            h_list = []
            if j == 0:
                for i in range(len(self.list1) + 1):
                    h_list.append(D_SCORE*i)
            else:
                h_list.append(D_SCORE*j)
                for i in range(len(self.list1)):
                    h_list.append(0)
            score.append(h_list)
        return score

    def get_matrix(self, score):
        for i in range(1, len(self.list1) + 1):
            for j in range(1, len(self.list2) + 1):
                w = MATCH_SCORE if self.list1[i-1] == self.list2[j-1] else NOT_MATCH_SCORE
                s1 = score[j-1][i-1] + w
                s2 = score[j-1][i] + D_SCORE
                s3 = score[j][i-1] + D_SCORE
                score[j][i] = max(s1, s2, s3)
        return score

    def get_alignment(self, score):
        align1 = ""
        align2 = ""
        i = len(self.list1)
        j = len(self.list2)
        while i != 0 and j != 0:
            w = MATCH_SCORE if self.list1[i - 1] == self.list2[j - 1] else NOT_MATCH_SCORE
            if score[j][i] == score[j-1][i-1] + w:
                i = i - 1
                j = j - 1
                align1 = self.list1[i] + align1
                align2 = self.list2[j] + align2
            elif score[j][i] == score[j-1][i] + D_SCORE:
                j = j - 1
                align1 = "-" + align1
                align2 = self.list2[j] + align2
            elif score[j][i] == score[j][i-1] + D_SCORE:
                i = i - 1
                align1 = self.list1[i] + align1
                align2 = "-" + align2
        return align1, align2

    def output_score(self, score):
        for j in range(len(self.list2)):
            print(score[j])
        print("score: " + str(score[len(self.list2)][len(self.list2)]))


def main():
    pa = PairwiseAlignment()
    pa.input_lists()
    score = pa.init_matrix()
    score = pa.get_matrix(score)
    aligns = pa.get_alignment(score)
    print(aligns[0])
    print(aligns[1])
    pa.output_score(score)


if __name__ == '__main__':
    main()
