import mano
import sys

print(mano.version_)

#try:
#print(sys.argv[0])
#print(len(sys.argv))
#if sys.argv[0] == "-version":
#print(mano.version_)
#except Exception as e:
#print(f"Unexpected error: {e}")

print(mano.state + ".n")
while True:
	comman = input("Python++ > ")
	cmd = comman
	results = mano.lexer(cmd)
			
	print(results)
