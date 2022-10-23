import re




with open(r"E:\Program\leviouseyon\text_editor\text.txt",'rt',encoding='utf-8') as fp:
    text=fp.readlines()
    fp.close()

with open(r"E:\Program\leviouseyon\text_editor\sample.txt",'a',encoding='utf-8') as f:
    for item in text:
        # item=re.sub(pattern='(.*)',repl='<p>\1</p>',string=item)
        item=re.sub(pattern='(第.*编.*)',repl='<div class=\'law_part\'>\1</div>',string=item)
        item=re.sub(pattern='(第.*章.*)',repl='<div class=\'law_chapter\'>\1</div>',string=item)
        item=re.sub(pattern='(第.*节.*)',repl='<div class=\'law_section\'>\1</div>',string=item) # 第几节
        item=re.sub(pattern='(第.*条)',repl='<div class=\'law_number\'>\1：</div>',string=item)
        item=re.sub(pattern='(【.*】)',repl='<mark>\1</mark>',string=item)  #立法目的高亮
        f.write(item)
        f.write('\n')
