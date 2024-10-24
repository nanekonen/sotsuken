import os
import codecs
import re
from pygments.lexers import get_lexer_by_name
from pygments.lexers import get_lexer_for_filename
from pygments.token import Token

for curDir, dirs, ReadFiles in os.walk(""):
    for ReadFile in ReadFiles:
        PATH = os.path.join(curDir, ReadFile)
        with codecs.open(PATH, 'r', 'utf-8', 'ignore') as SourceCodeFile:
            filename = os.path.basename(PATH)
        
            try:
                lexer = get_lexer_for_filename(filename)
            except ValueError as e:
                continue
        
            if lexer.name != "Java":
                continue
    
            lines = SourceCodeFile.readlines()
            code = lines
            with open('seg_code_Java2.txt',mode='a', encoding='utf-8') as writeFile:
                for line in code:
                    token_it = lexer.get_tokens_unprocessed(line)
                    for idx, token_type, token_string in token_it:
                        if token_type in Token.Literal or token_type in Token.Comment or token_type in Token.Text :
                            continue
                        elif token_type in Token.Error or token_type in Token.Other or token_type in Token.Generic:
                            continue
                        else:
                            writeFile.write(token_string + ' ')