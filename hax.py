import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
friendsIP = ""
hackedMC = minecraft.Minecraft.create(friendsIP)
hackedMC.postToChat("Hello World")
