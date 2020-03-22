import aiml

kernel=aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml a")

print(kernel.respond(input("Enter a message: ")))