# Overview
Here is a list of all the projects I have done. I started off with very basic malware development and a technique for and Active Directory attack. From there I branched into wifi hacking, and now I'm focusing on web app research and building out offensive security tooling. Most of the tooling will be automation related, but I do have a few idea's which would be cool to publish.

For the web app stuff I'm currently looking into tomcat, XXE to RCE via gopher as I found this during a CTF and would like to automate some / most of the attack and gain a deeper understanding on how the attack works.

# Offsec Dev
This has it's own section:
[Offensive Security Tooling](Offsec%20Dev/README.md)

# Project Table
Newest at the top:

|Topic|Status|Overview|
|-|-|-|
|[Javaisbad](./Javaisbad.md)|In progress|Java is bad and getting a shell off a webapp running java is stupid. I found a one liner and decided to build a tool to do this automatically against tomcat applications.|
|[Wifi Hacking Part 1](./RPi%20wifi%20framework.md)|Done|Built out a framework for wifi deauthing and evil-twins on a RPi.|
|[Wifi Reseach](./Learning%20Wifi%20Attacks.md)|Done|Learning what wifi hacking is and how to do it.|
|[RBCD the hard-ish way](./RBCD%20-%20Without%20PowerView.md)|Done|Back before I knew you could disable AMSI I tried to load powerview and it got blocked. So I spent the next few days figuring out how to do the attack from native powershell.|

# Ideas
1. Look into building a lab for XXE to RCE via gopher.
2. Build a pivoting lab
3. Build an AD lab
