msg1 = "This is a new technology"
msg2 = "This needs to be used for processing"
umsg1 = msg1.upper()
lmsg2 = msg2.lower()
finalmsg = msg1 + " " + msg2 + " Note***"
print(finalmsg)
finalmsgf = f'{umsg1} {lmsg2} This is an imp note'
print(finalmsgf)

##using formatted string & place holders

first = "queen"
last = "elizabeth"
#simple concatenation
msg = first + ' [' + last + '] is a queen' 
print(msg)

#{}--defining place holders in a formatted string
msgf = f'{first} {last} is a queen'
print(msgf)
