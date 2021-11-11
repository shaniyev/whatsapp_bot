import pywhatkit as kt

print("Let's Automate Whatsapp!")
p_num = '+77776866457'#or you can use getpass module to capture cell num
# import getpass as gp
# p_num = gp.getpass(prompt='Phoneumber: ', stream=None)

msg = "I love Python"

kt.sendwhatmsg(p_num, msg,12,20)