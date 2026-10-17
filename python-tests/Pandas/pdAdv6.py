#String manipulation
val = 'a,b,test,is a ,rule'
val.split(',')
pieces = [x.strip() for x in val.split(',')]
pieces
'::'.join(pieces)

'rule' in val
val.find('rules')
val.replace(',', '::')
val.replace(',', '')