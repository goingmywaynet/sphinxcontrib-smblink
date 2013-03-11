# _*_ coding: utf-8; _*_

import smblink
import unittest,urllib

verboseMode = True   # print out test case details

def testText():
  string = r'\\hoge\new\to\path'
  print smblink.convertToWSLStyle(string)

  string = r'\\日本語 #%^~{}[];@=&$ほげほげ\ふがふが'
  print smblink.convertToWSLStyle(string)

  string = r':smblink:`this is link     <\\日本語 #%^~{}[];@=&$ほげほげ\ふがふが>`'
  print smblink.convertToWSLStyle(string)

class TestSequenceFunctions(unittest.TestCase): #unittest.TestCaseのサブクラスとしてテストケース作成

  def setUp(self):
    if verboseMode : print "\n"

  def test_convertToWSLStyle_simpleStr(self):
    chkList = [
        # [ input , output ]
        [r'\\hoge\new\to\path',r'<a href="file://hoge/new/to/path">\\hoge\new\to\path</a>'],
        [r'\\path',r'<a href="file://path">\\path</a>']
      ]
    for chk in chkList:
      self.assertEqual( chk[1], smblink.convertToWSLStyle( chk[0] ) )
      if verboseMode : print " Input  : "+chk[0]+"\n Assert : "+chk[1] + "\n ---- "

  def test_convertToWSLStyle_multibyteStr(self):
    chkList = [
        # [ input , output ]
        [r'\\日本語ほげほげ',r'<a href="file://日本語ほげほげ">\\日本語ほげほげ</a>'],
      ]
    for chk in chkList:
      self.assertEqual( chk[1], smblink.convertToWSLStyle( chk[0] ) )
      if verboseMode : print " Input  : "+chk[0]+"\n Assert : "+chk[1] + "\n ---- "

  def test_smblink_role(self):
    chkList = [
        # [ input , output ]
        [r':smblink:`\\path`', r'<a href="file://path">\\path</a>']
        ,[r':smblink:`\\日本語ほげほげ`',r'<a href="file://日本語ほげほげ">\\日本語ほげほげ</a>'] 
      ]
    for chk in chkList:
      print smblink.smblink_role('', chk[0], '','','','')[0][0].astext()
      self.assertEqual( chk[1] , 
          #smblink.smblink_role("smblink", rawtext, chk[0],'','','')[0][0].astext().encode('utf-8') )
          smblink.smblink_role("smblink", chk[0], '','','','')[0][0].astext() )
      if verboseMode : print " Input  : "+chk[0]+"\n Assert : "+chk[1] + "\n ---- "


if __name__ == '__main__':
  unittest.main(verbosity=2)
