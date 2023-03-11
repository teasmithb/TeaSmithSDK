#!/usr/bin/env python


from unittest import main, TestCase


from subprocess import Popen, PIPE


class TestProcess(TestCase):

    def test01(self):
        '''
        tests all movies
        '''
        p = Popen(["python3", "movies_api.py","915sul6Ogp3nJurtu49K"], stdout=PIPE,cwd="../")
        stdout, _ = p.communicate()
        print ("todo-verify object returned is valid")
    def test02(self):
        #tests specified movie id and no quote 
        p = Popen(["python3", "movies_api.py","915sul6Ogp3nJurtu49K",], stdout=PIPE,cwd="../")
        stdout, _ = p.communicate()
        print (stdout)
        print ("todo-verify object returned is valid")
        #self.assertEquals(stdout, b"Hello World!\n")

    def test03(self):
        # tests specified movie id with quote 
        print ("python3", "../movies_api.py","915sul6Ogp3nJurtu49K","5cd95395de30eff6ebccde56","--quote")
        p = Popen(["python3", "movies_api.py","915sul6Ogp3nJurtu49K"], stdout=PIPE,cwd="../")
        stdout, _ = p.communicate()
        print (stdout)
        print ("todo-verify object returned is valid")
        #self.assertEquals(stdout, b"Hello World!\n")
    def test04(self):
        # call the python script and not provide token or with empty token, it should fail 
        p = Popen(["python3", "movies_api.py",""], stdout=PIPE,cwd="../")
        stdout, _ = p.communicate()
        print (stdout)
        print ("todo-verify object returned is valid")
        #self.assertEquals(stdout, b"Hello World!\n")


if __name__ == "__main__":
    main()


