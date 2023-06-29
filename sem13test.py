import xml.etree.ElementTree as etree
import unittest
from sem13 import Corpus


class CorpusTest(unittest.TestCase):

    def setUp(self):
        self.corpus = Corpus()
        self.corpus.load('annot.opcorpora.no_ambig.xml')

        tree = etree.parse('annot.opcorpora.no_ambig.xml')
        root = tree.getroot()

        self.test_corpus = []
        for sentence in root.findall('text/paragraphs/paragraph/sentence'):
            sent = sentence.find('source').text
            words = []
            for token in sentence.iter('token'):
                wordform = token.get('text')
                grammems = []
                for i in token.iter('i'):
                    grammems.append(i.attrib['v'])
                word = [wordform, grammems]
                words.append(word)
            sentence = [sent, words]
            self.test_corpus.append(sentence)

    def test_num_sents(self):
        self.assertEqual(len(self.test_corpus), len(self.corpus._sentences))