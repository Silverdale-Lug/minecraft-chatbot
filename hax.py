import mcpi.minecraft as minecraft
import sys

def usage():
    print("Usage: python %s IP_of_Minecraft_Server Port_of_Minecraft_Server"%sys.argv[0])
    exit(1)

if len(sys.argv) < 2:
    usage()

ip = sys.argv[1]
port = sys.argv[2]

mc = minecraft.Minecraft.create(address=str(ip), port=int(port))
x, y, z = mc.player.getPos()
mc.postToChat("Position: x: %f y: %f z: %f"% (x,y,z))
print(x,y,z)
