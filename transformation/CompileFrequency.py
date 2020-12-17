import nltk
import seaborn as sb


class CompileFrequency:

    def calculate_word_freq(self, words):
        sb.set()
        freqdist = nltk.FreqDist(words)
        return freqdist
