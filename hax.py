import mcpi.minecraft as minecraft
friendsIP = ""
friendsPort = 25565
hackedMC = minecraft.Minecraft.create(address=friendsIP, port=friendsPort)
hackedMC.postToChat("Hello World")
