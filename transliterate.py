#!/usr/bin/env python3

def lowp(string):
  return string.lower().replace("і","І") # currently only smallcase letters are supported. Need to rework this.

latin2_dict = [
		["ю","йу"],
		["я","йа"],
		["ё","йо"],
		["аа","аъа"],
		["ии","иъи"],
		["уу","уъу"],
		["ф","f"],
		["цц","cc"],
		["цІцІ","ts'ts'"],
		["кІкІ","k'k'"],
		["лълъ","tltl"],
		["лъ","tl"],
		["кІ","k'"],
		["къ","q"],           # possible kq
		["кь","ql"],
		["пІ","p'"],
		["чІ","ch'"],
		["сс","ss"],
		["гь","h"],
		["кк","kk"],
		["чч","chch"],
		["кІ","k'"],          # possible q
		["хІ","h'"],
		["цІ","ts'"],
		["хх","hh"],
		["тІ","t'"],
		["хь","hl"],
		["гІ","gh"],
		["хъ","kh"],
		["гъ","qh"],
		["лл","ll"],
		["ь","й"],
		["б","b"],
		["р","r"],
		["п","p"],
		["л","l"],
		["т","t"],
		["з","z"],
		["ж","zh"],
		["с","s"],
		["м","m"],
		["н","n"],
		["ш","sh"],
		["щ","sch"],
		["к","k"],
		["ч","ch"],
		["ц","c"],
		["в","v"],
		["й","y"],
		["а","a"],
		["х","h"],
		["г","g"],
		["и","i"],
		["е","e"],
		["л","l"],
		["д","d"],
		["о","o"],
		["у","u"],
		["ъ","'"],
		["ы","i"],
		["э","'e"],
		["(",""],         # definatelly wrong place for cutting braces off...
		[")",""]
]

def cyr2latin(string):
  string = lowp(string)
  if string[0] == "е": string="й"+string   # some dirty code
  for k,v in latin2_dict:
    string = string.replace(k,v)
  return string


ajam_dict = [
		["ю","йу"],
		["я","йа"],
		["ё","йо"],
		["э","ъе"],
		["аа","аъа"],
		["ии","иъи"],
		["уу","уъу"],
		["ф","ڣ"],
		["цІцІ","ضّ"],
		["кІкІ","گّ"],
		["лълъ","ڸّ"],
		["чІчІ","ڃّ"],
		["лъ","ڸ"],
		["цІ","ض"],
		["кІ","گ"],
		["къ","ق"],
		["кь","ڨ"],
		["пІ","ڣ"],
		["чІ","ڃ"],
		["сс","سّ"],
		["гь","ه"],
		["кк","كّ"],
		["чч","چّ"],
		["цц","صّ"],
		["кІ","گ"],
		["хІ","ح"],
		["хх","خّ"],
		["тІ","ط"],
		["хь","ڮ"],
		["гІ","ع"],
		["хъ","څ"],
		["гъ","غ"],
		["лл","لّ"],
		["ь","й"],
		["б","ب"],
		["р","ر"],
		["п","ف"],
		["л","ل"],
		["т","ت"],
		["з","ز"],
		["ж","ج"],
		["с","س"],
		["м","م"],
		["н","ن"],
		["ш","ش"],
		["щ","ڜ"],
		["к","ك"],
		["ч","چ"],
		["ц","ص"],
		["в","و"],
		["й","ي"],
		["а","ا"],
		["х","خ"],
		["г","ڬ"],
		["и","ێ"],
		["е","ې"],
		["л","ل"],
		["д","د"],
		["о","ۈ"],
		["у","ۇ"],
		["ъ","ئ"],
		["(",""],
		[")",""]
]

def cyr2ajam(string):
  string = lowp(string)
  if string[0] in ["и","у","о"]:
    string = "ъ" + string
  if string[0] == "э":
    string = "ъе" + string[1:]
  for k,v in ajam_dict:
    string = string.replace(k,v)
  return string


latin_dict = [
		["ضّ","ⱬⱬ"],
		["گّ","ⱪⱪ"],
		["ڸّ","ꝉ"],
		["ڃّ","çç"],
		["ڸ","ļ"],
		["ض","ⱬ"],
		["گ","ⱪ"],
		["ق","q"],
		["ڨ","ꝗ"],
		["ڃ","ç"],
		["سّ","ss"],
		["ه","h"],
		["كّ","kk"],
		["چّ","cс"],
		["صّ","tsts"],
		["گ","ⱪ"],
		["ح","ћ"],
		["خّ","xx"],
		["ط","ƫ"],
		["ڮ","ҳ"],
		["ع","ⱨ"],
		["څ","ӿ"],
		["غ","ƣ"],
		["لّ","ll"],
		["ب","b"],
		["ر","r"],
		["ف","p"],
		["ل","l"],
		["ت","t"],
		["ز","z"],
		["ج","ƶ"],
		["س","s"],
		["م","m"],
		["ن","n"],
		["ش","ş"],
		["ك","k"],
		["چ","c"],
		["ص","ts"],
		["و","v"],
		["ي","j"],
		["ا","a"],
		["خ","x"],
		["ڬ","g"],
		["ڣ","f"],
		["ێ","i"],
		["ې","e"],
		["ل","l"],
		["د","d"],
		["ۈ","o"],
		["ۇ","u"],
		["ئ","'"]
]

def cyr2latin0(string):
  string = cyr2ajam(string)
  for k,v in latin_dict:
    string = string.replace(k,v)
  return string

latin_conv_dict = [
                ["ⱨ","gh"],
                ["c","ch"],
                ["с","ch"],
                ["ç","ch'"],
                ["ş","sh"], # conflicts with ["c","ch"]
                ["ڜ","sch"],
                ["ƫ","t'"],
                ["ⱪ","k'"],
                ["ļ","tl"],
                ["ꝉ","tltl"],
                ["ƶ","zh"],
                ["ƣ","qh"],
                ["ꝗ","ql"],
                ["ꝗ","q"],
                ["ӿ","kh"],
                ["ҳ","hl"],
                ["x","h"],
                ["ћ","h'"],
                ["ы","i"],
                ["j","y"],
                ["ts","c"],  # conflicts with ["c","ch"] and ["ç","ch'"]
                ["ⱬ","ts'"], # conflicts with ["ts","c"]
]

def latin2latin(string):
  if string[0] == "e": string = "y"+string
  if string[0:2] == "'o": string = string[1:]
  if string[0:2] == "'i": string = string[1:]
  if string[0:2] == "'u": string = string[1:]
  for k,v in latin_conv_dict:
    string = string.replace(k,v)
  return string

check_req_dict=[
            ("!","1"),
            ("|","1"),
            ("і","1"),
            ("Ӏ","1"),
            ("1","І"),
            ("l","І"),
            ("i","І"),
            ("ӏ","І")
          ]

def normalize_request(string):
  string = string.strip().split(" ")[0] # only words, no sentences support
  string = string.lower()               # need to rework this step. Currently all letters are treated as small-case
  for k,v in check_req_dict:            # every incorrect "palochka" should be replaced with correct WARNING 1, !
    string = string.replace(k,v)
  return string

if __name__ == '__main__':
  import sys
  import fileinput
  nr = normalize_request
  for line in fileinput.input():
    line = line.rstrip()
    line = nr(line)
    print(f'{line}:{cyr2latin0(line)}:{cyr2ajam(line)}:{cyr2latin(line)}')
